import time

from tqdm import tqdm

from runnable.fast_embed_runnable import FastEmbedRunnable


def test_fast_embed_runnable_performance():
    runnable = FastEmbedRunnable()
    test_content = """
        如果今夜月光是温凉
        星星闪烁着坠入了眼眶
        那么 我们会怎样
        会不会有勇气摊开手掌
        小小雏菊的香
        你笑着称赞过我的眉目舒朗
        我抱吉他给你把老歌唱一唱
        生活年月几分 秒秒钟沉沦
        所有细碎的话都很诚恳
        我恋慕春天的晚风
        夏天耳畔响起蝉声
        秋天金黄的时辰
        雪花飞上来
        模糊了暮色里你的眼神
        比最轻的晚风还动人
        还没听过鲸鱼和海的和声
        记得你说那远方的山峦 有雪的吻痕
        世界几米方寸 万万里飞奔
        藏满了我能够想象到的永恒
        我恋慕春天的晚风
        夏天耳畔响起蝉声
        秋天金黄的时辰
        雪花无声飞上来
        模糊了暮色里你的眼神
        比最轻的晚风还动人
        如果今夜月光是温凉
        星星闪烁着坠入了眼眶
        我会小心翼翼地摊开手掌
        有那一朵小雏菊静躺 带着香
    """
    for _ in tqdm(range(1000)):
        runnable.execute(test_content)
