import json
import os

def clean_question_text(q_str):
    # Try splitting by common markers of option blocks
    markers = ["\nA.\n", "\nA. ", "\nA.\r\n", "\nA .", "\nA."]
    for marker in markers:
        if marker in q_str:
            return q_str.split(marker)[0].strip()
    return q_str

def main():
    enhanced_path = "src/data/questions_enhanced.json"
    enriched_path = "scripts/output/enriched_questions.json"
    checkpoint_path = "scripts/output/enrichment_checkpoint.json"
    
    # 1. Prepare Ground Truth for Q36
    q36_options = [
        {"key": "A", "text": "public abstract class ShippingCalculator {\n  public abstract calculate() {/* implementation */ }\n}"},
        {"key": "B", "text": "public abstract class ShippingCalculator {\n  public void calculate() {/* implementation */ }\n}"},
        {"key": "C", "text": "public abstract class ShippingCalculator {\n  public virtual void calculate() {/* implementation */ }\n}"},
        {"key": "D", "text": "public abstract class ShippingCalculator {\n  public override calculate() {/* implementation */ }\n}"}
    ]
    q36_correct = ["C"]
    q36_explanation = {
        "vi_question": "Lập trình viên cần tạo class ShippingCalculator không được phép khởi tạo trực tiếp (cannot be instantiated) nhưng phải chứa một phương thức calculate có sẵn mã xử lý mặc định để các class con có thể ghi đè (override). Khai báo nào sau đây là đúng?",
        "why_correct": "Để class không được khởi tạo trực tiếp, ta dùng từ khóa 'abstract class'. Để phương thức có code mặc định và cho phép class con ghi đè, ta dùng từ khóa 'public virtual void calculate() ...' (tương ứng với đáp án C).",
        "why_wrong": {
            "A": "Phương thức calculate() khai báo abstract thì không được phép định nghĩa body (phần thân hàm có chứa code mặc định) trong Apex.",
            "B": "Thiếu từ khóa 'virtual' ở phương thức calculate() khiến lớp con không thể sử dụng từ khóa 'override' để ghi đè.",
            "D": "Từ khóa 'override' chỉ dùng khi lớp con muốn ghi đè phương thức từ lớp cha, không thể dùng ở lớp cha để khai báo ban đầu."
        },
        "tip": "Không cho new trực tiếp -> abstract class. Cho phép ghi đè + có code mặc định -> virtual method."
    }

    # 2. Prepare Ground Truth for Q72
    q72_options = [
        {"key": "A", "text": "webservice class WebServiceClass {\n  private Boolean helperMethod() { /*implementation ...*/ }\n  global static String updateRecords() { /*implementation ...*/ }\n}"},
        {"key": "B", "text": "global class WebServiceClass {\n  private Boolean helperMethod() { /*implementation ...*/ }\n  webservice static String updateRecords() { /*implementation ...*/ }\n}"},
        {"key": "C", "text": "webservice class WebServiceClass {\n  private Boolean helperMethod() { /*implementation ...*/ }\n  webservice static String updateRecords() { /*implementation ...*/ }\n}"},
        {"key": "D", "text": "global class WebServiceClass {\n  private Boolean helperMethod() { /*implementation ...*/ }\n  global String updateRecords() { /*implementation ...*/ }\n}"}
    ]
    q72_correct = ["B"]
    q72_explanation = {
        "vi_question": "Developer cần tạo một custom SOAP Web Service để ứng dụng web bên ngoài gọi vào. Lập trình viên muốn viết thêm các phương thức helper nội bộ không dùng cho bên ngoài. Khai báo class và method nào sau đây là đúng chuẩn?",
        "why_correct": "Bất kỳ class nào chứa phương thức khai báo từ khóa 'webservice' đều BẮT BUỘC phải là global class (để bên ngoài có thể truy cập). Phương thức API phơi ra cho bên ngoài gọi qua SOAP bắt buộc phải dùng từ khóa 'webservice static'. Các phương thức helper nội bộ không muốn lộ ra ngoài thì cứ khai báo 'private' bình thường. Do đó khai báo B là chuẩn nhất.",
        "why_wrong": {
            "A": "Cú pháp 'webservice class' là sai bét, Apex không cho phép dùng từ khóa webservice cho phần định nghĩa class.",
            "C": "Tương tự A, sai cú pháp khai báo class với 'webservice class'.",
            "D": "Thiếu từ khóa 'webservice' và 'static' trên phương thức updateRecords(), làm cho hệ thống bên ngoài không thể nhận diện và gọi qua SOAP."
        },
        "tip": "Quy tắc vàng SOAP trong Apex: Class bắt buộc GLOBAL, Method bắt buộc WEBSERVICE STATIC."
    }

    # 3. Prepare Ground Truth for Q165
    q165_options = [
        {"key": "A", "text": "public class CreditCardPayment extends Payment {\n  public virtual void makePayment(Decimal amount) { /*implementation*/ }\n}"},
        {"key": "B", "text": "public class CreditCardPayment extends Payment {\n  public override void makePayment(Decimal amount) { /*implementation*/ }\n}"},
        {"key": "C", "text": "public class CreditCardPayment implements Payment {\n  public virtual void makePayment(Decimal amount) { /*implementation*/ }\n}"},
        {"key": "D", "text": "public class CreditCardPayment implements Payment {\n  public override void makePayment(Decimal amount) { /*implementation*/ }\n}"}
    ]
    q165_correct = ["B"]
    q165_explanation = {
        "vi_question": "Developer cần tạo class CreditCardPayment kế thừa từ class Payment ảo có sẵn: [Payment Class]. Khai báo nào sau đây là đúng cú pháp?",
        "why_correct": "Vì lớp cha Payment là một class ảo thông thường được khai báo với từ khóa virtual, nên class con muốn kế thừa bắt buộc phải dùng từ khóa extends. Đồng thời, để ghi đè (chỉnh sửa lại logic) của phương thức ảo makePayment(), class con bắt buộc phải dùng từ khóa override (B).",
        "why_wrong": {
            "A": "Sử dụng từ khóa virtual ở class con thay vì override khi muốn ghi đè phương thức lớp cha là sai cú pháp.",
            "C": "Từ khóa implements chỉ dành cho interface, không dùng để kế thừa một virtual class thông thường. Ngoài ra cũng sai từ khóa ghi đè.",
            "D": "Sử dụng sai từ khóa implements thay vị extends để kế thừa class."
        },
        "tip": "Kế thừa Class -> Dùng EXTENDS + OVERRIDE. Hiện thực hóa Interface -> Dùng IMPLEMENTS."
    }

    ids_to_clean_q = [36, 40, 72, 74, 165, 168, 231, 236, 240, 290, 343]

    # Process lists (enhanced and enriched)
    for path in [enhanced_path, enriched_path]:
        if not os.path.exists(path):
            print(f"Skipping {path} (not found)")
            continue
        with open(path, "r", encoding="utf-8") as f:
            questions = json.load(f)
            
        for q in questions:
            qid = q["id"]
            if qid in ids_to_clean_q:
                old_q = q["question"]
                q["question"] = clean_question_text(old_q)
                if old_q != q["question"]:
                    print(f"Cleaned question field for ID {qid} in {path}")
                    
            if qid == 36:
                q["options"] = q36_options
                q["correct"] = q36_correct
                q["explanation"] = q36_explanation
                print(f"Updated options, correct and explanation for ID 36 in {path}")
            elif qid == 72:
                q["options"] = q72_options
                q["correct"] = q72_correct
                q["explanation"] = q72_explanation
                print(f"Updated options, correct and explanation for ID 72 in {path}")
            elif qid == 165:
                q["options"] = q165_options
                q["correct"] = q165_correct
                q["explanation"] = q165_explanation
                print(f"Updated options, correct and explanation for ID 165 in {path}")
                
        with open(path, "w", encoding="utf-8") as f:
            json.dump(questions, f, ensure_ascii=False, indent=2)
        print(f"Successfully saved {path}")

    # Process checkpoint dict
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path, "r", encoding="utf-8") as f:
            checkpoint = json.load(f)
            
        # Update explanation keys
        for str_id, data_ex in checkpoint.items():
            qid = data_ex.get("id")
            if qid is None:
                continue
                
            if qid == 36:
                checkpoint[str_id] = {"id": 36, **q36_explanation}
                print("Updated Q36 in checkpoint")
            elif qid == 72:
                checkpoint[str_id] = {"id": 72, **q72_explanation}
                print("Updated Q72 in checkpoint")
            elif qid == 165:
                checkpoint[str_id] = {"id": 165, **q165_explanation}
                print("Updated Q165 in checkpoint")
                
        with open(checkpoint_path, "w", encoding="utf-8") as f:
            json.dump(checkpoint, f, ensure_ascii=False, indent=2)
        print(f"Successfully saved {checkpoint_path}")

if __name__ == "__main__":
    main()
