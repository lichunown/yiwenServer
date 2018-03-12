## 向某人发送私信
POST `message/send/`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | touser | "Passage Title" |    发送的用户名    |
|  *   | data  | "lalalalalala。" |    数据    |

## 获取私信列表
POST `message/list/`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |


## 获取某人发送的私信
POST `message/get/`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | fromuser | "Passage Title" |    接收的用户名    |
|  *   | nums  | [1,2,3,4] |    标识    |