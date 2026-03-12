import json
import os
from openai import OpenAI


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    ai_input = load_json("ai_input.json")

    # まずは先頭3件だけで試す
    sample_input = ai_input[:3]

    prompt = f"""
あなたは業務システムのテスト設計者です。
入力された画面項目定義とテスト観点から、画面テストケースを作成してください。

出力ルール:
- 出力は必ずJSON配列
- 1項目につき、必要な観点ごとに複数ケースを作成する
- 同じ意味の重複ケースは作らない
- 不明な仕様は expected_result に「要確認」と明記する
- expected_result は具体的に書く

各テストケースの項目:
- case_id
- section
- item_name
- test_point
- test_purpose
- precondition
- input_value
- operation
- expected_result
- priority

入力データ:
{json.dumps(sample_input, ensure_ascii=False, indent=2)}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    result_text = response.output_text

    with open("testcases_raw.json", "w", encoding="utf-8") as f:
        f.write(result_text)

    print("testcases_raw.json を作成しました")
    print(result_text)


if __name__ == "__main__":
    main()