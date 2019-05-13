# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
{
    "name": "Sales, Purchase, Invoices, Inventory, BOM, Scrap - All In One Barcode Scanner",

    'author' : 'Softhealer Technologies',
    
    'website': 'https://www.softhealer.com',
        
    "support": "info@softhealer.com",    
        
    'version': '12.0.2',
        
    "category": "Extra Tools",

    "summary": "This modules useful do quick operations of sales, purchases, invoicing and inventory, inventory adjustment, bill of material, scrap using barcode scanner.",   
        
    'description': """
    
        Do your time wasting in sales, purchases, invoices, inventory, inventory adjustment, bill of material, scrap operations by manual product selection ?
     So here is the solutions this modules useful do quick operations of sales, purchases, invoicing and inventory, bill of material, scrap using barcode scanner.
     You no need to select product and do one by one. scan it and you done!
     
    12 0 2 Becareful Quantity exceed than initial demand message added and product uom qty plus 1 condition added    
     
     
     """,
    
    "depends": ['purchase','sale_management','barcodes','account','stock','mrp'],
    
    "data": [
        
        'views/assets_backend.xml',
        'views/stock_scrap_view.xml',
    
    ],    
    'images': ['static/description/background.png',],            
    
    "installable": True,    
    "application": True,    
    "autoinstall": False,
    "price": 30,
    "currency": "EUR"        
}
