def tinhkhauhao(giamua,phivanchuyen,chiphilapdat,sonam):
    nguyengia=giamua+phivanchuyen+chiphilapdat
    khauhaonam=nguyengia/sonam
    khauhaonam=round(khauhaonam,2)
    khauhaothang=khauhaonam/12
    khauhaothang=round(khauhaothang,2)
    return nguyengia,khauhaonam,khauhaothang
def tinhchitietkhauhao(giamua,phivanchuyen,chiphilapdat,sonam):
    nguyengia=giamua+phivanchuyen+chiphilapdat
    khauhaonam=nguyengia/sonam
    chitiet=''
    khauhaoluyke=0
    for nam in range(1,sonam+1):
        if nam==sonam:
            khauhaonam=nguyengia-khauhaoluyke
        khauhaoluyke+=khauhaonam
        chitiet+=f"Năm{nam}: Còn lại: {nguyengia-khauhaoluyke:.2f}\n"
        

