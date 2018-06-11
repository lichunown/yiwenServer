## 向某人发送私信
POST `message/send/`

|  -   |  key   |     example     |    info    |
| :--: | :----: | :-------------: | :--------: |
|  *   | token  |       "1"       | 用户登录的token |
|  *   | toname |   tousername    |   发送的用户名   |
|  *   | action |     "send"      |    固定值     |
|  *   |  data  | "sdfcsedfsdefs" |     数据     |

## 获取私信列表
POST `message/send/`

|  -   |  key   | example |    info    |
| :--: | :----: | :-----: | :--------: |
|  *   | token  |   "1"   | 用户登录的token |
|  *   | action | "list"  |    固定值     |
```python
{"action": "cleanmessage", 
"data": ["qwe"], 
"result": "succeed"}
```

## 获取某人发送的私信
POST `message/get/`

|  -   |  key   | example  |    info    |
| :--: | :----: | :------: | :--------: |
|  *   | token  |   "1"    | 用户登录的token |
|  *   | froms  | username |   接收的用户名   |
|      | action |  "get"   |    固定值     |

```python
{
"action": "getmessage", 

"data": [
  [
    [[2018, 6, 11, 21, 43, 36, 0, 162, 0], "adadswggf"], 
    [[2018, 6, 11, 21, 43, 37, 0, 162, 0], "adadswggf"], 
    [[2018, 6, 11, 21, 43, 37, 0, 162, 0], "adadswggf"]
  ], 
  [
    [[2018, 6, 11, 21, 43, 36, 0, 162, 0], "adadswggf"], 
    [[2018, 6, 11, 21, 43, 37, 0, 162, 0], "adadswggf"], 
    [[2018, 6, 11, 21, 43, 37, 0, 162, 0], "adadswggf"]
  ]
], 

"result": "succeed"
}
```

```python
{
"action": "getmessage", 
"data": 
  {
    "qwe": [
      [[2018, 6, 11, 21, 43, 36, 0, 162, 0], "adadswggf"], 
      [[2018, 6, 11, 21, 43, 37, 0, 162, 0], "adadswggf"], 
      [[2018, 6, 11, 21, 43, 37, 0, 162, 0], "adadswggf"]
    ]
  }, 
"result": "succeed"}
```

### error

- actionNotExist :
  action不存在，只能为“list”，“get”，“send”，“clean”

- TokenDoNotMatch：
  用户登录的token有问题