from django.db import models

# How do I inspectdb table which contains space in own name
# https://stackoverflow.com/questions/27163702/how-do-i-inspectdb-1-table-from-database-which-contains-1000-tables

class NlcCustomer(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    no_field = models.CharField(db_column='No_', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed because it ended with '_'.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    search_name = models.CharField(db_column='Search Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name_2 = models.CharField(db_column='Name 2', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.CharField(db_column='Address', max_length=60)  # Field name made lowercase.
    address_2 = models.CharField(db_column='Address 2', max_length=60)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    city = models.CharField(db_column='City', max_length=30)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=30)  # Field name made lowercase.
    phone_no_field = models.CharField(db_column='Phone No_', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    telex_no_field = models.CharField(db_column='Telex No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    our_account_no_field = models.CharField(db_column='Our Account No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    territory_code = models.CharField(db_column='Territory Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    global_dimension_1_code = models.CharField(db_column='Global Dimension 1 Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    global_dimension_2_code = models.CharField(db_column='Global Dimension 2 Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chain_name = models.CharField(db_column='Chain Name', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    budgeted_amount = models.DecimalField(db_column='Budgeted Amount', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_limit_lcy_field = models.DecimalField(db_column='Credit Limit (LCY)', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    customer_posting_group = models.CharField(db_column='Customer Posting Group', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code = models.CharField(db_column='Currency Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_price_group = models.CharField(db_column='Customer Price Group', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    language_code = models.CharField(db_column='Language Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    statistics_group = models.IntegerField(db_column='Statistics Group')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_terms_code = models.CharField(db_column='Payment Terms Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fin_charge_terms_code = models.CharField(db_column='Fin_ Charge Terms Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesperson_code = models.CharField(db_column='Salesperson Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shipment_method_code = models.CharField(db_column='Shipment Method Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shipping_agent_code = models.CharField(db_column='Shipping Agent Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_export = models.CharField(db_column='Place of Export', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    invoice_disc_code = models.CharField(db_column='Invoice Disc_ Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_disc_group = models.CharField(db_column='Customer Disc_ Group', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_code = models.CharField(db_column='Country Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collection_method = models.CharField(db_column='Collection Method', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amount = models.DecimalField(db_column='Amount', max_digits=38, decimal_places=20)  # Field name made lowercase.
    blocked = models.IntegerField(db_column='Blocked')  # Field name made lowercase.
    invoice_copies = models.IntegerField(db_column='Invoice Copies')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_statement_no_field = models.IntegerField(db_column='Last Statement No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    print_statements = models.SmallIntegerField(db_column='Print Statements')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_to_customer_no_field = models.CharField(db_column='Bill-to Customer No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    payment_method_code = models.CharField(db_column='Payment Method Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_date_modified = models.DateTimeField(db_column='Last Date Modified')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    application_method = models.IntegerField(db_column='Application Method')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prices_including_vat = models.SmallIntegerField(db_column='Prices Including VAT')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_code = models.CharField(db_column='Location Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fax_no_field = models.CharField(db_column='Fax No_', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    telex_answer_back = models.CharField(db_column='Telex Answer Back', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vat_registration_no_field = models.CharField(db_column='VAT Registration No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    combine_shipments = models.SmallIntegerField(db_column='Combine Shipments')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gen_bus_posting_group = models.CharField(db_column='Gen_ Bus_ Posting Group', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    post_code = models.CharField(db_column='Post Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    county = models.CharField(db_column='County', max_length=30)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-Mail', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    home_page = models.CharField(db_column='Home Page', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reminder_terms_code = models.CharField(db_column='Reminder Terms Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_series = models.CharField(db_column='No_ Series', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tax_area_code = models.CharField(db_column='Tax Area Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tax_liable = models.SmallIntegerField(db_column='Tax Liable')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vat_bus_posting_group = models.CharField(db_column='VAT Bus_ Posting Group', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reserve = models.IntegerField(db_column='Reserve')  # Field name made lowercase.
    block_payment_tolerance = models.SmallIntegerField(db_column='Block Payment Tolerance')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ic_partner_code = models.CharField(db_column='IC Partner Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    primary_contact_no_field = models.CharField(db_column='Primary Contact No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    responsibility_center = models.CharField(db_column='Responsibility Center', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shipping_advice = models.IntegerField(db_column='Shipping Advice')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shipping_time = models.CharField(db_column='Shipping Time', max_length=32)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shipping_agent_service_code = models.CharField(db_column='Shipping Agent Service Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_zone_code = models.CharField(db_column='Service Zone Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notification_process_code = models.CharField(db_column='Notification Process Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    queue_priority = models.IntegerField(db_column='Queue Priority')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allow_line_disc_field = models.SmallIntegerField(db_column='Allow Line Disc_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    base_calendar_code = models.CharField(db_column='Base Calendar Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_sell_to_addr_to_qte_from = models.IntegerField(db_column='Copy Sell-to Addr_ to Qte From')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_bank_code = models.CharField(db_column='Default Bank Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_no_field = models.CharField(db_column='Vendor No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    act_signed_by_name = models.CharField(db_column='Act Signed by Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    act_signed_by_position = models.CharField(db_column='Act Signed by Position', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kpp_code = models.CharField(db_column='KPP Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tk_limit = models.DecimalField(db_column='TK Limit', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_counteragent_code = models.CharField(db_column='Default Counteragent Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    full_name = models.CharField(db_column='Full Name', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_3 = models.CharField(db_column='Address 3', max_length=60)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    respcenter_filter = models.CharField(db_column='RespCenter Filter', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    showcustomer = models.SmallIntegerField(db_column='ShowCustomer')  # Field name made lowercase.
    mailsendtocust = models.SmallIntegerField(db_column='MailSendToCust')  # Field name made lowercase.
    mailsendtospers = models.SmallIntegerField(db_column='MailSendToSPers')  # Field name made lowercase.
    delaydays = models.IntegerField(db_column='DelayDays')  # Field name made lowercase.
    lastsend = models.DateTimeField(db_column='LastSend')  # Field name made lowercase.
    nextsend = models.DateTimeField(db_column='NextSend')  # Field name made lowercase.
    debtdays = models.IntegerField(db_column='DebtDays')  # Field name made lowercase.
    customer_type = models.IntegerField(db_column='Customer Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    send_invoices_to_manager = models.SmallIntegerField(db_column='Send Invoices To Manager')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'NLC$Customer'
        unique_together = (('search_name', 'no_field'), ('customer_posting_group', 'no_field'), ('currency_code', 'no_field'), ('country_code', 'no_field'), ('gen_bus_posting_group', 'no_field'), ('name', 'address', 'city', 'no_field'), ('vat_registration_no_field', 'no_field'),)


class NlcGtdLedgerEntry(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    journal_batch_name = models.CharField(db_column='Journal Batch Name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    document_no_field = models.CharField(db_column='Document No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    posting_date = models.DateTimeField(db_column='Posting Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtddate = models.DateTimeField(db_column='GTDDate')  # Field name made lowercase.
    gtdcustom = models.CharField(db_column='GTDCustom', max_length=20)  # Field name made lowercase.
    gtdno_field = models.CharField(db_column='GTDNo_', max_length=40)  # Field name made lowercase. Field renamed because it ended with '_'.
    invoiceno_field = models.CharField(db_column='InvoiceNo_', max_length=10)  # Field name made lowercase. Field renamed because it ended with '_'.
    tir = models.CharField(db_column='TIR', max_length=30)  # Field name made lowercase.
    autonumber = models.CharField(db_column='AutoNumber', max_length=70)  # Field name made lowercase.
    itemcategory = models.CharField(db_column='ItemCategory', max_length=10)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=38, decimal_places=20)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=10)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=30)  # Field name made lowercase.
    addquantity = models.IntegerField(db_column='AddQuantity')  # Field name made lowercase.
    gtdquantity = models.DecimalField(db_column='GTDQuantity', max_digits=38, decimal_places=20)  # Field name made lowercase.
    responsibility_center = models.CharField(db_column='Responsibility Center', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_no_field = models.CharField(db_column='Customer No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    customer_name = models.CharField(db_column='Customer Name', max_length=60)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual = models.SmallIntegerField(db_column='Actual')  # Field name made lowercase.
    journal_template_name = models.CharField(db_column='Journal Template Name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_ledger_entry_no_field = models.IntegerField(db_column='Service Ledger Entry No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gtd_transport_kind = models.IntegerField(db_column='GTD Transport Kind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    global_dimension_1_code = models.CharField(db_column='Global Dimension 1 Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    global_dimension_2_code = models.CharField(db_column='Global Dimension 2 Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kpp = models.CharField(db_column='KPP', max_length=9)  # Field name made lowercase.
    delivery_type = models.IntegerField(db_column='Delivery Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_type = models.IntegerField(db_column='Service Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    svh_type = models.IntegerField(db_column='SVH Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    goods_location_code = models.CharField(db_column='Goods Location Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'NLC$GTD Ledger Entry'
        unique_together = (('document_no_field', 'posting_date', 'entry_no_field'), ('gtdno_field', 'entry_no_field'), ('customer_no_field', 'autonumber', 'gtdno_field', 'entry_no_field'), ('service_ledger_entry_no_field', 'tir', 'entry_no_field'),)


class NlcGtdJournalLine(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    journal_template_name = models.CharField(db_column='Journal Template Name', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    journal_batch_name = models.CharField(db_column='Journal Batch Name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    document_no_field = models.CharField(db_column='Document No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    posting_date = models.DateTimeField(db_column='Posting Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtddate = models.DateTimeField(db_column='GTDDate')  # Field name made lowercase.
    gtdcustom = models.CharField(db_column='GTDCustom', max_length=20)  # Field name made lowercase.
    gtdno_field = models.CharField(db_column='GTDNo_', max_length=40)  # Field name made lowercase. Field renamed because it ended with '_'.
    invoiceno_field = models.CharField(db_column='InvoiceNo_', max_length=10)  # Field name made lowercase. Field renamed because it ended with '_'.
    tir = models.CharField(db_column='TIR', max_length=30)  # Field name made lowercase.
    autonumber = models.CharField(db_column='AutoNumber', max_length=70)  # Field name made lowercase.
    itemcategory = models.CharField(db_column='ItemCategory', max_length=10)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=38, decimal_places=20)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=10)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=30)  # Field name made lowercase.
    addquantity = models.IntegerField(db_column='AddQuantity')  # Field name made lowercase.
    gtdquantity = models.DecimalField(db_column='GTDQuantity', max_digits=38, decimal_places=20)  # Field name made lowercase.
    responsibility_center = models.CharField(db_column='Responsibility Center', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_no_field = models.CharField(db_column='Customer No_', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actual = models.SmallIntegerField(db_column='Actual', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    gtd_transport_kind = models.IntegerField(db_column='GTD Transport Kind', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    global_dimension_1_code = models.CharField(db_column='Global Dimension 1 Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    global_dimension_2_code = models.CharField(db_column='Global Dimension 2 Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kpp = models.CharField(db_column='KPP', max_length=9)  # Field name made lowercase.
    delivery_type = models.IntegerField(db_column='Delivery Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_type = models.IntegerField(db_column='Service Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    svh_type = models.IntegerField(db_column='SVH Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    goods_location_code = models.CharField(db_column='Goods Location Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'NLC$GTD Journal Line'
        unique_together = (('journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'gtdno_field', 'autonumber', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'autonumber', 'gtdno_field', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'tir', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'itemcategory', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'mode', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'weight', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'addquantity', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'gtdquantity', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'gtddate', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('gtdno_field', 'journal_template_name', 'journal_batch_name', 'line_no_field'), ('customer_no_field', 'global_dimension_1_code', 'global_dimension_2_code', 'gtddate', 'journal_template_name', 'journal_batch_name', 'line_no_field'),)


class NlcSvhDocumentControlDetail(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    do_number = models.CharField(db_column='DO Number', max_length=60)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtd_no_field = models.CharField(db_column='GTD No_', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    guid = models.CharField(db_column='GUID', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NLC$SVH Document Control Detail'
        unique_together = (('entry_no_field', 'line_no_field'), ('gtd_no_field', 'entry_no_field', 'line_no_field'),)


class NlcSvhDocumentControlNumber(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    no_field = models.AutoField(db_column='No_', primary_key=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=50)  # Field name made lowercase.
    open = models.SmallIntegerField(db_column='Open')  # Field name made lowercase.
    items_description = models.CharField(db_column='Items Description', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_no_field = models.CharField(db_column='Customer No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tir = models.CharField(db_column='TIR', max_length=30)  # Field name made lowercase.
    cmr = models.CharField(db_column='CMR', max_length=50)  # Field name made lowercase.
    autonumber = models.CharField(db_column='AutoNumber', max_length=30)  # Field name made lowercase.
    location_licence = models.CharField(db_column='Location Licence', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_code = models.CharField(db_column='Location Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notification = models.CharField(db_column='Notification', max_length=60)  # Field name made lowercase.
    entrance_date = models.DateTimeField(db_column='Entrance Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exit_date = models.DateTimeField(db_column='Exit Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_date = models.DateTimeField(db_column='Location Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    document_date = models.DateTimeField(db_column='Document Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guid = models.CharField(db_column='GUID', max_length=8)  # Field name made lowercase.
    recieved = models.SmallIntegerField(db_column='Recieved')  # Field name made lowercase.
    removed = models.SmallIntegerField(db_column='Removed')  # Field name made lowercase.
    recieved_posted = models.SmallIntegerField(db_column='Recieved Posted')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    removed_posted = models.SmallIntegerField(db_column='Removed Posted')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    responsibility_center = models.CharField(db_column='Responsibility Center', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guid2 = models.CharField(db_column='GUID2', max_length=8)  # Field name made lowercase.
    change_inn_datetime = models.DateTimeField(db_column='Change INN Datetime')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    change_inn_user_id = models.CharField(db_column='Change INN User ID', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'NLC$SVH Document Control Number'
        unique_together = (('customer_no_field', 'no_field'), ('entrance_date', 'no_field'), ('cmr', 'no_field'), ('tir', 'no_field'), ('inn', 'no_field'),)