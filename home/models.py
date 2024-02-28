from django.db import models




class Account(models.Model):
    id = models.BigIntegerField(primary_key=True)
    eid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'account'


class StockDetails(models.Model):
    id = models.BigIntegerField(primary_key=True)
    stock_id = models.UUIDField()
    ticker = models.CharField(blank=True, null=True)
    company_name = models.CharField(blank=True, null=True)
    sector = models.CharField(blank=True, null=True)
    industry = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    market_cap = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_e = models.CharField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    change = models.CharField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    upcoming_earnings = models.DateField(blank=True, null=True)
    etf = models.BooleanField(blank=True, null=True)
    is_options_exists = models.BooleanField(blank=True, null=True)
    round_lot_size = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'stock_details'


class StockScreener(models.Model):
    
    stock_screener_id = models.UUIDField(primary_key=True)
    run_date = models.DateField(blank=True, null=True)
    ticker = models.CharField(max_length=255, blank=True, null=True)
    market_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    upcoming_earnings_date = models.DateField(blank=True, null=True)
    is_earnings_within_2w = models.BooleanField(blank=True, null=True)
    analysts_ratings = models.CharField(max_length=255, blank=True, null=True)
    sma_indicator = models.CharField(max_length=255, blank=True, null=True)
    rsi_indicator = models.CharField(max_length=255, blank=True, null=True)
    put_l1_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    put_l1_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l1_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l1_volume = models.CharField(max_length=255, blank=True, null=True)
    put_l2_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    put_l2_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l2_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l2_volume = models.CharField(max_length=255, blank=True, null=True)
    put_l3_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    put_l3_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l3_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l3_volume = models.CharField(max_length=255, blank=True, null=True)
    put_l4_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    put_l4_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l4_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l4_volume = models.CharField(max_length=255, blank=True, null=True)
    put_l5_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    put_l5_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l5_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    put_l5_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l1_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    call_l1_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l1_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l1_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l2_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    call_l2_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l2_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l2_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l3_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    call_l3_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l3_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l3_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l4_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    call_l4_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l4_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l4_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l5_strikeprice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    call_l5_mid_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l5_mid_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    call_l5_volume = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'stock_screener'

class Employees(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Meta:
        db_table = 'employees'


class HomeProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.CharField(max_length=40, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'home_product'   

