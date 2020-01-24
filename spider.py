from config import opt
import spidersMoudle


def spider(**kwargs):
    # 根据命令行参数更新配置 否则使用默认配置
    opt.parse(kwargs)

    spiderTool = getattr(spidersMoudle, opt.spiderTool)(opt)

    spiderTool.main()


if __name__ == '__main__':
    import fire
    fire.Fire()

