# **docker-compose启动**
## **gpu版本**
docker-compose -f docker-compose-gpu.yml up -d
## **cpu版本**
docker-compose -f docker-compose-cpu.yml up -d

# **request**
```
{
    "query_list": [
    {
        "uuid": "1",
        "raw_code": "68.23002",
        "raw_name": "小腿脓肿切开引流术"
    },
    {
      "uuid": "2",
      "raw_code": "60.29002",
      "raw_name": "白线疝修补术"
    },
    {
      "uuid": "3",
      "raw_code": "80.40",
      "raw_name": "髋部大关节粘连松解术"
    }
  ],
  "topk": 5,
  "version": "手术-联仁手术操作分类标准及术语集20220425"
}
```
# **response**
```
{
  "status_code": 200,
  "message": "success",
  "data": [
    {
      "uuid": "1",
      "input_text": "小腿脓肿切开引流术",
      "entity_number": 1,
      "entity_records": [
        {
          "code": "A86.0400",
          "name": "皮肤和皮下组织的其他切开术伴引流术",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 1,
          "priority": 1
        }
      ]
    },
    {
      "uuid": "2",
      "input_text": "白线疝修补术",
      "entity_number": 4,
      "entity_records": [
        {
          "code": "53.5900x001",
          "name": "腹壁白线疝修补术",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 0.661,
          "priority": 1
        },
        {
          "code": "53.9x06",
          "name": "网膜疝修补术",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 0.482,
          "priority": 2
        },
        {
          "code": "46.7602",
          "name": "盲肠瘘修补术",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 0.365,
          "priority": 3
        },
        {
          "code": "99.8301",
          "name": "新生儿蓝光治疗",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 0.128,
          "priority": 4
        }
      ]
    },
    {
      "uuid": "3",
      "input_text": "髋部大关节粘连松解术",
      "entity_number": 4,
      "entity_records": [
        {
          "code": "93.2600x002",
          "name": "大关节粘连手法松解术",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 0.648,
          "priority": 1
        },
        {
          "code": "71.0100x003",
          "name": "大阴唇粘连松解术",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 0.51,
          "priority": 2
        },
        {
          "code": "02.9100",
          "name": "大脑皮层粘连松解术",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 0.473,
          "priority": 3
        },
        {
          "code": "45.0300",
          "name": "大肠切开术",
          "label": "手术",
          "version": "手术-联仁手术操作分类标准及术语集20220425",
          "score": 0.254,
          "priority": 4
        }
      ]
    }
  ]
}
```




