
import pandas as pd

# ファイル読み込み
design = pd.read_excel("design_items.xlsx")
rules = pd.read_excel("rule_definition.xlsx", sheet_name="項目テスト-新規-")
points = pd.read_excel("rule_definition.xlsx", sheet_name="テスト観点定義")

# テンプレート
template = pd.read_excel("test_template.xlsx", sheet_name="項目テスト-新規-")

result = []

for _, item in design.iterrows():

    section = item["section"]
    name = item["item_name"]

    for _, rule in rules.iterrows():

        column = rule["設計書列"]
        cond_type = rule["条件タイプ"]
        cond_value = rule["条件値"]

        value = item.get(column, "")

        match = False

        if cond_type == "equals":
            match = value == cond_value

        elif cond_type == "contains":
            match = cond_value in str(value)

        elif cond_type == "mapping":
            match = cond_value in str(value)

        elif cond_type == "numeric":
            match = str(value).isdigit()

        elif cond_type == "bracket_numeric":
            match = str(value).startswith("(")

        elif cond_type == "regex":
            import re
            match = bool(re.search(cond_value, str(value)))

        if not match:
            continue

        point = rule["観点ID"]

        if pd.isna(point):
            continue

        row = points[points["観点ID"] == point].iloc[0]

        result.append({
            "場所": section,
            "項目名": name,
            "テスト要否": 1,
            "テスト区分": row["テスト区分"],
            "テスト内容": row["テスト内容テンプレート"],
            "期待値": ""
        })

df = pd.DataFrame(result)

df.to_excel("generated_test_spec.xlsx", index=False)

print("テスト仕様書を生成しました")
