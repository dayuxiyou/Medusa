#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability
from Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability2
from Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability3
from Cms.ThinkPHP import ThinkPHPSqlInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(ThinkPHPArbitraryCommandExecutionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(ThinkPHPArbitraryCommandExecutionVulnerability2.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(ThinkPHPArbitraryCommandExecutionVulnerability3.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(ThinkPHPSqlInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("ThinkPHP")