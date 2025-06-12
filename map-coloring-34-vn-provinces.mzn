% === Danh sách tỉnh ===
enum REGION = {
  LAI_CHAU, DIEN_BIEN, SON_LA, LAO_CAI, TUYEN_QUANG, CAO_BANG, THAI_NGUYEN,
  PHU_THO, HA_NOI, BAC_NINH, LANG_SON, QUANG_NINH, HAI_PHONG, HUNG_YEN,
  NINH_BINH, THANH_HOA, NGHE_AN, HA_TINH, QUANG_TRI, HUE, DA_NANG,
  QUANG_NGAI, GIA_LAI, DAK_LAK, KHANH_HOA, DONG_NAI, LAM_DONG, TAY_NINH,
  HO_CHI_MINH, DONG_THAP, VINH_LONG, AN_GIANG, CAN_THO, CA_MAU
};

enum COLOR = Color(1..card(REGION));

% === Quan hệ láng giềng (chỉnh phần này nếu đổi bản đồ) ===
array [int] of tuple(REGION, REGION): neighbors = [
  (LAI_CHAU, DIEN_BIEN), (LAI_CHAU, SON_LA), (LAI_CHAU, LAO_CAI),
  (DIEN_BIEN, SON_LA),
  (SON_LA, LAO_CAI), (SON_LA, PHU_THO), (SON_LA, THANH_HOA),
  (LAO_CAI, TUYEN_QUANG), (LAO_CAI, PHU_THO),
  (TUYEN_QUANG, PHU_THO), (TUYEN_QUANG, THAI_NGUYEN), (TUYEN_QUANG, CAO_BANG),
  (CAO_BANG, THAI_NGUYEN), (CAO_BANG, LANG_SON),
  (THAI_NGUYEN, LANG_SON), (THAI_NGUYEN, BAC_NINH), (THAI_NGUYEN, PHU_THO), (THAI_NGUYEN, HA_NOI),
  (PHU_THO, THANH_HOA), (PHU_THO, HA_NOI),
  (HA_NOI, BAC_NINH), (HA_NOI, HUNG_YEN), (HA_NOI, NINH_BINH),
  (BAC_NINH, LANG_SON),
  (LANG_SON, QUANG_NINH),
  (QUANG_NINH, HAI_PHONG),
  (HAI_PHONG, HUNG_YEN),
  (HUNG_YEN, NINH_BINH),
  (NINH_BINH, THANH_HOA),
  (THANH_HOA, NGHE_AN),
  (NGHE_AN, HA_TINH),
  (HA_TINH, QUANG_TRI),
  (QUANG_TRI, HUE),
  (HUE, DA_NANG),
  (DA_NANG, QUANG_NGAI),
  (QUANG_NGAI, GIA_LAI),
  (GIA_LAI, DAK_LAK),
  (DAK_LAK, LAM_DONG), (DAK_LAK, KHANH_HOA),
  (KHANH_HOA, DONG_NAI),
  (DONG_NAI, LAM_DONG), (DONG_NAI, TAY_NINH), (DONG_NAI, HO_CHI_MINH),
  (TAY_NINH, HO_CHI_MINH),
  (HO_CHI_MINH, DONG_THAP),
  (DONG_THAP, VINH_LONG), (DONG_THAP, AN_GIANG),
  (VINH_LONG, CAN_THO),
  (CAN_THO, CA_MAU)
];

% === Biến màu của mỗi tỉnh ===
array [REGION] of var COLOR: color;

% === Sử dụng ít màu nhất có thể ===
include "nvalue_fn.mzn";
var 1..card(COLOR): n_colors :: output = nvalue(color);

% === Ràng buộc: Các tỉnh giáp nhau không được trùng màu ===
constraint forall (pair in neighbors) (
  color[pair.1] != color[pair.2]
);

% === Giải bài toán ===
solve minimize n_colors;

% === Kết quả in ra hoặc vẽ nếu cần ===
include "visualise.mzn";
