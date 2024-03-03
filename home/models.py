from django.db import models

# class StockDetails(models.Model):
#     stock_id = models.UUIDField(primary_key=True,)
#     ticker = models.CharField(blank=True, null=True)
#     company_name = models.CharField(blank=True, null=True)
#     sector = models.CharField(blank=True, null=True)
#     industry = models.CharField(blank=True, null=True)
#     country = models.CharField(blank=True, null=True)
#     market_cap = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     p_e = models.CharField(blank=True, null=True)
#     price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     change = models.CharField(blank=True, null=True)
#     volume = models.IntegerField(blank=True, null=True)
#     upcoming_earnings = models.DateField(blank=True, null=True)
#     etf = models.BooleanField(blank=True, null=True)
#     is_options_exists = models.BooleanField(blank=True, null=True)
#     round_lot_size = models.IntegerField(blank=True, null=True)
#     create_date = models.DateTimeField(blank=True, null=True)
#     update_date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = 'stock_details'


# class StockScreener(models.Model):
    
#     stock_screener_id = models.UUIDField(primary_key=True)
#     run_date = models.DateField(blank=True, null=True)
#     ticker = models.CharField(max_length=255, blank=True, null=True)
#     market_price = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     exp_date = models.DateField(blank=True, null=True)
#     upcoming_earnings_date = models.DateField(blank=True, null=True)
#     is_earnings_within_2w = models.BooleanField(blank=True, null=True)
#     analysts_ratings = models.CharField(max_length=255, blank=True, null=True)
#     sma_indicator = models.CharField(max_length=255, blank=True, null=True)
#     rsi_indicator = models.CharField(max_length=255, blank=True, null=True)
#     put_l1_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     put_l1_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l1_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l1_volume = models.CharField(max_length=255, blank=True, null=True)
#     put_l2_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     put_l2_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l2_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l2_volume = models.CharField(max_length=255, blank=True, null=True)
#     put_l3_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     put_l3_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l3_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l3_volume = models.CharField(max_length=255, blank=True, null=True)
#     put_l4_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     put_l4_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l4_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l4_volume = models.CharField(max_length=255, blank=True, null=True)
#     put_l5_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     put_l5_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l5_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     put_l5_volume = models.CharField(max_length=255, blank=True, null=True)
#     call_l1_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     call_l1_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l1_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l1_volume = models.CharField(max_length=255, blank=True, null=True)
#     call_l2_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     call_l2_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l2_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l2_volume = models.CharField(max_length=255, blank=True, null=True)
#     call_l3_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     call_l3_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l3_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l3_volume = models.CharField(max_length=255, blank=True, null=True)
#     call_l4_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     call_l4_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l4_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l4_volume = models.CharField(max_length=255, blank=True, null=True)
#     call_l5_strikeprice = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     call_l5_mid_percent = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l5_mid_price = models.DecimalField(
#         max_digits=5, decimal_places=2, blank=True, null=True)
#     call_l5_volume = models.CharField(max_length=255, blank=True, null=True)
#     create_date = models.DateTimeField(blank=True, null=True)
#     update_date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = 'stock_screener'


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class StockDetails(models.Model):
    stock_id = models.UUIDField()
    ticker = models.CharField(blank=True, null=True)
    company_name = models.CharField(blank=True, null=True)
    sector = models.CharField(blank=True, null=True)
    industry = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    market_cap = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_e = models.CharField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    change = models.CharField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    upcoming_earnings = models.DateField(blank=True, null=True)
    etf = models.BooleanField(blank=True, null=True)
    is_options_exists = models.BooleanField(blank=True, null=True)
    round_lot_size = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_details'

class StockScreener(models.Model):
    stock_screener_id = models.UUIDField(primary_key=True)
    run_date = models.DateField(blank=True, null=True)
    ticker = models.CharField(max_length=255, blank=True, null=True)
    market_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    upcoming_earnings_date = models.DateField(blank=True, null=True)
    is_earnings_within_2w = models.BooleanField(blank=True, null=True)
    analysts_ratings = models.CharField(max_length=255, blank=True, null=True)
    sma_indicator = models.CharField(max_length=255, blank=True, null=True)
    rsi_indicator = models.CharField(max_length=255, blank=True, null=True)
    put_l1_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l1_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l1_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l1_volume = models.CharField(max_length=255, blank=True, null=True)
    put_l2_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l2_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l2_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l2_volume = models.CharField(max_length=255, blank=True, null=True)
    put_l3_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l3_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l3_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l3_volume = models.CharField(max_length=255, blank=True, null=True)
    put_l4_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l4_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l4_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l4_volume = models.CharField(max_length=255, blank=True, null=True)
    put_l5_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l5_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l5_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    put_l5_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l1_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l1_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l1_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l1_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l2_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l2_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l2_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l2_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l3_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l3_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l3_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l3_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l4_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l4_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l4_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l4_volume = models.CharField(max_length=255, blank=True, null=True)
    call_l5_strikeprice = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l5_mid_percent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l5_mid_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    call_l5_volume = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_screener'



class Account(models.Model):
    account_id = models.UUIDField(primary_key=True)
    brokerage_name = models.CharField(blank=True, null=True)
    brokerage_account = models.CharField(blank=True, null=True)
    brokerage_account_type = models.CharField(blank=True, null=True)
    account_alias_number = models.CharField(blank=True, null=True)
    subscription_plan_name = models.CharField(blank=True, null=True)
    prefix = models.CharField(blank=True, null=True)
    full_name = models.CharField(blank=True, null=True)
    suffix = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    access_token = models.CharField(blank=True, null=True)
    account_initial_value = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    accrued_interest = models.CharField(blank=True, null=True)
    is_admin_approved = models.BooleanField(blank=True, null=True)
    is_monthly_email_report_enabled = models.BooleanField(
        blank=True, null=True)
    is_weekly_email_report_enabled = models.BooleanField(blank=True, null=True)
    is_dev_mode = models.BooleanField(blank=True, null=True)
    is_day_trader = models.BooleanField(blank=True, null=True)
    is_invoice_eligible = models.BooleanField(blank=True, null=True)
    is_subscribed = models.BooleanField(blank=True, null=True)
    is_token_generation_allowed = models.BooleanField(blank=True, null=True)
    cash_available_for_trading = models.CharField(blank=True, null=True)
    cash_available_for_withdrawal = models.CharField(blank=True, null=True)
    consumer_key = models.CharField(blank=True, null=True)
    date_of_first_run = models.DateTimeField(blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    liquidation_value = models.CharField(blank=True, null=True)
    refresh_token = models.CharField(blank=True, null=True)
    refresh_token_updated_date = models.DateTimeField(blank=True, null=True)
    ticker_selection = models.CharField(blank=True, null=True)
    account_type = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    is_enabled_early_profitbooking = models.BooleanField(blank=True, null=True)
    is_market_watch_enabled = models.BooleanField(blank=True, null=True)
    is_enabled_stoploss_cc = models.BooleanField(blank=True, null=True)
    is_enabled_stoploss_csp = models.BooleanField(blank=True, null=True)
    account_balance = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    new_subscription_plan = models.CharField(blank=True, null=True)
    new_plan_effective_date = models.DateField(blank=True, null=True)
    payment_status = models.CharField(blank=True, null=True)
    invoice_contact_id = models.CharField(
        max_length=100, blank=True, null=True)
    recurring_invoice_id = models.CharField(
        max_length=100, blank=True, null=True)
    early_exit_profit_percentage = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    ondemand_wheel_execution = models.BooleanField(blank=True, null=True)
    account_alias_name = models.CharField(blank=True, null=True)
    enable_whatsapp_alerts = models.BooleanField(blank=True, null=True)
    enable_sms_alerts = models.BooleanField(blank=True, null=True)
    ticker_txn_dates = models.CharField(
        max_length=10000, blank=True, null=True)
    strategy_configs = models.CharField(blank=True, null=True)
    remarks = models.CharField(blank=True, null=True)
    strategy_short_put_spreads = models.CharField(blank=True, null=True)
    strategy_long_call_spreads = models.CharField(blank=True, null=True)
    strategy_based_amount_allocation = models.CharField(blank=True, null=True)
    realized_income = models.FloatField(blank=True, null=True)
    un_realized_income = models.FloatField(blank=True, null=True)
    brokerage_trading_type = models.CharField(blank=True, null=True)
    brokerage_clearing_status = models.CharField(blank=True, null=True)
    brokerage_noclient_trading = models.BooleanField(blank=True, null=True)
    brokerage_business_type = models.CharField(blank=True, null=True)
    account_category = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    last_invoice_create_date = models.DateField(blank=True, null=True)
    strategy_long_call_spreads_daily = models.CharField(blank=True, null=True)
    billing_customer_secret = models.CharField(
        max_length=255, blank=True, null=True)
    billing_contact_id = models.CharField(
        max_length=255, blank=True, null=True)
    billing_period_start = models.DateField(blank=True, null=True)
    billing_period_end = models.DateField(blank=True, null=True)
    subscription_plan_description = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class AccountDailySummary(models.Model):
    account_summary_id = models.UUIDField(primary_key=True)
    account_id = models.UUIDField(blank=True, null=True)
    summary_date = models.DateField(blank=True, null=True)
    account_ending_balance = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    account_starting_balance = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    cash_balance = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    daily_net_fee = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    day_profit_loss = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    day_profit_loss_per_10k = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    day_profit_loss_percentage = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_subscribed = models.BooleanField(blank=True, null=True)
    till_date_profit_loss = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    unsettled_cash = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    ytd_profit_loss = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    settled_cash = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    realized_pnl = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    unrealized_pnl = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    qg_unrealized_pnl = models.FloatField(blank=True, null=True)
    qg_realized_pnl = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_daily_summary'


class AccountPortfolio(models.Model):
    account_portfolio_id = models.UUIDField(primary_key=True)
    account_id = models.UUIDField(blank=True, null=True)
    ticker_symbol = models.CharField(blank=True, null=True)
    present_date = models.DateField(blank=True, null=True)
    position_status = models.CharField(blank=True, null=True)
    last_updated_date = models.DateField(blank=True, null=True)
    underlying_symbol = models.CharField(blank=True, null=True)
    put_call = models.CharField(blank=True, null=True)
    qty = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    long_quantity = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    settled_long_quantity = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    settled_short_quantity = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    short_quantity = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    previous_session_long_quantity = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    asset_type = models.CharField(blank=True, null=True)
    average_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    current_day_cost = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    current_day_profit_loss = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    current_day_profit_loss_percentage = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    maintenance_requirement = models.CharField(blank=True, null=True)
    market_value = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    current_market_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    underlying_name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_portfolio'


class ActivityLog(models.Model):
    activity_id = models.UUIDField()
    account_id = models.UUIDField(blank=True, null=True)
    event_name = models.CharField(blank=True, null=True)
    criticality = models.CharField(blank=True, null=True)
    json_payload = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_log'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CommunityInsights(models.Model):
    insights_id = models.UUIDField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    strategy = models.CharField(blank=True, null=True)
    symbol = models.CharField(blank=True, null=True)
    market_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    avg_premium = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    avg_premium_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    total_cc_contracts = models.IntegerField(blank=True, null=True)
    total_csp_contracts = models.IntegerField(blank=True, null=True)
    num_times_cc_profit_exit = models.IntegerField(blank=True, null=True)
    num_times_csp_profit_exit = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    filled_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_insights'


class CustomerInvoice(models.Model):
    invoice_id = models.CharField(primary_key=True)
    account_id = models.CharField(blank=True, null=True)
    invoice_number = models.CharField(blank=True, null=True)
    invoice_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_currency = models.CharField(blank=True, null=True)
    invoice_description = models.CharField(blank=True, null=True)
    invoice_generation_system = models.CharField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    invoice_start_date = models.DateField(blank=True, null=True)
    invoice_end_date = models.DateField(blank=True, null=True)
    invoice_due_date = models.DateField(blank=True, null=True)
    invoice_paid_status = models.CharField(blank=True, null=True)
    invoice_payment_link = models.CharField(blank=True, null=True)
    account_begining_balance = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    adjustment_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    adjustment_description = models.CharField(blank=True, null=True)
    paid_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)
    recurrence_name = models.CharField(blank=True, null=True)
    reference_number = models.CharField(blank=True, null=True)
    repeat_every = models.CharField(blank=True, null=True)
    subscription_plan_name = models.CharField(blank=True, null=True)
    tax_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_invoice'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoTruncateModel1(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_truncate_model1'


class DjangoTruncateModel2(models.Model):
    name = models.CharField(max_length=200)
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'django_truncate_model2'


class GlobalConfig(models.Model):
    global_config_id = models.CharField(blank=True, null=True)
    global_config_description = models.CharField(blank=True, null=True)
    key = models.CharField(blank=True, null=True)
    value = models.CharField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_config'


class OptionsActivity(models.Model):
    option_activity_id = models.UUIDField(primary_key=True)
    account_id = models.UUIDField(blank=True, null=True)
    api_request_text = models.CharField(blank=True, null=True)
    api_response_text = models.CharField(blank=True, null=True)
    cash_balance_effect_flag = models.BooleanField(blank=True, null=True)
    day_trade_buying_power_effect = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    instrument_asset_type = models.CharField(blank=True, null=True)
    instrument_cusip = models.CharField(blank=True, null=True)
    item_instruction = models.CharField(blank=True, null=True)
    net_total_fees = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    net_total_transaction_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    net_transaction_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    option_expiration_date = models.DateField(blank=True, null=True)
    options_type = models.CharField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    order_id = models.CharField(blank=True, null=True)
    position_effect = models.CharField(blank=True, null=True)
    remarks = models.CharField(blank=True, null=True)
    total_fees = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    transaction_total_cost = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    transaction_type = models.CharField(blank=True, null=True)
    instrument_description = models.CharField(blank=True, null=True)
    mark_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    order_source = models.CharField(blank=True, null=True)
    qty = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    strike_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    underlying_symbol = models.CharField(blank=True, null=True)
    ticker_symbol = models.CharField(blank=True, null=True)
    underlying_equity_trade_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    underlying_equity_mark_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    transaction_id = models.CharField(blank=True, null=True)
    call_ask_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    exercise_profit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    net_credit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    put_call_type = models.CharField(blank=True, null=True)
    status_description = models.CharField(blank=True, null=True)
    trade_strategy = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    account_portfolio = models.CharField(blank=True, null=True)
    contract_id = models.CharField(max_length=100, blank=True, null=True)
    filled_qty = models.CharField(blank=True, null=True)
    remaining_qty = models.CharField(blank=True, null=True)
    entry_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    exit_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    # Field name made lowercase.
    outcomestatus = models.CharField(
        db_column='outcomeStatus', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options_activity'


class Profile(models.Model):
    profile_id = models.UUIDField(primary_key=True)
    display_name = models.CharField()
    prefix = models.CharField(blank=True, null=True)
    full_name = models.CharField()
    suffix = models.CharField(blank=True, null=True)
    email = models.CharField(unique=True)
    phone_number = models.CharField(blank=True, null=True)
    is_admin_approved = models.BooleanField(blank=True, null=True)
    is_profile_active = models.BooleanField(blank=True, null=True)
    is_super_admin = models.BooleanField(blank=True, null=True)
    is_subscribed = models.BooleanField(blank=True, null=True)
    profile_enrolled_batch = models.CharField(blank=True, null=True)
    profile_pwd = models.CharField(blank=True, null=True)
    profile_temp_otp = models.CharField(blank=True, null=True)
    subscribed_strategies = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    is_support_admin = models.BooleanField(blank=True, null=True)
    is_profile_details_updated = models.BooleanField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    zip_code = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    profile_picture = models.CharField(blank=True, null=True)
    profile_theme = models.CharField(blank=True, null=True)
    referral_code = models.CharField(blank=True, null=True)
    referral_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_invoice_create_date = models.DateField(blank=True, null=True)
    invoice_contact_id = models.CharField(blank=True, null=True)
    recurring_invoice_id = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'


class ProfileAccountRelationship(models.Model):
    relationship_id = models.CharField(primary_key=True)
    profile_id = models.UUIDField(blank=True, null=True)
    account_id = models.UUIDField(blank=True, null=True)
    access_role_type = models.CharField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_account_relationship'


class ProfileDetails(models.Model):
    profile_details_id = models.UUIDField()
    date_of_birth = models.DateField(blank=True, null=True)
    home_phone = models.CharField(blank=True, null=True)
    mobile_phone = models.CharField(blank=True, null=True)
    work_phone = models.CharField(blank=True, null=True)
    permanent_address = models.CharField(blank=True, null=True)
    apt_or_suite_no = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    zip_code = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    country_of_tax_residence = models.CharField(blank=True, null=True)
    country_of_citizenship = models.CharField(blank=True, null=True)
    place_or_country_of_issuance = models.CharField(blank=True, null=True)
    id_number = models.CharField(blank=True, null=True)
    id_type = models.CharField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    advisory_agreement = models.CharField(blank=True, null=True)
    advisory_customer_relationship_summary_agreement = models.CharField(
        blank=True, null=True)
    advisory_legal_disclosures_agreement = models.CharField(
        blank=True, null=True)
    advisory_privacy_policy_agreement = models.CharField(blank=True, null=True)
    annual_expenses = models.CharField(blank=True, null=True)
    annual_income = models.CharField(blank=True, null=True)
    employment_status = models.CharField(blank=True, null=True)
    marital_status = models.CharField(blank=True, null=True)
    degree_of_risk = models.CharField(blank=True, null=True)
    expected_period_of_time_invest = models.CharField(blank=True, null=True)
    investment_risk_tolerance = models.CharField(blank=True, null=True)
    investment_time_horizon = models.CharField(blank=True, null=True)
    investment_tranperyr_alternative = models.CharField(blank=True, null=True)
    investment_tranperyr_annuities = models.CharField(blank=True, null=True)
    investment_tranperyr_bonds = models.CharField(blank=True, null=True)
    investment_tranperyr_mf_etf = models.CharField(blank=True, null=True)
    investment_tranperyr_margin = models.CharField(blank=True, null=True)
    investment_tranperyr_options = models.CharField(blank=True, null=True)
    investment_tranperyr_securities_futures = models.CharField(
        blank=True, null=True)
    investment_tranperyr_stocks = models.CharField(blank=True, null=True)
    investment_yoe_alternative = models.CharField(blank=True, null=True)
    investment_yoe_annuities = models.CharField(blank=True, null=True)
    investment_yoe_bonds = models.CharField(blank=True, null=True)
    investment_yoe_mf_etf = models.CharField(blank=True, null=True)
    investment_yoe_margin = models.CharField(blank=True, null=True)
    investment_yoe_options = models.CharField(blank=True, null=True)
    investment_yoe_securities_futures = models.CharField(blank=True, null=True)
    investment_yoe_stocks = models.CharField(blank=True, null=True)
    liquid_net_worth = models.CharField(blank=True, null=True)
    liquidity_needs = models.CharField(blank=True, null=True)
    net_worth = models.CharField(blank=True, null=True)
    no_of_dependents = models.CharField(blank=True, null=True)
    plan_to_use_this_account = models.CharField(blank=True, null=True)
    special_expenses = models.CharField(blank=True, null=True)
    tax_rate = models.CharField(blank=True, null=True)
    funding = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    profile = models.ForeignKey(
        Profile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_details'


class ReferralActivity(models.Model):
    referral_id = models.UUIDField(blank=True, null=True)
    referral_type = models.CharField(blank=True, null=True)
    referral_code = models.CharField(blank=True, null=True)
    referred_by_profile_id = models.CharField(blank=True, null=True)
    referred_to_profile_id = models.CharField(blank=True, null=True)
    referral_datetime = models.DateTimeField(blank=True, null=True)
    referral_status = models.CharField(blank=True, null=True)
    referral_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    referral_paid_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referral_activity'


class ReferralLookup(models.Model):
    referral_type = models.CharField(blank=True, null=True)
    referral_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referral_lookup'


class SupportRequest(models.Model):
    request_id = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    account_alias_name = models.CharField(blank=True, null=True)
    is_applicable_to_all_accounts = models.BooleanField(blank=True, null=True)
    module_name = models.CharField(blank=True, null=True)
    criticality = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    notes = models.CharField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    support_request_id = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_request'


class SystemActivity(models.Model):
    activity_id = models.CharField()
    profile_id = models.CharField(blank=True, null=True)
    account_id = models.CharField(blank=True, null=True)
    table_name = models.CharField(blank=True, null=True)
    column_name = models.CharField(blank=True, null=True)
    new_value = models.CharField(blank=True, null=True)
    old_value = models.CharField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_activity'


class TransactionActivity(models.Model):
    transaction_activity_id = models.UUIDField(primary_key=True)
    account_id = models.UUIDField(blank=True, null=True)
    transaction_id = models.CharField(blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    transaction_total_cost = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    transaction_type = models.CharField(blank=True, null=True)
    additional_status = models.CharField(blank=True, null=True)
    cash_balance_effect_flag = models.BooleanField(blank=True, null=True)
    day_trade_buying_power_effect = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    instrument_asset_type = models.CharField(blank=True, null=True)
    instrument_cusip = models.CharField(blank=True, null=True)
    item_instruction = models.CharField(blank=True, null=True)
    net_total_fees = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    net_total_transaction_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    net_transaction_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    option_expiration_date = models.DateField(blank=True, null=True)
    options_type = models.CharField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    order_id = models.CharField(blank=True, null=True)
    order_source = models.CharField(blank=True, null=True)
    position_effect = models.CharField(blank=True, null=True)
    remarks = models.CharField(blank=True, null=True)
    underlying_symbol = models.CharField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    instrument_description = models.CharField(blank=True, null=True)
    mark_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    put_call_type = models.CharField(blank=True, null=True)
    qty = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    status_description = models.CharField(blank=True, null=True)
    strike_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    underlying_equity_mark_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    underlying_equity_trade_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    ticker_symbol = models.CharField(blank=True, null=True)
    trade_strategy = models.CharField(blank=True, null=True)
    exercise_profit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    net_credit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    settlement_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    contract_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_activity'
