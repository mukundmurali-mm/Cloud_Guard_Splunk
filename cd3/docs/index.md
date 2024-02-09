# Understanding CD3?
CD3 stands for Cloud Deployment Design Deliverable and is a structured design-level representation of the future-state configuration for the customer’s OCI environment. The CD3 Automation toolkit is a processor that converts the detailed OCI design spec in the form of an Excel sheet into an executable Terraform code or takes an export of customer tenancy objects and resources and converts it back into a design spec in Excel format. The generated Terraform files can be reused  at any time to build similar infrastructure.

![CD3](https://blogs.oracle.com/content/published/api/v1.1/assets/CONT22A62EB11D894C46B73D779B9EF43085/Medium?cb=_cache_5a47&channelToken=f7814d202b7d468686f50574164024ec&format=jpg)


A graphic depicting the CD3 Automation toolkit process

The above image illustrates the process where information obtained during discovery sessions is utilized to create the CD3 Excel sheet. This Excel sheet serves as input for the Automation Toolkit, responsible for producing Terraform files. Once created, these Terraform files can be utilized to provision the resources on Oracle Cloud Infrastructure (OCI). The image also depicts that the toolkit can extract the data from OCI tenancy and populate the CD3 excel sheet.

