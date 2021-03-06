y_list_ml = ['流动资产',
             '流动资产/货币资金',
             '流动资产/结算备付金',
             '流动资产/拆出资金',
             '流动资产/交易性金融资产',
             '流动资产/衍生金融资产',
             '流动资产/应收票据',
             '流动资产/应收账款',
             '流动资产/应收款项融资',
             '流动资产/预付款项',
             '流动资产/应收保费',
             '流动资产/应收分保账款',
             '流动资产/应收分保合同准备金',
             '流动资产/其他应收款',
             '流动资产/其他应收款/应收利息',
             '流动资产/其他应收款/应收股利',
             '流动资产/其他应收款/买入返售金融资产',
             '流动资产/其他应收款/存货',
             '流动资产/其他应收款/合同资产',
             '流动资产/其他应收款/持有待售资产',
             '流动资产/其他应收款/一年内到期的非流动资产',
             '流动资产/其他应收款/其他流动资产',
             '流动资产合计',
             '非流动资产',
             '非流动资产/发放贷款和垫款',
             '非流动资产/债权投资',
             '非流动资产/其他债权投资',
             '非流动资产/长期应收款',
             '非流动资产/长期股权投资',
             '非流动资产/其他权益工具投资'
             '非流动资产/其他非流动金融资产',
             '非流动资产/投资性房地产',
             '非流动资产/固定资产',
             '非流动资产/在建工程',
             '非流动资产/生产性生物资产',
             '非流动资产/油气资产',
             '非流动资产/使用权资产',
             '非流动资产/无形资产',
             '非流动资产/开发支出',
             '非流动资产/商誉',
             '非流动资产/长期待摊费用',
             '非流动资产/递延所得税资产',
             '非流动资产/其他非流动资产',
             '非流动资产合计',
             '资产总计',
             '流动负债',
             '流动负债/短期借款',
             '流动负债/向中央银行借款',
             '流动负债/拆入资金',
             '流动负债/交易性金融负债',
             '流动负债/衍生金融负债',
             '流动负债/应付票据',
             '流动负债/应付账款',
             '流动负债/预收款项',
             '流动负债/合同负债',
             '流动负债/卖出回购金融资产款',
             '流动负债/吸收存款及同业存放',
             '流动负债/代理买卖证券款',
             '流动负债/代理承销证券款'
             '流动负债/应付职工薪酬',
             '流动负债/应交税费',
             '流动负债/其他应付款',
             '流动负债/其他应付款/应付利息',
             '流动负债/其他应付款/应付股利',
             '流动负债/应付手续费及佣金',
             '流动负债/应付分保账款',
             '流动负债/持有待售负债',
             '流动负债/一年内到期的非流动负债',
             '流动负债/其他流动负债',
             '流动负债合计',
             '非流动负债',
             '非流动负债/保险合同准备金',
             '非流动负债/长期借款',
             '非流动负债/应付债券',
             '非流动负债/应付债券/优先股',
             '非流动负债/应付债券/永续债',
             '非流动负债/租赁负债',
             '非流动负债/长期应付款',
             '非流动负债/长期应付职工薪酬',
             '非流动负债/预计负债',
             '非流动负债/递延收益',
             '非流动负债/递延所得税负债',
             '非流动负债/其他非流动负债',
             '非流动负债合计',
             '负债合计',
             '所有者权益',
             '所有者权益/股本',
             '所有者权益/其他权益工具',
             '所有者权益/其他权益工具/优先股',
             '所有者权益/其他权益工具/优永续债',
             '所有者权益/资本公积',
             '所有者权益/库存股',
             '所有者权益/其他综合收益',
             '所有者权益/专项储备',
             '所有者权益/盈余公积',
             '所有者权益/一般风险准备',
             '所有者权益/未分配利润',
             '归属于母公司所有者权益合计',
             '少数股东权益',
             '所有者权益合计',
             '负债和所有者权益总计'
             ]

y_list_pf = ['营业总收入',
             '营业总收入/营业收入',
             '营业总收入/利息收入',
             '营业总收入/已赚保费',
             '营业总收入/手续费及佣金收入',
             '营业总成本',
             '营业总成本/营业成本',
             '营业总成本/利息支出',
             '营业总成本/手续费及佣金支出',
             '营业总成本/退保金',
             '营业总成本/赔付支出净额',
             '营业总成本/提取保险责任合同准备金净额',
             '营业总成本/保单红利支出',
             '营业总成本/分保费用',
             '营业总成本/税金及附加',
             '营业总成本/销售费用',
             '营业总成本/管理费用',
             '营业总成本/研发费用',
             '营业总成本/财务费用',
             '营业总成本/财务费用/利息费用',
             '营业总成本/财务费用/利息收入',
             '营业总成本/其他收益',
             '营业总成本/投资收益',
             '营业总成本/对联营企业和合营企业的投资收益',
             '营业总成本/以摊余成本计量的金融资产终止确认收益',
             '营业总成本/汇兑收益',
             '营业总成本/净敞口套期收益',
             '营业总成本/公允价值变动收益',
             '营业总成本/信用减值损失',
             '营业总成本/资产减值损失',
             '营业总成本/资产处置收益',
             '营业利润',
             '营业利润/营业外收入',
             '营业利润/营业外支出',
             '利润总额',
             '利润总额/所得税费用',
             '净利润',
             '净利润/按经营持续性分类',
             '净利润/按经营持续性分类/持续经营净利润',
             '净利润/按经营持续性分类/终止经营净利润',
             '净利润/按所有权归属分类',
             '净利润/按所有权归属分类/归属于母公司股东的净利润',
             '净利润/按所有权归属分类/少数股东损益',
             '其他综合收益的税后净额',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/不能重分类进损益的其他综合收益',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/不能重分类进损益的其他综合收益/重新计量设定受益计划变动额',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/不能重分类进损益的其他综合收益/权益法下不能转损益的其他综合收益',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/不能重分类进损益的其他综合收益/其他权益工具投资公允价值变动',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/不能重分类进损益的其他综合收益/企业自身信用风险公允价值变动',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/不能重分类进损益的其他综合收益/其他',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/将重分类进损益的其他综合收益',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/将重分类进损益的其他综合收益/权益法下可转损益的其他综合收益',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/将重分类进损益的其他综合收益/其他债权投资公允价值变动',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/将重分类进损益的其他综合收益/金融资产重分类计入其他综合收益的金额',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/将重分类进损益的其他综合收益/其他债权投资信用减值准备',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/将重分类进损益的其他综合收益/现金流量套期储备',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/将重分类进损益的其他综合收益/外币财务报表折算差额',
             '其他综合收益的税后净额/归属母公司所有者的其他综合收益的税后净额/将重分类进损益的其他综合收益/其他',
             '其他综合收益的税后净额/归属于少数股东的其他综合收益的税后净额,',
             '综合收益总额',
             '综合收益总额/归属于母公司所有者的综合收益总额',
             '综合收益总额/归属于少数股东的综合收益总额',
             '每股收益',
             '每股收益/基本每股收益',
             '每股收益/稀释每股收益']

y_list_kb = [
    '经营活动产生的现金流量',
    '经营活动产生的现金流量/销售商品、提供劳务收到的现金',
    '经营活动产生的现金流量/客户存款和同业存放款项净增加额',
    '经营活动产生的现金流量/向中央银行借款净增加额',
    '经营活动产生的现金流量/向其他金融机构拆入资金净增加额',
    '经营活动产生的现金流量/收到原保险合同保费取得的现金',
    '经营活动产生的现金流量/收到再保业务现金净额',
    '经营活动产生的现金流量/保户储金及投资款净增加额',
    '经营活动产生的现金流量/收取利息、手续费及佣金的现金',
    '经营活动产生的现金流量/拆入资金净增加额',
    '经营活动产生的现金流量/回购业务资金净增加额',
    '经营活动产生的现金流量/代理买卖证券收到的现金净额',
    '经营活动产生的现金流量/收到的税费返还',
    '经营活动产生的现金流量/收到其他与经营活动有关的现金',
    '经营活动产生的现金流量/经营活动现金流入小计',
    '经营活动产生的现金流量/购买商品、接受劳务支付的现金',
    '经营活动产生的现金流量/客户贷款及垫款净增加额',
    '经营活动产生的现金流量/存放中央银行和同业款项净增加额',
    '经营活动产生的现金流量/支付原保险合同赔付款项的现金',
    '经营活动产生的现金流量/拆出资金净增加额',
    '经营活动产生的现金流量/支付利息、手续费及佣金的现金',
    '经营活动产生的现金流量/支付保单红利的现金',
    '经营活动产生的现金流量/支付给职工以及为职工支付的现金',
    '经营活动产生的现金流量/支付的各项税费',
    '经营活动产生的现金流量/支付其他与经营活动有关的现金',
    '经营活动产生的现金流量/经营活动现金流出小计',
    '经营活动产生的现金流量/经营活动产生的现金流量净额',
    '投资活动产生的现金流量',
    '投资活动产生的现金流量/收回投资收到的现金',
    '投资活动产生的现金流量/取得投资收益收到的现金',
    '投资活动产生的现金流量/处置固定资产、无形资产和其他长期资产收回的现金净额',
    '投资活动产生的现金流量/处置子公司及其他营业单位收到的现金净额',
    '投资活动产生的现金流量/收到其他与投资活动有关的现金',
    '投资活动产生的现金流量/投资活动现金流入小计',
    '投资活动产生的现金流量/购建固定资产、无形资产和其他长期资产支付的现金',
    '投资活动产生的现金流量/投资支付的现金',
    '投资活动产生的现金流量/质押贷款净增加额',
    '投资活动产生的现金流量/取得子公司及其他营业单位支付的现金净额',
    '投资活动产生的现金流量/支付其他与投资活动有关的现金',
    '投资活动产生的现金流量/投资活动现金流出小计',
    '投资活动产生的现金流量/投资活动产生的现金流量净额',
    '筹资活动产生的现金流量',
    '筹资活动产生的现金流量/吸收投资收到的现金',
    '筹资活动产生的现金流量/子公司吸收少数股东投资收到的现金',
    '筹资活动产生的现金流量/取得借款收到的现金',
    '筹资活动产生的现金流量/收到其他与筹资活动有关的现金',
    '筹资活动产生的现金流量/筹资活动现金流入小计',
    '筹资活动产生的现金流量/偿还债务支付的现金',
    '筹资活动产生的现金流量/分配股利、利润或偿付利息支付的现金',
    '筹资活动产生的现金流量/子公司支付给少数股东的股利、利润',
    '筹资活动产生的现金流量/支付其他与筹资活动有关的现金',
    '筹资活动产生的现金流量/筹资活动现金流出小计',
    '筹资活动产生的现金流量/筹资活动产生的现金流量净额',
    '汇率变动对现金及现金等价物的影响',
    '现金及现金等价物净增加额',
    '期初现金及现金等价物余额',
    '期末现金及现金等价物余额',
]

y_list_mlr = [
    '营业收入',
    '营业收入/营业成本',
    '营业收入/税金及附加',
    '营业收入/销售费用',
    '营业收入/管理费用',
    '营业收入/研发费用',
    '营业收入/财务费用',
    '营业收入/利息费用',
    '营业收入/利息收入',
    '营业收入/其他收益',
    '营业收入/投资收益',
    '营业收入/对联营企业和合营企业的投资收益',
    '营业收入/以摊余成本计量的金融资产终止确认收益',
    '营业收入/净敞口套期收益',
    '营业收入/公允价值变动收益',
    '营业收入/信用减值损失',
    '营业收入/资产减值损失',
    '营业收入/资产处置收益',
    '营业利润',
    '营业利润/营业外收入',
    '营业利润/营业外支出',
    '利润总额',
    '利润总额/所得税费用',
    '净利润',
    '净利润/持续经营净利润',
    '净利润/终止经营净利润',
    '其他综合收益的税后净额',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/重新计量设定受益计划变动额',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/权益法下不能转损益的其他综合收益',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/其他权益工具投资公允价值变动',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/企业自身信用风险公允价值变动',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/其他',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/权益法下可转损益的其他综合收益',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/其他债权投资公允价值变动',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/金融资产重分类计入其他综合收益的金额',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/其他债权投资信用减值准备',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/现金流量套期储备',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/外币财务报表折算差额',
    '其他综合收益的税后净额/不能重分类进损益的其他综合收益/其他',
    '其他综合收益的税后净额/综合收益总额',
    '其他综合收益的税后净额/每股收益',
    '其他综合收益的税后净额/每股收益/基本每股收益',
    '其他综合收益的税后净额/每股收益/稀释每股收益', ]

y_list_mzf = [
    '流动资产',
    '流动资产/货币资金',
    '流动资产/交易性金融资产',
    '流动资产/衍生金融资产',
    '流动资产/应收票据',
    '流动资产/应收账款',
    '流动资产/应收款项融资',
    '流动资产/预付款项',
    '流动资产/其他应收款',
    '流动资产/应收利息',
    '流动资产/应收股利',
    '流动资产/存货',
    '流动资产/合同资产',
    '流动资产/持有待售资产',
    '流动资产/一年内到期的非流动资产',
    '流动资产/其他流动资产',
    '流动资产/流动资产合计',
    '非流动资产',
    '非流动资产/债权投资',
    '非流动资产/其他债权投资',
    '非流动资产/长期应收款',
    '非流动资产/长期股权投资',
    '非流动资产/其他权益工具投资',
    '非流动资产/其他非流动金融资产',
    '非流动资产/投资性房地产',
    '非流动资产/固定资产',
    '非流动资产/在建工程',
    '非流动资产/生产性生物资产',
    '非流动资产/油气资产',
    '非流动资产/使用权资产',
    '非流动资产/无形资产',
    '非流动资产/开发支出',
    '非流动资产/商誉',
    '非流动资产/长期待摊费用',
    '非流动资产/递延所得税资产',
    '非流动资产/其他非流动资产',
    '非流动资产/非流动资产合计',
    '非流动资产/资产总计',
    '流动负债',
    '流动负债/短期借款',
    '流动负债/交易性金融负债',
    '流动负债/衍生金融负债',
    '流动负债/应付票据',
    '流动负债/应付账款',
    '流动负债/预收款项',
    '流动负债/合同负债',
    '流动负债/应付职工薪酬',
    '流动负债/应交税费',
    '流动负债/其他应付款',
    '流动负债/应付利息',
    '流动负债/应付股利',
    '流动负债/持有待售负债',
    '流动负债/一年内到期的非流动负债',
    '流动负债/其他流动负债',
    '流动负债/流动负债合计',
    '非流动负债',
    '非流动负债/长期借款',
    '非流动负债/应付债券',
    '非流动负债/优先股',
    '非流动负债/永续债',
    '非流动负债/租赁负债',
    '非流动负债/长期应付款',
    '非流动负债/长期应付职工薪酬',
    '非流动负债/预计负债',
    '非流动负债/递延收益',
    '非流动负债/递延所得税负债',
    '非流动负债/其他非流动负债',
    '非流动负债/非流动负债合计',
    '非流动负债/负债合计',
    '所有者权益',
    '所有者权益/股本',
    '所有者权益/其他权益工具',
    '所有者权益/优先股',
    '所有者权益/永续债',
    '所有者权益/资本公积',
    '所有者权益/库存股',
    '所有者权益/其他综合收益',
    '所有者权益/专项储备',
    '所有者权益/盈余公积',
    '所有者权益/未分配利润',
    '所有者权益/所有者权益合计',
    '所有者权益/所有者权益合计'
]

fixed = [
    '账面原值',
    '账面原值/期初余额',
    '账面原值/本期增加金额',
    '账面原值/本期增加金额/购置',
    '账面原值/本期增加金额/在建工程转入',
    '账面原值/本期增加金额/企业合并增加',
    '账面原值/本期减少金额',
    '账面原值/本期减少金额/处置或报废',
    '账面原值/期末余额',
    '累计折旧',
    '累计折旧/期初余额',
    '累计折旧/本期增加金额',
    '累计折旧/本期增加金额/计提',
    '累计折旧/本期减少金额',
    '累计折旧/本期减少金额/处置或报废',
    '累计折旧/期末余额',
    '减值准备',
    '减值准备/期初余额',
    '减值准备/本期增加金额',
    '减值准备/本期增加金额/计提',
    '减值准备/本期减少金额',
    '减值准备/本期减少金额/处置或报废',
    '减值准备/期末余额',
    '账面价值',
    '账面价值/期末账面价值',
    '账面价值/期初账面价值',
]

# 无形资产-明细情况（intangible_assets_detail）

iad = [
    '账面原值',
    '账面原值/期初余额',
    '账面原值/本期增加金额',
    '账面原值/本期增加金额/购置',
    '账面原值/本期增加金额/内部研发',
    '账面原值/本期增加金额/企业合并增加',
    '账面原值/本期减少金额',
    '账面原值/本期减少金额/处置',
    '账面原值/本期减少金额/转入投资型房地产',
    '账面原值/本期减少金额/期末外币报表折算差额减少',
    '账面原值/期末余额',
    '累计摊销',
    '累计摊销/期初余额',
    '累计摊销/本期增加金额',
    '累计摊销/本期增加金额/计提',
    '累计摊销/本期增加金额/转入投资型房地产',
    '累计摊销/本期减少金额',
    '累计摊销/本期减少金额/处置',
    '累计摊销/本期减少金额/转入投资型房地产',
    '累计摊销/期末余额',
    '减值准备',
    '减值准备/期初余额',
    '减值准备/本期增加金额',
    '减值准备/本期增加金额/计提',
    '减值准备/本期减少金额',
    '减值准备/本期减少金额/处置',
    '减值准备/期末余额',
    '账面价值',
    '账面价值/期末账面价值',
    '账面价值/期初账面价值'
]
