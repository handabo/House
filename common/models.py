"""
业务实体
"""
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agent(models.Model):
    """经纪人"""
    agentid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    servstar = models.IntegerField(default=0)
    realstar = models.IntegerField(default=0)
    profstar = models.IntegerField(default=0)
    certificated = models.BooleanField(default=False)
    estates = models.ManyToManyField('Estate', through='AgentEstate')

    class Meta:
        managed = False
        db_table = 'tb_agent'


class AgentEstate(models.Model):
    """经纪人楼盘"""
    agent_estate_id = models.AutoField(primary_key=True)
    estate = models.ForeignKey('Estate', models.DO_NOTHING, db_column='estateid')
    agent = models.ForeignKey('Agent', models.DO_NOTHING, db_column='agentid')

    class Meta:
        managed = False
        db_table = 'tb_agent_estate'
        unique_together = (('estate', 'agent'),)


class District(models.Model):
    """地区"""
    distid = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='pid', blank=True, null=True)
    name = models.CharField(max_length=255)
    intro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tb_district'


class Estate(models.Model):
    """楼盘"""
    estateid = models.AutoField(primary_key=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='distid')
    name = models.CharField(max_length=255)
    hot = models.IntegerField(default=0, blank=True, null=True)
    intro = models.CharField(max_length=511, blank=True, null=True)
    agents = models.ManyToManyField('Agent', through='AgentEstate')

    class Meta:
        managed = False
        db_table = 'tb_estate'


class HouseInfo(models.Model):
    """房源信息"""
    houseid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    area = models.IntegerField()
    floor = models.IntegerField()
    totalfloor = models.IntegerField()
    direction = models.CharField(max_length=10)
    price = models.IntegerField()
    priceunit = models.CharField(max_length=10)
    detail = models.CharField(max_length=511, blank=True, null=True)
    mainphoto = models.CharField(max_length=255)
    pubdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    street = models.CharField(max_length=255)
    hassubway = models.IntegerField()
    isshared = models.IntegerField()
    hasagentfees = models.IntegerField()
    type = models.ForeignKey('HouseType', models.DO_NOTHING, db_column='typeid')
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='distid')
    estate = models.ForeignKey('Estate', models.DO_NOTHING, db_column='estateid', blank=True, null=True)
    agent = models.ForeignKey('Agent', models.DO_NOTHING, db_column='agentid', blank=True, null=True)
    tags = models.ManyToManyField('Tag', through='HouseTag')

    class Meta:
        managed = False
        db_table = 'tb_house_info'


class HousePhoto(models.Model):
    """房源照片"""
    photoid = models.AutoField(primary_key=True)
    house = models.ForeignKey('HouseInfo', on_delete=models.DO_NOTHING, db_column='houseid')
    path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_house_photo'


class HouseTag(models.Model):
    """房源标签"""
    house_tag_id = models.AutoField(primary_key=True)
    tag = models.ForeignKey('Tag', on_delete=models.DO_NOTHING, db_column='tagid')
    house = models.ForeignKey('HouseInfo', on_delete=models.DO_NOTHING, db_column='houseid')

    class Meta:
        managed = False
        db_table = 'tb_house_tag'
        unique_together = (('tag', 'house'),)


class HouseType(models.Model):
    """房源户型"""

    typeid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_house_type'


class LoginLog(models.Model):
    """登录日志"""

    logid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, db_column='userid')
    ipaddr = models.CharField(max_length=255)
    logdate = models.DateTimeField(auto_now_add=True)
    devcode = models.CharField(max_length=255, default='')

    class Meta:
        managed = False
        db_table = 'tb_login_log'


class Record(models.Model):
    """浏览记录"""

    recordid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, db_column='userid')
    house = models.ForeignKey('HouseInfo', on_delete=models.DO_NOTHING, db_column='houseid')
    recorddate = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'tb_record'
        unique_together = (('user', 'house'),)


class Tag(models.Model):
    """标签"""

    tagid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_tag'


class User(models.Model):
    """用户"""

    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=32)
    realname = models.CharField(max_length=20)
    tel = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=255)
    createdate = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=32)
    point = models.IntegerField(default=0)
    lastvisit = models.DateTimeField(auto_now_add=True)
    isagent = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'tb_user'
