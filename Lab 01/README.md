# **Bài tập Lý thuyết LAB 01**
**Câu 1 và 2 dựa và Đồ thị mẫu 2 và Đồ thị mẫu 5**

Câu 1:
-  BFS duyệt theo từng lớp, nên sẽ tìm được đường đi có ít cạnh nhất trên đồ thị không trọng số.
Trên đồ thị có trọng số, BFS không xét đến chi phí, nên có thể chọn đường đi có nhiều trọng số hơn.
-  Ví dụ từ Đồ thị mẫu 5:
BFS chọn S -> B -> G có tổng trọng số là 7, nhưng S -> A -> G có tổng trọng số là 4 lại tốt hơn -> BFS sai trong đồ thị có trọng số.

Câu 2:
-  Cả BFS và DFS cần sử dụng tập các đỉnh đã thăm (visited) để không duyệt lại đỉnh cũ.
-  Điều này giúp tránh đi vào chu trình vô tận, đặc biệt trong đồ thị có vòng.
Ví dụ từ Đồ thị mẫu 2:

Nếu không đánh dấu, DFS có thể lặp: A -> B -> D -> C -> A -> ...
=> Gây vòng lặp vô hạn nếu không kiểm soát.

**Câu 1 và 2 dựa vào Đồ thị mẫu 6 và 7**

Câu 1:
-  BFS duyệt theo số lượng bước đi, không xét trọng số của cạnh → không đảm bảo tổng trọng số nhỏ nhất.
-  DFS duyệt theo chiều sâu tuỳ ý → cũng không xét trọng số.
-  Cả hai chỉ quan tâm đến cấu trúc chứ không quan tâm đến chi phí.
Ví dụ từ Đồ thị mẫu 6:
-  Đường S -> A -> D -> E -> H có tổng trọng số: 2 + 4 + 8 + 10 = 24
-  Nhưng nếu BFS đi theo S → C → D → E → H thì tổng trọng số là: 5 + 7 + 8 + 10 = 30
=> Không tối ưu.

Câu 2:
-  BFS duyệt theo từng lớp -> tìm mọi đường ngắn nhất -> có thể ra nhiều đường có cùng độ dài.
-  DFS chỉ tìm một đường -> không đảm bảo ngắn nhất, không ra nhiều kết quả cùng độ dài.
Ví dụ từ Đồ thị mẫu 7:
Cả S → D → E → H và S → E → H đều dài 3 bước.
=> BFS có thể liệt kê cả hai, còn DFS thì chỉ ra một trong số đó.
