variable "location" {
    type = string
    sensitive = false
    default = "France Central"
}

variable "prod" {
    type = string
    sensitive = false
    default = "prod-saline"
}

variable "preprod" {
    type = string
    sensitive = false
    default = "preprod-saline"
}

variable "admin_username" {
    type = string
    sensitive = true
}

variable "admin_password" {
    type = string
    sensitive = true
}