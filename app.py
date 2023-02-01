#!/usr/bin/env python
# coding: utf-8

# In[5]:


from fastapi import FastAPI
import uvicorn
import pickle
from models import Test

# In[6]:


app = FastAPI()
model = pickle.load(open("model_pickle.pkl", "rb"))


# In[19]:


@app.get("/{name}")
def hello(name):
    return {"Hello {} and welcome to this API".format(name)}


# In[20]:


@app.get("/")
def greet():
    return{"Hello World!"}


# In[21]:
@app.post("/predict")
def predict(req: Test):
    x1 = req.X1
    x2 = req.X2
    x3 = req.X3
    x4 = req.X4
    x5 = req.X5
    x6 = req.X6
    x7 = req.X7
    x8 = req.X8
    x9 = req.X9
    x10 = req.X10
    x11 = req.X11
    x12 = req.X12
    x13 = req.X13
    x14 = req.X14
    x15 = req.X15
    x16 = req.X16
    x17 = req.X17
    x18 = req.X18
    x19 = req.X19
    x20 = req.X20
    x21 = req.X21
    x22 = req.X22
    x23 = req.X23
    x24 = req.X24
    x25 = req.X25
    x26 = req.X26
    x27 = req.X27
    x28 = req.X28
    x29 = req.X29
    x30 = req.X30
    x31 = req.X31
    x32 = req.X32
    x33 = req.X33
    x34 = req.X34
    x35 = req.X35
    x36 = req.X36
    x37 = req.X37
    x38 = req.X38
    x39 = req.X39
    x40 = req.X40
    x41 = req.X41
    x42 = req.X42
    x43 = req.X43
    x44 = req.X44
    x45 = req.X45
    x46 = req.X46
    x47 = req.X47
    x48 = req.X48
    x49 = req.X49
    x50 = req.X50
    x51 = req.X51
    x52 = req.X52
    x53 = req.X53
    x54 = req.X54
    x55 = req.X55
    x56 = req.X56
    x57 = req.X57
    x58 = req.X58
    x59 = req.X59
    x60 = req.X60
    x61 = req.X61
    x62 = req.X62
    x63 = req.X63
    x64 = req.X64
    x65 = req.X65
    x66 = req.X66
    x67 = req.X67
    x68 = req.X68
    x69 = req.X69
    x70 = req.X70
    x71 = req.X71
    x72 = req.X72
    x73 = req.X73
    x74 = req.X74
    x75 = req.X75
    x76 = req.X76
    x77 = req.X77
    x78 = req.X78
    x79 = req.X79
    x80 = req.X80
    x81 = req.X81
    x82 = req.X82
    x83 = req.X83
    x84 = req.X84
    x85 = req.X85
    x86 = req.X86
    x87 = req.X87
    x88 = req.X88
    x89 = req.X89
    x90 = req.X90
    x91 = req.X91
    x92 = req.X92
    x93 = req.X93
    x94 = req.X94
    x95 = req.X95
    x96 = req.X96
    x97 = req.X97
    x98 = req.X98
    x99 = req.X99
    x100 = req.X100
    x101 = req.X101
    x102 = req.X102
    x103 = req.X103
    x104 = req.X104
    x105 = req.X105
    x106 = req.X106
    x107 = req.X107
    x108 = req.X108
    x109 = req.X109
    x110 = req.X110
    x111 = req.X111
    x112 = req.X112
    x113 = req.X113
    x114 = req.X114
    x115 = req.X115
    x116 = req.X116
    x117 = req.X117
    x118 = req.X118
    x119 = req.X119
    x120 = req.X120
    x121 = req.X121
    x122 = req.X122
    x123 = req.X123
    x124 = req.X124
    x125 = req.X125
    x126 = req.X126
    x127 = req.X127
    x128 = req.X128
    x129 = req.X129
    x130 = req.X130
    x131 = req.X131
    x132 = req.X132
    x133 = req.X133
    x134 = req.X134
    x135 = req.X135
    x136 = req.X136
    x137 = req.X137
    x138 = req.X138
    x139 = req.X139
    x140 = req.X140
    x141 = req.X141
    x142 = req.X142
    x143 = req.X143
    x144 = req.X144
    x145 = req.X145
    x146 = req.X146
    x147 = req.X147
    x148 = req.X148
    x149 = req.X149
    x150 = req.X150
    x151 = req.X151
    x152 = req.X152
    x153 = req.X153
    x154 = req.X154
    x155 = req.X155
    x156 = req.X156
    x157 = req.X157
    x158 = req.X158
    x159 = req.X159
    x160 = req.X160
    x161 = req.X161
    x162 = req.X162
    x163 = req.X163
    x164 = req.X164
    x165 = req.X165
    x166 = req.X166
    x167 = req.X167
    x168 = req.X168
    x169 = req.X169
    x170 = req.X170
    x171 = req.X171
    x172 = req.X172
    x173 = req.X173
    x174 = req.X174
    x175 = req.X175
    x176 = req.X176
    x177 = req.X177
    x178 = req.X178
    features = list([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33,x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46, x47, x48, x49, x50, x51, x52, x53, x54, x55, x56, x57, x58, x59, x60, x61,x62, x63, x64, x65, x66, x67, x68, x69, x70, x71, x72, x73, x74, x75, x76, x77, x78, x79, x80, x81, x82, x83, x84, x85, x89, x90, x91, x92, x93, x94, x95, x96, x97, x98, x99, x100, x101, x102, x103, x104, x105, x106, x107, x108, x109, x110, x111, x112, x113, x114, x115, x116, x117, x118, x119, x120, x121, x122, x123, x124, x125, x126, x127, x128, x129, x130, x131, x132, x133, x134, x135, x136, x137, x138, x139, x140, x141, x142, x143, x144, x145, x146, x147, x148, x149, x150, x151, x152, x153, x154, x155, x156, x157, x158, x159, x160, x161, x162, x163, x164, x165, x166, x167, x168, x169, x170, x171, x172, x173, x174, x175, x176, x177, x178 ])
    predict = model.predict([features])
    probab = model.predict_proba([features])
    if(predict==1):
        return {"ans": "you have been tested positive with this {} probability".format(probab[0][1])}
    else:
        return {"ans": "you have been tested positive with this {} probability".format(probab[0][0])}







if __name__ == "__main__":
    uvicorn.run(app)


# In[ ]:





# In[ ]:




