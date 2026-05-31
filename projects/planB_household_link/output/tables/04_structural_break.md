# Plan B — Stage 04 structural-break diagnostics

Chow F-statistics for a single break at the indicated year on national weighted time-series (linear trend baseline). F-statistic critical values (5%): for `df_den ≈ 10` and `df_num = 2`, F_crit ≈ 4.10. Values above the critical threshold suggest a structural break.

| series        |   break_year |      F |   df_num |   df_den |
|:--------------|-------------:|-------:|---------:|---------:|
| shannon_actor |         2013 |  0.722 |        2 |       10 |
| shannon_actor |         2016 |  5.893 |        2 |       10 |
| shannon_actor |         2020 | 15.905 |        2 |       10 |
| central_share |         2013 |  1.513 |        2 |       10 |
| central_share |         2016 |  2.962 |        2 |       10 |
| central_share |         2020 |  4.602 |        2 |       10 |
| log_events    |         2013 |  2.01  |        2 |       10 |
| log_events    |         2016 |  0.136 |        2 |       10 |
| log_events    |         2020 |  0.04  |        2 |       10 |

## National time-series (weighted by event count)

|   data_year |   shannon_actor |   central_share |   local_share |   social_share |   soe_finance_share |   university_share |   log_events |
|------------:|----------------:|----------------:|--------------:|---------------:|--------------------:|-------------------:|-------------:|
|        2009 |           1.267 |           0.446 |         0.092 |          0.169 |               0.215 |              0.015 |        4.19  |
|        2010 |           1.269 |           0.264 |         0.379 |          0.126 |               0.172 |              0.008 |        6.261 |
|        2011 |           1.315 |           0.315 |         0.199 |          0.27  |               0.176 |              0     |        5.866 |
|        2012 |           1.268 |           0.317 |         0.266 |          0.173 |               0.209 |              0     |        6.035 |
|        2013 |           1.307 |           0.35  |         0.151 |          0.095 |               0.215 |              0.127 |        5.935 |
|        2014 |           1.51  |           0.145 |         0.221 |          0.141 |               0.257 |              0.107 |        6.43  |
|        2015 |           1.433 |           0.226 |         0.255 |          0.088 |               0.21  |              0.162 |        5.932 |
|        2016 |           1.741 |           0.224 |         0.22  |          0.176 |               0.147 |              0.074 |        6.532 |
|        2017 |           1.658 |           0.228 |         0.154 |          0.143 |               0.252 |              0.09  |        6.498 |
|        2018 |           1.648 |           0.196 |         0.126 |          0.122 |               0.284 |              0.186 |        6.667 |
|        2019 |           1.698 |           0.246 |         0.127 |          0.083 |               0.286 |              0.174 |        6.886 |
|        2020 |           1.776 |           0.198 |         0.131 |          0.094 |               0.233 |              0.228 |        7.116 |
|        2021 |           1.689 |           0.192 |         0.146 |          0.094 |               0.226 |              0.239 |        7.212 |
|        2022 |           1.195 |           0.417 |         0.041 |          0.086 |               0.202 |              0.254 |        7.267 |
