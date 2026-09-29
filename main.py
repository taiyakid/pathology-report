print("=== Pathology Report ===")

# 基本情報
patient_id = input("患者ID: ")
organ = input("臓器: ")
specimen = input("検体: ")

# 臨床情報
clinical_info = input("臨床情報: ")

# 病理診断
diagnosis = input("病理診断: ")

# 免疫染色
ihc = input("免疫染色: ")

# コメント
comment = input("コメント: ")

# 病理診断書を作成
report = f"""
======================
      病理診断書
======================

【　患者ID　】
{patient_id}

【　臓器　】
{organ}

【　検体　】
{specimen}

【　臨床情報　】
{clinical_info}

【　病理診断　】
{diagnosis}.

【　免疫染色　】
{ihc}

【　コメント　】
{comment}

======================
"""

print(report)