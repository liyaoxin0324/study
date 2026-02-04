districts = {
    "name": "中国",
    "code": 86,
    "subs": [
        {"name": "北京", "code": 110},
        {"name": "天津", "code": 120},
        {"name": "河北", "code": 130, "subs": [
             {"name": "石家庄", "code": 1301},
             {"name": "唐山", "code": 1302},
             {"name": "秦皇岛", "code": 1303},
             {"name": "邯郸", "code": 1304},
             {"name": "邢台", "code": 1305},
             {"name": "保定", "code": 1306},
             {"name": "张家口", "code": 1307},
             {"name": "承德", "code": 1308},
             {"name": "沧州", "code": 1309, "subs": [
                  {"name": "新华区", "code": 130901},
                  {"name": "运河区", "code": 130902},
                  {"name": "泊头市", "code": 130903},
                  {"name": "黄骅市", "code": 130904},
                  {"name": "沧县", "code": 130905},
                  {"name": "青县", "code": 130906},
                  {"name": "沧县", "code": 130907},
                  {"name": "东光县", "code": 130908},
                  {"name": "肃宁县", "code": 130909},
                  {"name": "吴桥县", "code": 130910},
                  {"name": "献县", "code": 130911}
              ]}
          ]}
    ]}




def find_name_code(district,target_code):
    if district["code"] == target_code:
        return district["name"]
    if "subs" in district:
        for sub in district["subs"]:
            result = find_name_code(sub,target_code)
            if result:
                return result
    return None

target_code = int(input("请输入您想要查找的地区编码："))
name = find_name_code(districts,target_code)
if name:
    print(f"code{target_code}，对应名称是：{name}")
else:
    print(f"未找到code{target_code}对应的地区")



