from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    decimals = models.BigIntegerField()

    def __str__(self):
        return self.name


class Dex(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    abi = models.TextField()

    def __str__(self):
        return self.name


class CoinPair(models.Model):
    coin_1 = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='coin_1', blank=True, null=True)
    coin_2 = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='coin_2', blank=True, null=True)

    def __str__(self):
        return f"{self.coin_1} ---- {self.coin_2}"


class DexPair(models.Model):
    dex_1 = models.ForeignKey(Dex, on_delete=models.CASCADE, related_name='dex_1', blank=True, null=True)
    dex_2 = models.ForeignKey(Dex, on_delete=models.CASCADE, related_name='dex_2', blank=True, null=True)

    def __str__(self):
        return f"{self.dex_1} ---- {self.dex_2}"


class Setting(models.Model):
    # total_deposit_amount = models.IntegerField()
    # total_tax_collected = models.IntegerField()
    # slippage = models.IntegerField()
    # minimum_price_difference = models.FloatField()
    # maximum_gas_price = models.IntegerField()
    # start_pause = models.BooleanField(default=False)
    tax_percentage = models.FloatField()
    taxation_address = models.CharField(max_length=255)
    min_deposit_amount = models.IntegerField()
    max_deposit_amount = models.IntegerField()


class BotManager(models.Model):
    start_pause = models.BooleanField(default=False, verbose_name=' Off | On')
    maximum_gas_price = models.IntegerField()
    slippage = models.IntegerField()

    class Meta:
        verbose_name_plural = "Bot Manager"

    # total_deposit_amount = models.IntegerField()
    # total_tax_collected = models.IntegerField()
    # minimum_price_difference = models.FloatField()


class Result(models.Model):
    coin_pair = models.CharField(max_length=255)
    price_difference = models.CharField(max_length=255)
    dex_pair = models.CharField(max_length=255)
    percentage = models.FloatField()
    date = models.TextField(null=True, blank=True)
    dexes = models.CharField(max_length=255)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class Whitelist(models.Model):
    file = models.FileField(upload_to='uploads/')

    class Meta:
        verbose_name_plural = 'Whitelisted accounts'

    def file_link(self):
        if self.file:
            return "<a href='%s'>download</a>" % (self.file.url,)
        else:
            return "No attachment"

    file_link.allow_tags = True


class Analytics(models.Model):
    class Meta:
        verbose_name_plural = 'Analytics'

    total_tax_collected = models.CharField(max_length=255)
    current_total_balance = models.CharField(max_length=255)
    total_deposit_amount = models.CharField(max_length=255)
    transaction_list = models.CharField(max_length=255)