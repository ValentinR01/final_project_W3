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