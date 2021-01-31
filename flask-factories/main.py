# 工廠模式 create_app() 建立app，再返回app物件
# 可以根據環境，進行設定檔配置
from app import create_app

# app = create_app('dev')
app = create_app('test')