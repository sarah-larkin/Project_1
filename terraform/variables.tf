variable "files_prefix" {
    type = string                                  #string is the default
    default = "project-files-"
}
variable "S3_ingestion_prefix" {
    type = string                                  
    default = "project-1-ingestion-bucket-"
}

variable "S3_processed_prefix" {
    type = string 
    default = "project-1-processed-bucket-"
}

variable "environment" {
    type = string
    default = "Dev"
}