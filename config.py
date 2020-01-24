
class DefaultConfig(object):

    spiderTool = 'ACLSeries'
    Keywords= ['emotion detect conversation','emotion detect dialog','emotion recognition conversation','emotion recognition dialog']  # 关键词列表
    Years = [2016,2017,2018,2019]
    Field = '对话情感分析'
    Meeting = 'NAACL'
    path = '/Users/apple/PycharmProjects/NLPPapersSpider/'

def parse(self, kwargs):
    '''
    根据字典kwargs 更新 默认的config参数
    '''
    # 更新配置参数
    for k, v in kwargs.items():
        if not hasattr(self, k):
            # 警告还是报错，取决个人喜好
            warnings.warn("Warning: opt has not attribut %s" % k)
        setattr(self, k, v)

    # 打印配置信息
    print('user config:')
    for k, v in self.__class__.__dict__.items():  # python3 中iteritems()已经废除了
        if not k.startswith('__'):
            print(k, getattr(self, k))


DefaultConfig.parse = parse
opt = DefaultConfig()
