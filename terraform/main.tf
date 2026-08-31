# 1. تحديد مزود الخدمة (AWS) والمنطقة
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# 2. إنشاء جدار ناري (Security Group)
resource "aws_security_group" "app_sg" {
  name        = "devops_app_security_group"
  description = "Allow SSH and HTTP traffic"

  # فتح منفذ الـ SSH (22) للدخول للسيرفر
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # فتح منفذ التطبيق (8000)
  ingress {
    description = "App Port"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # السماح للسيرفر بالاتصال بالإنترنت لتنزيل التحديثات
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 3. حجز السيرفر (EC2 Instance)
resource "aws_instance" "web_server" {
  ami  = "ami-0c7217cdde317cfec" # صورة نظام Ubuntu 22.04 الرسمية المجانية
  instance_type = "t2.micro"  # النوع المشمول في الباقة المجانية (Free Tier)

  vpc_security_group_ids = [aws_security_group.app_sg.id]

  # سكريبت يعمل تلقائياً عند إقلاع السيرفر لتثبيت Docker داخله فوراً
  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update -y
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo usermod -aG docker ubuntu
              EOF

  tags = {
    Name = "DevOps-Project-Server"
  }
}

# 4. طباعة الآي بي (Public IP) بعد إنشاء السيرفر
output "server_public_ip" {
  value       = aws_instance.web_server.public_ip
  description = "The Public IP of the created server"
}