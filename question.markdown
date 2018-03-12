## 查看提问

GET `question/`

|  -   |  key  |     example      |    info    |
| :--: | :---: | :--------------: | :--------: |
|      | token |       "1"        | 用户登录的token |
|  *   | title | "question Title" |    提问标题    |


## 创建提问

POST `question/add`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | title | "Passage Title" |    提问标题    |
|  *   | body  | "lalalalalala。" |    提问内容    |

## 修改提问

POST `question/modify`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | title | "Passage Title" |    提问标题    |
|  *   | body  | "lalalalalala。" |    提问内容    |

## 删除提问

POST `question/delete`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | title | "Passage Title" |    文章标题    |

## 获取回答

POST `question/answer/`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | title | "Passage Title" |    提问标题    |
|  *   | nums  |   [1,2,3,4,5]   |   回答标号列表   |

## 回答

POST `question/answer/add`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | title | "Passage Title" |    提问标题    |
|  *   | body  | "lalalalalala。" |    提问内容    |


## 修改回答
POST `question/answer/modify`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | title | "Passage Title" |    提问标题    |
|  *   | body  | "lalalalalala。" |    提问内容    |
|  *   | id  | "lalalalalala。" |    回答id    |

## 删除回答

POST `question/answer/delete`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | title | "Passage Title" |    提问标题    |
|  *   | id  | "lalalalalala。" |    回答id    |

## 回答下评论

POST `question/answer/comment/add`

## 删除回答下评论

POST `question/answer/comment/delete`

## 回答点赞
POST `question/answer/support`
## 关注问题
POST `question/focus`

