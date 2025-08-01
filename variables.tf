variable "region" {
  default = "us-east-1"
}

variable "cluster_name" {
  default = "chicken-cluster"
}

variable "node_role_arn" {
  description = "IAM Role ARN for EKS node group"
  default     = "arn:aws:iam::<your-account-id>:role/<your-node-role>"
}

variable "user_arn" {
  description = "IAM User ARN for admin access"
  default     = "arn:aws:iam::<your-account-id>:user/<your-username>"
}
