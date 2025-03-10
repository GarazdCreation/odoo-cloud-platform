# Copyright 2017-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    "name": "Cloud Platform Azure",
    "summary": "Addons required for the Camptocamp Cloud Platform on Azure",
    "version": "15.0.1.0.0",
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Extra Tools",
    "depends": [
        "cloud_platform",
        "attachment_azure",
        "monitoring_prometheus",
    ],
    "excludes": [
        "cloud_platform_ovh",
        "cloud_platform_exoscale",
    ],
    "website": "https://www.camptocamp.com",
    "data": [],
    "installable": True,
}
