#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.BaijiaCMS import BaijiaCMSPathLeakVulnerability
from ClassCongregation import Prompt

def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(BaijiaCMSPathLeakVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("BaijiaCMS")