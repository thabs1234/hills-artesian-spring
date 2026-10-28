#!/usr/bin/env python3
# Generate waterfall.svg
waterfall = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 800' width='600' height='800'>
  <defs>
    <linearGradient id='waterTop' x1='0' y1='0' x2='0' y2='1'>
      <stop offset='0' stop-color='#FFD700'/>
      <stop offset='0.15' stop-color='#F5A623'/>
      <stop offset='0.35' stop-color='#F2A900'/>
      <stop offset='0.6' stop-color='#E8910C'/>
      <stop offset='0.8' stop-color='#D4820A'/>
      <stop offset='1' stop-color='#BC6D08'/>
    </linearGradient>
    <linearGradient id='waterMid' x1='0' y1='0' x2='0' y2='1'>
      <stop offset='0' stop-color='#F2A900' stop-opacity='0.95'/>
      <stop offset='1' stop-color='#8B6914' stop-opacity='0.9'/>
    </linearGradient>
    <linearGradient id='rockFace' x1='0' y1='0' x2='0' y2='1'>
      <stop offset='0' stop-color='#4a3f35'/>
      <stop offset='0.3' stop-color='#3a3128'/>
      <stop offset='0.6' stop-color='#2a2118'/>
      <stop offset='0.8' stop-color='#1C1917'/>
      <stop offset='1' stop-color='#14110E'/>
    </linearGradient>
    <linearGradient id='skyGrad' x1='0' y1='0' x2='0' y2='1'>
      <stop offset='0' stop-color='#1C1917'/>
      <stop offset='0.4' stop-color='#221A14'/>
      <stop offset='0.7' stop-color='#1C1917'/>
      <stop offset='1' stop-color='#14110E'/>
    </linearGradient>
    <linearGradient id='foamGrad' x1='0' y1='0' x2='0' y2='1'>
      <stop offset='0' stop-color='#FFFFFF' stop-opacity='0.6'/>
      <stop offset='0.5' stop-color='#FFFFFF' stop-opacity='0.3'/>
      <stop offset='1' stop-color='#FFFFFF' stop-opacity='0.1'/>
    </linearGradient>
    <linearGradient id='mistGrad' x1='0' y1='0' x2='0' y2='1'>
      <stop offset='0' stop-color='rgba(192,192,192,0.15)'/>
      <stop offset='1' stop-color='rgba(192,192,192,0.05)'/>
    </linearGradient>
    <radialGradient id='sparkle' cx='50%' cy='50%' r='50%'>
      <stop offset='0' stop-color='#FFFFFF' stop-opacity='0.8'/>
      <stop offset='1' stop-color='#FFFFFF' stop-opacity='0'/>
    </radialGradient>
  </defs>
  <rect width='600' height='800' fill='url(#skyGrad)'/>
  <path d='M0,650 L0,620 Q80,600 150,610 Q220,605 300,620 Q380,610 460,620 Q520,615 600,620 L600,650 Z' fill='#2a2118' opacity='0.3'/>
  <path d='M0,680 L0,660 Q100,645 200,655 Q300,648 400,655 Q500,650 600,655 L600,680 Z' fill='#221A14' opacity='0.2'/>
  <path d='M0,0 L0,800 Q50,795 100,800 Q150,790 200,800 Q250,792 300,800 Q350,798 400,800 Q450,800 500,800 Q550,800 600,800 L600,0 Z' fill='url(#rockFace)'/>
  <path d='M0,0 L0,800 Q30,790 60,800 Q90,785 120,800 Q150,790 180,800 Q210,795 240,800 Q270,790 300,800 Q330,792 360,800 Q390,798 420,800 Q450,800 480,800 Q510,800 540,800 Q570,800 600,800 Z' fill='#2a2118' opacity='0.4'/>
  <g>
    <path d='M160,180 Q162,260 160,350 Q160,450 160,550 Q160,650 160,780 L155,780 Q155,650 155,550 Q155,450 155,350 Q155,260 155,180 Z' fill='url(#waterTop)' opacity='0.9'>
      <animate attributeName='d' values='M160,180 Q162,260 160,350 Q160,450 160,550 Q160,650 160,780 L155,780 Q155,650 155,550 Q155,450 155,350 Q155,260 155,180 Z;M160,185 Q162,265 160,355 Q160,455 160,555 Q160,655 160,785 L155,780 Q155,650 155,550 Q155,450 155,350 Q155,260 155,180 Z;M160,180 Q162,260 160,350 Q160,450 160,550 Q160,650 160,780 L155,780 Q155,650 155,550 Q155,450 155,350 Q155,260 155,180 Z' dur='4s' repeatCount='indefinite'/>
    </path>
    <path d='M175,190 Q177,270 175,360 Q175,460 175,560 Q175,660 175,790 L172,790 Q172,660 172,560 Q172,460 172,360 Q172,270 172,190 Z' fill='url(#waterMid)' opacity='0.85'>
      <animate attributeName='d' values='M175,190 Q177,270 175,360 Q175,460 175,560 Q175,660 175,790 L172,790 Q172,660 172,560 Q172,460 172,360 Q172,270 172,190 Z;M175,195 Q177,275 175,365 Q175,465 175,565 Q175,665 175,795 L172,790 Q172,660 172,560 Q172,460 172,360 Q172,270 172,190 Z;M175,190 Q177,270 175,360 Q175,460 175,560 Q175,660 175,790 L172,790 Q172,660 172,560 Q172,460 172,360 Q172,270 172,190 Z' dur='4.5s' repeatCount='indefinite'/>
    </path>
    <path d='M190,200 Q192,280 190,370 Q190,470 190,570 Q190,670 190,800 L189,800 Q189,670 189,570 Q189,470 189,370 Q189,280 189,200 Z' fill='url(#waterMid)' opacity='0.8'>
      <animate attributeName='d' values='M190,200 Q192,280 190,370 Q190,470 190,570 Q190,670 190,800 L189,800 Q189,670 189,570 Q189,470 189,370 Q189,280 189,200 Z;M190,205 Q192,285 190,375 Q190,475 190,575 Q190,675 190,805 L189,800 Q189,670 189,570 Q189,470 189,370 Q189,280 189,200 Z;M190,200 Q192,280 190,370 Q190,470 190,570 Q190,670 190,800 L189,800 Q189,670 189,570 Q189,470 189,370 Q189,280 189,200 Z' dur='5s' repeatCount='indefinite'/>
    </path>
  </g>
  <g>
    <path d='M140,150 Q150,170 160,180 Q170,170 180,150 Q175,160 170,150 Q165,165 160,150 Q155,160 150,150 Z' fill='url(#foamGrad)' opacity='0.7'>
      <animate attributeName='d' values='M140,150 Q150,170 160,180 Q170,170 180,150 Q175,160 170,150 Q165,165 160,150 Q155,160 150,150 Z;M140,155 Q150,175 160,185 Q170,175 180,155 Q175,165 170,155 Q165,170 160,155 Q155,165 150,155 Z;M140,150 Q150,170 160,180 Q170,170 180,150 Q175,160 170,150 Q165,165 160,150 Q155,160 150,150 Z' dur='3s' repeatCount='indefinite'/>
    </path>
    <path d='M150,140 Q160,160 170,170 Q180,160 190,140 Q185,155 180,140 Q175,155 170,140 Q165,155 160,140 Z' fill='url(#foamGrad)' opacity='0.5'/>
  </g>
  <ellipse cx='175' cy='790' rx='60' ry='12' fill='#8B6914' opacity='0.3'>
    <animate attributeName='rx' from='50' to='70' dur='2s' repeatCount='indefinite'/>
    <animate attributeName='opacity' from='0.2' to='0.4' dur='2s' repeatCount='indefinite'/>
  </ellipse>
  <ellipse cx='175' cy='790' rx='30' ry='6' fill='#D4820A' opacity='0.5'>
    <animate attributeName='rx' from='25' to='35' dur='1.5s' repeatCount='indefinite'/>
    <animate attributeName='opacity' from='0.4' to='0.6' dur='1.5s' repeatCount='indefinite'/>
  </ellipse>
  <g>
    <circle cx='162' cy='100' r='2.5' fill='#F5A623' opacity='0.9'>
      <animate attributeName='cy' from='100' to='790' dur='2.2s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.9;0.3;0.9' dur='2.2s' repeatCount='indefinite'/>
    </circle>
    <circle cx='163' cy='80' r='2' fill='#F5A623' opacity='0.8'>
      <animate attributeName='cy' from='80' to='790' dur='1.8s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.8;0.2;0.8' dur='1.8s' repeatCount='indefinite'/>
    </circle>
    <circle cx='161' cy='90' r='3' fill='#F5A623' opacity='0.85'>
      <animate attributeName='cy' from='90' to='790' dur='2.5s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.85;0.3;0.85' dur='2.5s' repeatCount='indefinite'/>
    </circle>
    <circle cx='164' cy='110' r='2' fill='#F2A900' opacity='0.8'>
      <animate attributeName='cy' from='110' to='790' dur='2s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.8;0.2;0.8' dur='2s' repeatCount='indefinite'/>
    </circle>
    <circle cx='160' cy='115' r='1.5' fill='#D4820A' opacity='0.7'>
      <animate attributeName='cy' from='115' to='790' dur='1.6s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.7;0.2;0.7' dur='1.6s' repeatCount='indefinite'/>
    </circle>
    <circle cx='163' cy='140' r='2.5' fill='#F2A900' opacity='0.85'>
      <animate attributeName='cy' from='140' to='790' dur='2.3s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.85;0.3;0.85' dur='2.3s' repeatCount='indefinite'/>
    </circle>
    <circle cx='165' cy='150' r='2' fill='#F2A900' opacity='0.8'>
      <animate attributeName='cy' from='150' to='790' dur='1.9s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.8;0.2;0.8' dur='1.9s' repeatCount='indefinite'/>
    </circle>
    <circle cx='161' cy='145' r='1.5' fill='#D4820A' opacity='0.7'>
      <animate attributeName='cy' from='145' to='790' dur='1.7s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.7;0.2;0.7' dur='1.7s' repeatCount='indefinite'/>
    </circle>
    <circle cx='162' cy='165' r='2.5' fill='#F5A623' opacity='0.85'>
      <animate attributeName='cy' from='165' to='790' dur='2.4s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.85;0.3;0.85' dur='2.4s' repeatCount='indefinite'/>
    </circle>
    <circle cx='164' cy='170' r='2' fill='#F2A900' opacity='0.8'>
      <animate attributeName='cy' from='170' to='790' dur='2.1s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.8;0.2;0.8' dur='2.1s' repeatCount='indefinite'/>
    </circle>
    <circle cx='170' cy='200' r='2' fill='#F2A900' opacity='0.8'>
      <animate attributeName='cy' from='200' to='790' dur='2.6s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.8;0.25;0.8' dur='2.6s' repeatCount='indefinite'/>
    </circle>
    <circle cx='168' cy='210' r='1.5' fill='#F2A900' opacity='0.7'>
      <animate attributeName='cy' from='210' to='790' dur='2.2s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.7;0.2;0.7' dur='2.2s' repeatCount='indefinite'/>
    </circle>
    <circle cx='172' cy='205' r='2' fill='#F2A900' opacity='0.75'>
      <animate attributeName='cy' from='205' to='790' dur='2.8s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.75;0.25;0.75' dur='2.8s' repeatCount='indefinite'/>
    </circle>
    <circle cx='169' cy='225' r='1.5' fill='#D4820A' opacity='0.6'>
      <animate attributeName='cy' from='225' to='790' dur='2.4s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.6;0.2;0.6' dur='2.4s' repeatCount='indefinite'/>
    </circle>
    <circle cx='171' cy='230' r='2' fill='#F2A900' opacity='0.7'>
      <animate attributeName='cy' from='230' to='790' dur='2.5s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.7;0.2;0.7' dur='2.5s' repeatCount='indefinite'/>
    </circle>
    <circle cx='167' cy='240' r='1.5' fill='#F5A623' opacity='0.7'>
      <animate attributeName='cy' from='240' to='790' dur='2.3s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.7;0.2;0.7' dur='2.3s' repeatCount='indefinite'/>
    </circle>
    <circle cx='173' cy='245' r='2' fill='#F2A900' opacity='0.75'>
      <animate attributeName='cy' from='245' to='790' dur='2.7s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.75;0.25;0.75' dur='2.7s' repeatCount='indefinite'/>
    </circle>
    <circle cx='170' cy='255' r='1.5' fill='#D4820A' opacity='0.6'>
      <animate attributeName='cy' from='255' to='790' dur='2.5s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.6;0.2;0.6' dur='2.5s' repeatCount='indefinite'/>
    </circle>
    <circle cx='168' cy='265' r='1.5' fill='#F5A623' opacity='0.7'>
      <animate attributeName='cy' from='265' to='790' dur='2.6s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.7;0.2;0.7' dur='2.6s' repeatCount='indefinite'/>
    </circle>
    <circle cx='172' cy='270' r='2' fill='#F2A900' opacity='0.7'>
      <animate attributeName='cy' from='270' to='790' dur='2.8s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.7;0.2;0.7' dur='2.8s' repeatCount='indefinite'/>
    </circle>
    <circle cx='175' cy='300' r='2' fill='#F2A900' opacity='0.75'>
      <animate attributeName='cy' from='300' to='790' dur='2.4s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.75;0.25;0.75' dur='2.4s' repeatCount='indefinite'/>
    </circle>
    <circle cx='173' cy='310' r='1.5' fill='#D4820A' opacity='0.6'>
      <animate attributeName='cy' from='310' to='790' dur='2.6s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.6;0.2;0.6' dur='2.6s' repeatCount='indefinite'/>
    </circle>
    <circle cx='176' cy='320' r='2' fill='#F2A900' opacity='0.7'>
      <animate attributeName='cy' from='320' to='790' dur='2.5s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.7;0.2;0.7' dur='2.5s' repeatCount='indefinite'/>
    </circle>
    <circle cx='174' cy='335' r='1.5' fill='#F5A623' opacity='0.65'>
      <animate attributeName='cy' from='335' to='790' dur='2.4s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.65;0.2;0.65' dur='2.4s' repeatCount='indefinite'/>
    </circle>
    <circle cx='177' cy='340' r='2' fill='#F2A900' opacity='0.65'>
      <animate attributeName='cy' from='340' to='790' dur='2.6s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.65;0.2;0.65' dur='2.6s' repeatCount='indefinite'/>
    </circle>
    <circle cx='172' cy='350' r='1.5' fill='#D4820A' opacity='0.6'>
      <animate attributeName='cy' from='350' to='790' dur='2.5s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.6;0.2;0.6' dur='2.5s' repeatCount='indefinite'/>
    </circle>
    <circle cx='175' cy='360' r='2' fill='#F2A900' opacity='0.65'>
      <animate attributeName='cy' from='360' to='790' dur='2.7s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.65;0.2;0.65' dur='2.7s' repeatCount='indefinite'/>
    </circle>
    <circle cx='170' cy='370' r='1.5' fill='#F5A623' opacity='0.6'>
      <animate attributeName='cy' from='370' to='790' dur='2.6s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.6;0.2;0.6' dur='2.6s' repeatCount='indefinite'/>
    </circle>
    <circle cx='176' cy='380' r='2' fill='#F2A900' opacity='0.65'>
      <animate attributeName='cy' from='380' to='790' dur='2.8s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.65;0.2;0.65' dur='2.8s' repeatCount='indefinite'/>
    </circle>
    <circle cx='173' cy='390' r='1.5' fill='#D4820A' opacity='0.55'>
      <animate attributeName='cy' from='390' to='790' dur='2.7s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.55;0.2;0.55' dur='2.7s' repeatCount='indefinite'/>
    </circle>
    <circle cx='180' cy='420' r='1.5' fill='#F2A900' opacity='0.55'>
      <animate attributeName='cy' from='420' to='790' dur='2.5s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.55;0.15;0.55' dur='2.5s' repeatCount='indefinite'/>
    </circle>
    <circle cx='178' cy='430' r='1.5' fill='#F5A623' opacity='0.5'>
      <animate attributeName='cy' from='430' to='790' dur='2.6s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.5;0.15;0.5' dur='2.6s' repeatCount='indefinite'/>
    </circle>
    <circle cx='182' cy='440' r='1.5' fill='#F2A900' opacity='0.5'>
      <animate attributeName='cy' from='440' to='790' dur='2.7s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.5;0.15;0.5' dur='2.7s' repeatCount='indefinite'/>
    </circle>
    <circle cx='179' cy='450' r='1.5' fill='#D4820A' opacity='0.45'>
      <animate attributeName='cy' from='450' to='790' dur='2.5s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.45;0.15;0.45' dur='2.5s' repeatCount='indefinite'/>
    </circle>
    <circle cx='183' cy='460' r='1.5' fill='#F2A900' opacity='0.5'>
      <animate attributeName='cy' from='460' to='790' dur='2.6s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.5;0.15;0.5' dur='2.6s' repeatCount='indefinite'/>
    </circle>
    <circle cx='177' cy='470' r='1.5' fill='#F5A623' opacity='0.45'>
      <animate attributeName='cy' from='470' to='790' dur='2.7s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.45;0.15;0.45' dur='2.7s' repeatCount='indefinite'/>
    </circle>
    <circle cx='181' cy='480' r='1.5' fill='#F2A900' opacity='0.45'>
      <animate attributeName='cy' from='480' to='790' dur='2.8s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.45;0.15;0.45' dur='2.8s' repeatCount='indefinite'/>
    </circle>
    <circle cx='175' cy='650' r='1' fill='#FFFFFF' opacity='0.4'>
      <animate attributeName='cy' from='650' to='790' dur='3s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.4;0;0.4' dur='3s' repeatCount='indefinite'/>
    </circle>
    <circle cx='175' cy='700' r='1' fill='#FFFFFF' opacity='0.3'>
      <animate attributeName='cy' from='700' to='790' dur='3.5s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.3;0;0.3' dur='3.5s' repeatCount='indefinite'/>
    </circle>
    <circle cx='175' cy='680' r='1' fill='#F2A900' opacity='0.4'>
      <animate attributeName='cy' from='680' to='790' dur='3.2s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.4;0;0.4' dur='3.2s' repeatCount='indefinite'/>
    </circle>
    <circle cx='175' cy='720' r='1' fill='#FFFFFF' opacity='0.35'>
      <animate attributeName='cy' from='720' to='790' dur='3.8s' repeatCount='indefinite'/>
      <animate attributeName='opacity' values='0.35;0;0.35' dur='3.8s' repeatCount='indefinite'/>
    </circle>
  </g>
  <ellipse cx='175' cy='790' rx='50' ry='8' fill='#D4AF37' opacity='0.15'>
    <animate attributeName='rx' from='40' to='60' dur='1.8s' repeatCount='indefinite'/>
    <animate attributeName='opacity' from='0.1' to='0.25' dur='1.8s' repeatCount='indefinite'/>
  </ellipse>
  <ellipse cx='175' cy='770' rx='120' ry='15' fill='url(#mistGrad)' opacity='0.4'>
    <animate attributeName='opacity' values='0.3;0.5;0.3' dur='4s' repeatCount='indefinite'/>
    <animate attributeName='rx' values='110;130;110' dur='4s' repeatCount='indefinite'/>
  </ellipse>
  <ellipse cx='160' cy='450' rx='80' ry='6' fill='#F2A900' opacity='0.05'>
    <animate attributeName='opacity' values='0.03;0.07;0.03' dur='3s' repeatCount='indefinite'/>
  </ellipse>
</svg>"""
with open('waterfall.svg', 'w') as f:
    f.write(waterfall)
print('waterfall.svg created, size:', len(waterfall), 'bytes')
