from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class Platform(models.Model):
    P_key = models.AutoField(primary_key=True)
    P_url = models.CharField(max_length=500)
    P_userkey = models.CharField(max_length=10)
    P_name = models.CharField(max_length=10)
    objects = models.Manager()


class User_info(models.Model):
    U_key = models.AutoField(primary_key=True)
    U_name = models.CharField(max_length=500)
    U_img = models.CharField(max_length=500)
    U_info = models.CharField(max_length=500)
    U_sudate = models.CharField(max_length=20)
    P_key = models.ForeignKey(
        Platform, related_name="User", on_delete=models.CASCADE)
    objects = models.Manager()


class Subscribe(models.Model):
    S_key = models.AutoField(primary_key=True)
    created_at = models.CharField(max_length=15)
    S_count = models.IntegerField(default=0)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    week = models.CharField(max_length=4)
    day = models.CharField(max_length=2)
    P_key = models.ForeignKey(
        Platform, related_name="Sub", on_delete=models.CASCADE)
    objects = models.Manager()


class Video(models.Model):
    V_key = models.AutoField(primary_key=True)
    V_name = models.CharField(max_length=500)
    V_upload = models.CharField(max_length=100)
    like_A_Y = models.CharField(max_length=10)
    dislike_Y = models.CharField(max_length=10)
    view_A_Y_T = models.CharField(max_length=10)
    comment_A_Y = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    week = models.CharField(max_length=4)
    day = models.CharField(max_length=2)
    P_key = models.ForeignKey(
        Platform, related_name="Video", on_delete=models.CASCADE)
    objects = models.Manager()


class Total(models.Model):
    T_key = models.AutoField(primary_key=True)
    T_like_count_A_Y= models.IntegerField(default=0)
    T_unlike_count_Y = models.IntegerField(default=0)
    T_view_count_Y_A_T = models.IntegerField(default=0)
    T_update = models.DateField(null=False)
    P_key = models.ForeignKey(
        Platform, related_name="Total", on_delete=models.CASCADE)
    objects = models.Manager()


class D_sub_gap(models.Model):
    SD_key = models.AutoField(primary_key=True)
    sub_count = models.IntegerField(default=0)
    P_key = models.ForeignKey(
        Platform, related_name="SD_gap", on_delete=models.CASCADE)
    objects = models.Manager()


class W_sub_gap(models.Model):
    SW_key = models.AutoField(primary_key=True)
    sub_count = models.IntegerField(default=0)
    P_key = models.ForeignKey(
        Platform, related_name="SW_gap", on_delete=models.CASCADE)
    objects = models.Manager()


class M_sub_gap(models.Model):
    SM_key = models.AutoField(primary_key=True)
    sub_count = models.IntegerField(default=0)
    P_key = models.ForeignKey(
        Platform, related_name="SM_gap", on_delete=models.CASCADE)
    objects = models.Manager()


class D_video_gap(models.Model):
    VD_key = models.AutoField(primary_key=True)
    like_A_Y = models.IntegerField(default=0)
    dislike_Y = models.IntegerField(default=0)
    view_A_Y_T = models.IntegerField(default=0)
    comment_A_Y = models.IntegerField(default=0)
    P_key = models.ForeignKey(
        Platform, related_name="VD_gap", on_delete=models.CASCADE)
    objects = models.Manager()


class W_video_gap(models.Model):
    VW_key = models.AutoField(primary_key=True)
    like_A_Y = models.IntegerField(default=0)
    dislike_Y = models.IntegerField(default=0)
    view_A_Y_T = models.IntegerField(default=0)
    comment_A_Y = models.IntegerField(default=0)
    P_key = models.ForeignKey(
        Platform, related_name="VW_gap", on_delete=models.CASCADE)
    objects = models.Manager()


class M_video_gap(models.Model):
    VM_key = models.AutoField(primary_key=True)
    like_A_Y = models.IntegerField(default=0)
    dislike_Y = models.IntegerField(default=0)
    view_A_Y_T = models.IntegerField(default=0)
    comment_A_Y = models.IntegerField(default=0)
    P_key = models.ForeignKey(
        Platform, related_name="VM_gap", on_delete=models.CASCADE)
    objects = models.Manager()
