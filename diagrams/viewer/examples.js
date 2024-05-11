const examples={
    actdiag:`actdiag {
write -> convert -> image

    lane user {
        label = "User"
        write [label = "Writing reST"];
        image [label = "Get diagram IMAGE"];
    }
    lane actdiag {
        convert [label = "Convert reST to Image"];
    }
}
`,
    blockdiag:`blockdiag {
    blockdiag -> generates -> "block-diagrams";
    blockdiag -> is -> "very easy!";

    blockdiag [color = "greenyellow"];
    "block-diagrams" [color = "pink"];
    "very easy!" [color = "orange"];
}
`,
seqdiag:`seqdiag {
    browser  -> webserver [label = "GET /index.html"];
    browser <-- webserver;
    browser  -> webserver [label = "POST /blog/comment"];
    webserver  -> database [label = "INSERT comment"];
    webserver <-- database;
    browser <-- webserver;
}`,
nwdiag:`nwdiag {
    network dmz {
        address = "210.x.x.x/24"

        web01 [address = "210.x.x.1"];
        web02 [address = "210.x.x.2"];
    }
    network internal {
        address = "172.x.x.x/24";

        web01 [address = "172.x.x.1"];
        web02 [address = "172.x.x.2"];
        db01;
        db02;
    }
}`,
mermaid:`graph TD
A[ Anyone ] -->|Can help | B( Go to github.com/yuzutech/kroki )
B --> C{ How to contribute? }
C --> D[ Reporting bugs ]
C --> E[ Sharing ideas ]
C --> F[ Advocating ]
`,
packetdiag:`packetdiag {
    colwidth = 32;
    node_height = 72;

    0-15: Source Port;
    16-31: Destination Port;
    32-63: Sequence Number;
    64-95: Acknowledgment Number;
    96-99: Data Offset;
    100-105: Reserved;
    106: URG [rotate = 270];
    107: ACK [rotate = 270];
    108: PSH [rotate = 270];
    109: RST [rotate = 270];
    110: SYN [rotate = 270];
    111: FIN [rotate = 270];
    112-127: Window;
    128-143: Checksum;
    144-159: Urgent Pointer;
    160-191: (Options and Padding);
    192-223: data [colheight = 3];
}`,
rackdiag:`rackdiag {
16U;
1: UPS [2U];
3: DB Server;
4: Web Server;
5: Web Server;
6: Web Server;
7: Load Balancer;
8: L3 Switch;
}`,
graphviz:`digraph "unix" {
graph [ fontname = "Helvetica-Oblique",
        fontsize = 36,
        label = "\n\n\n\nObject Oriented Graphs\nStephen North, 3/19/93",
        size = "6,6" ];
node [ shape = polygon,
        sides = 4,
        distortion = "0.0",
        orientation = "0.0",
        skew = "0.0",
        color = white,
        style = filled,
        fontname = "Helvetica-Outline" ];
"5th Edition" [sides=9, distortion="0.936354", orientation=28, skew="-0.126818", color=salmon2];
"6th Edition" [sides=5, distortion="0.238792", orientation=11, skew="0.995935", color=deepskyblue];
"PWB 1.0" [sides=8, distortion="0.019636", orientation=79, skew="-0.440424", color=goldenrod2];
LSX [sides=9, distortion="-0.698271", orientation=22, skew="-0.195492", color=burlywood2];
"1 BSD" [sides=7, distortion="0.265084", orientation=26, skew="0.403659", color=gold1];
"Mini Unix" [distortion="0.039386", orientation=2, skew="-0.461120", color=greenyellow];
Wollongong [sides=5, distortion="0.228564", orientation=63, skew="-0.062846", color=darkseagreen];
Interdata [distortion="0.624013", orientation=56, skew="0.101396", color=dodgerblue1];
"Unix/TS 3.0" [sides=8, distortion="0.731383", orientation=43, skew="-0.824612", color=thistle2];
"PWB 2.0" [sides=6, distortion="0.592100", orientation=34, skew="-0.719269", color=darkolivegreen3];
"7th Edition" [sides=10, distortion="0.298417", orientation=65, skew="0.310367", color=chocolate];
"8th Edition" [distortion="-0.997093", orientation=50, skew="-0.061117", color=turquoise3];
"32V" [sides=7, distortion="0.878516", orientation=19, skew="0.592905", color=steelblue3];
V7M [sides=10, distortion="-0.960249", orientation=32, skew="0.460424", color=navy];
"Ultrix-11" [sides=10, distortion="-0.633186", orientation=10, skew="0.333125", color=darkseagreen4];
Xenix [sides=8, distortion="-0.337997", orientation=52, skew="-0.760726", color=coral];
"UniPlus+" [sides=7, distortion="0.788483", orientation=39, skew="-0.526284", color=darkolivegreen3];
"9th Edition" [sides=7, distortion="0.138690", orientation=55, skew="0.554049", color=coral3];
"2 BSD" [sides=7, distortion="-0.010661", orientation=84, skew="0.179249", color=blanchedalmond];
"2.8 BSD" [distortion="-0.239422", orientation=44, skew="0.053841", color=lightskyblue1];
"2.9 BSD" [distortion="-0.843381", orientation=70, skew="-0.601395", color=aquamarine2];
"3 BSD" [sides=10, distortion="0.251820", orientation=18, skew="-0.530618", color=lemonchiffon];
"4 BSD" [sides=5, distortion="-0.772300", orientation=24, skew="-0.028475", color=darkorange1];
"4.1 BSD" [distortion="-0.226170", orientation=38, skew="0.504053", color=lightyellow1];
"4.2 BSD" [sides=10, distortion="-0.807349", orientation=50, skew="-0.908842", color=darkorchid4];
"4.3 BSD" [sides=10, distortion="-0.030619", orientation=76, skew="0.985021", color=lemonchiffon2];
"Ultrix-32" [distortion="-0.644209", orientation=21, skew="0.307836", color=goldenrod3];
"PWB 1.2" [sides=7, distortion="0.640971", orientation=84, skew="-0.768455", color=cyan];
"USG 1.0" [distortion="0.758942", orientation=42, skew="0.039886", color=blue];
"CB Unix 1" [sides=9, distortion="-0.348692", orientation=42, skew="0.767058", color=firebrick];
"USG 2.0" [distortion="0.748625", orientation=74, skew="-0.647656", color=chartreuse4];
"CB Unix 2" [sides=10, distortion="0.851818", orientation=32, skew="-0.020120", color=greenyellow];
"CB Unix 3" [sides=10, distortion="0.992237", orientation=29, skew="0.256102", color=bisque4];
"Unix/TS++" [sides=6, distortion="0.545461", orientation=16, skew="0.313589", color=mistyrose2];
"PDP-11 Sys V" [sides=9, distortion="-0.267769", orientation=40, skew="0.271226", color=cadetblue1];
"USG 3.0" [distortion="-0.848455", orientation=44, skew="0.267152", color=bisque2];
"Unix/TS 1.0" [distortion="0.305594", orientation=75, skew="0.070516", color=orangered];
"TS 4.0" [sides=10, distortion="-0.641701", orientation=50, skew="-0.952502", color=crimson];
"System V.0" [sides=9, distortion="0.021556", orientation=26, skew="-0.729938", color=darkorange1];
"System V.2" [sides=6, distortion="0.985153", orientation=33, skew="-0.399752", color=darkolivegreen4];
"System V.3" [sides=7, distortion="-0.687574", orientation=58, skew="-0.180116", color=lightsteelblue1];
"5th Edition" -> "6th Edition";
"5th Edition" -> "PWB 1.0";
"6th Edition" -> LSX;
"6th Edition" -> "1 BSD";
"6th Edition" -> "Mini Unix";
"6th Edition" -> Wollongong;
"6th Edition" -> Interdata;
Interdata -> "Unix/TS 3.0";
Interdata -> "PWB 2.0";
Interdata -> "7th Edition";
"7th Edition" -> "8th Edition";
"7th Edition" -> "32V";
"7th Edition" -> V7M;
"7th Edition" -> "Ultrix-11";
"7th Edition" -> Xenix;
"7th Edition" -> "UniPlus+";
V7M -> "Ultrix-11";
"8th Edition" -> "9th Edition";
"1 BSD" -> "2 BSD";
"2 BSD" -> "2.8 BSD";
"2.8 BSD" -> "Ultrix-11";
"2.8 BSD" -> "2.9 BSD";
"32V" -> "3 BSD";
"3 BSD" -> "4 BSD";
"4 BSD" -> "4.1 BSD";
"4.1 BSD" -> "4.2 BSD";
"4.1 BSD" -> "2.8 BSD";
"4.1 BSD" -> "8th Edition";
"4.2 BSD" -> "4.3 BSD";
"4.2 BSD" -> "Ultrix-32";
"PWB 1.0" -> "PWB 1.2";
"PWB 1.0" -> "USG 1.0";
"PWB 1.2" -> "PWB 2.0";
"USG 1.0" -> "CB Unix 1";
"USG 1.0" -> "USG 2.0";
"CB Unix 1" -> "CB Unix 2";
"CB Unix 2" -> "CB Unix 3";
"CB Unix 3" -> "Unix/TS++";
"CB Unix 3" -> "PDP-11 Sys V";
"USG 2.0" -> "USG 3.0";
"USG 3.0" -> "Unix/TS 3.0";
"PWB 2.0" -> "Unix/TS 3.0";
"Unix/TS 1.0" -> "Unix/TS 3.0";
"Unix/TS 3.0" -> "TS 4.0";
"Unix/TS++" -> "TS 4.0";
"CB Unix 3" -> "TS 4.0";
"TS 4.0" -> "System V.0";
"System V.0" -> "System V.2";
"System V.2" -> "System V.3";
}`,
pikchr:`scale = 0.8
fill = white
linewid *= 0.5
circle "C0" fit
circlerad = previous.radius
arrow
circle "C1"
arrow
circle "C2"
arrow
circle "C4"
arrow
circle "C6"
circle "C3" at dist(C2,C4) heading 30 from C2
arrow
circle "C5"
arrow from C2 to C3 chop
C3P: circle "C3'" at dist(C4,C6) heading 30 from C6
arrow right from C3P.e
C5P: circle "C5'"
arrow from C6 to C3P chop

box height C3.y-C2.y \
    width (C5P.e.x-C0.w.x)+linewid \
    with .w at 0.5*linewid west of C0.w \
    behind C0 \
    fill 0xc6e2ff thin color gray
box same width previous.e.x - C2.w.x \
    with .se at previous.ne \
    fill 0x9accfc
"trunk" below at 2nd last box.s
"feature branch" above at last box.n

circle "C0" at 3.7cm south of C0
arrow
circle "C1"
arrow
circle "C2"
arrow
circle "C4"
arrow
circle "C6"
circle "C3" at dist(C2,C4) heading 30 from C2
arrow
circle "C5"
arrow
circle "C7"
arrow from C2 to C3 chop
arrow from C6 to C7 chop

box height C3.y-C2.y \
    width (C7.e.x-C0.w.x)+1.5*C1.radius \
    with .w at 0.5*linewid west of C0.w \
    behind C0 \
    fill 0xc6e2ff thin color gray
box same width previous.e.x - C2.w.x \
    with .se at previous.ne \
    fill 0x9accfc
"trunk" below at 2nd last box.s
"feature branch" above at last box.n`,
erd:`[Person]
*name
height
weight
+birth_location_id

[Location]
*id
city
state
country

Person *--1 Location`,
vegalite:`{
    "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
    "description": "A diverging stacked bar chart for sentiments towards a set of eight questions, displayed as percentages with neutral responses straddling the 0% mark",
    "data": {
      "values": [
        {"question": "Question 1", "type": "Strongly disagree", "value": 24, "percentage": 0.7},
        {"question": "Question 1", "type": "Disagree", "value": 294, "percentage": 9.1},
        {"question": "Question 1", "type": "Neither agree nor disagree", "value": 594, "percentage": 18.5},
        {"question": "Question 1", "type": "Agree", "value": 1927, "percentage": 59.9},
        {"question": "Question 1", "type": "Strongly agree", "value": 376, "percentage": 11.7},
        {"question": "Question 2", "type": "Strongly disagree", "value": 2, "percentage": 18.2},
        {"question": "Question 2", "type": "Disagree", "value": 2, "percentage": 18.2},
        {"question": "Question 2", "type": "Neither agree nor disagree", "value": 0, "percentage": 0},
        {"question": "Question 2", "type": "Agree", "value": 7, "percentage": 63.6},
        {"question": "Question 2", "type": "Strongly agree", "value": 11, "percentage": 0},
        {"question": "Question 3", "type": "Strongly disagree", "value": 2, "percentage": 20},
        {"question": "Question 3", "type": "Disagree", "value": 0, "percentage": 0},
        {"question": "Question 3", "type": "Neither agree nor disagree", "value": 2, "percentage": 20},
        {"question": "Question 3", "type": "Agree", "value": 4, "percentage": 40},
        {"question": "Question 3", "type": "Strongly agree", "value": 2, "percentage": 20},
        {"question": "Question 4", "type": "Strongly disagree", "value": 0, "percentage": 0},
        {"question": "Question 4", "type": "Disagree", "value": 2, "percentage": 12.5},
        {"question": "Question 4", "type": "Neither agree nor disagree", "value": 1, "percentage": 6.3},
        {"question": "Question 4", "type": "Agree", "value": 7, "percentage": 43.8},
        {"question": "Question 4", "type": "Strongly agree", "value": 6, "percentage": 37.5},
        {"question": "Question 5", "type": "Strongly disagree", "value": 0, "percentage": 0},
        {"question": "Question 5", "type": "Disagree", "value": 1, "percentage": 4.2},
        {"question": "Question 5", "type": "Neither agree nor disagree", "value": 3, "percentage": 12.5},
        {"question": "Question 5", "type": "Agree", "value": 16, "percentage": 66.7},
        {"question": "Question 5", "type": "Strongly agree", "value": 4, "percentage": 16.7},
        {"question": "Question 6", "type": "Strongly disagree", "value": 1, "percentage": 6.3},
        {"question": "Question 6", "type": "Disagree", "value": 1, "percentage": 6.3},
        {"question": "Question 6", "type": "Neither agree nor disagree", "value": 2, "percentage": 12.5},
        {"question": "Question 6", "type": "Agree", "value": 9, "percentage": 56.3},
        {"question": "Question 6", "type": "Strongly agree", "value": 3, "percentage": 18.8},
        {"question": "Question 7", "type": "Strongly disagree", "value": 0, "percentage": 0},
        {"question": "Question 7", "type": "Disagree", "value": 0, "percentage": 0},
        {"question": "Question 7", "type": "Neither agree nor disagree", "value": 1, "percentage": 20},
        {"question": "Question 7", "type": "Agree", "value": 4, "percentage": 80},
        {"question": "Question 7", "type": "Strongly agree", "value": 0, "percentage": 0},
        {"question": "Question 8", "type": "Strongly disagree", "value": 0, "percentage": 0},
        {"question": "Question 8", "type": "Disagree", "value": 0, "percentage": 0},
        {"question": "Question 8", "type": "Neither agree nor disagree", "value": 0, "percentage": 0},
        {"question": "Question 8", "type": "Agree", "value": 0, "percentage": 0},
        {"question": "Question 8", "type": "Strongly agree", "value": 2, "percentage": 100}
      ]
    },
    "transform": [
      {
        "calculate": "if(datum.type === 'Strongly disagree',-2,0) + if(datum.type==='Disagree',-1,0) + if(datum.type =='Neither agree nor disagree',0,0) + if(datum.type ==='Agree',1,0) + if(datum.type ==='Strongly agree',2,0)",
        "as": "q_order"
      },
      {
        "calculate": "if(datum.type === 'Disagree' || datum.type === 'Strongly disagree', datum.percentage,0) + if(datum.type === 'Neither agree nor disagree', datum.percentage / 2,0)",
        "as": "signed_percentage"
      },
      {"stack": "percentage", "as": ["v1", "v2"], "groupby": ["question"]},
      {
        "joinaggregate": [
          {
            "field": "signed_percentage",
            "op": "sum",
            "as": "offset"
          }
        ],
        "groupby": ["question"]
      },
      {"calculate": "datum.v1 - datum.offset", "as": "nx"},
      {"calculate": "datum.v2 - datum.offset", "as": "nx2"}
    ],
    "mark": "bar",
    "encoding": {
      "x": {
        "field": "nx",
        "type": "quantitative",
        "axis": {
          "title": "Percentage"
        }
      },
      "x2": {"field": "nx2"},
      "y": {
        "field": "question",
        "type": "nominal",
        "axis": {
          "title": "Question",
          "offset": 5,
          "ticks": false,
          "minExtent": 60,
          "domain": false
        }
      },
      "color": {
        "field": "type",
        "type": "nominal",
        "legend": {
          "title": "Response"
        },
        "scale": {
          "domain": ["Strongly disagree", "Disagree", "Neither agree nor disagree", "Agree", "Strongly agree"],
          "range": ["#c30d24", "#f3a583", "#cccccc", "#94c6da", "#1770ab"],
          "type": "ordinal"
        }
      }
    }
  }`,
nomnoml:`[Pirate|eyeCount: Int|raid();pillage()|
    [beard]--[parrot]
    [beard]-:>[foul mouth]
  ]
  
  [<abstract>Marauder]<:--[Pirate]
  [Pirate]- 0..7[mischief]
  [jollyness]->[Pirate]
  [jollyness]->[rum]
  [jollyness]->[singing]
  [Pirate]-> *[rum|tastiness: Int|swig()]
  [Pirate]->[singing]
  [singing]<->[rum]
  
  [<start>st]->[<state>plunder]
  [plunder]->[<choice>more loot]
  [more loot]->[st]
  [more loot] no ->[<end>e]
  
  [<actor>Sailor] - [<usecase>shiver me;timbers]`,
plantuml:`@startuml
left to right direction
skinparam packageStyle rectangle
skinparam monochrome true
actor customer
actor clerk
rectangle checkout {
  customer -- (checkout)
  (checkout) .> (payment) : include
  (help) .> (checkout) : extends
  (checkout) -- clerk
}
@enduml`,
bytefield:`(defattrs :bg-green {:fill "#a0ffa0"})
(defattrs :bg-yellow {:fill "#ffffa0"})
(defattrs :bg-pink {:fill "#ffb0a0"})
(defattrs :bg-cyan {:fill "#a0fafa"})
(defattrs :bg-purple {:fill "#e4b5f7"})

(defn draw-group-label-header
  "Creates a small borderless box used to draw the textual label headers
  used below the byte labels for remotedb message diagrams.
  Arguments are the number of columns to span and the text of the
  label."
  [span label]
  (draw-box (text label [:math {:font-size 12}]) {:span    span
                                                  :borders #{}
                                                  :height  14}))

(defn draw-remotedb-header
  "Generates the byte and field labels and standard header fields of a
  request or response message for the remotedb database server with
  the specified kind and args values."
  [kind args]
  (draw-column-headers)
  (draw-group-label-header 5 "start")
  (draw-group-label-header 5 "TxID")
  (draw-group-label-header 3 "type")
  (draw-group-label-header 2 "args")
  (draw-group-label-header 1 "tags")
  (next-row 18)

  (draw-box 0x11 :bg-green)
  (draw-box 0x872349ae [{:span 4} :bg-green])
  (draw-box 0x11 :bg-yellow)
  (draw-box (text "TxID" :math) [{:span 4} :bg-yellow])
  (draw-box 0x10 :bg-pink)
  (draw-box (hex-text kind 4 :bold) [{:span 2} :bg-pink])
  (draw-box 0x0f :bg-cyan)
  (draw-box (hex-text args 2 :bold) :bg-cyan)
  (draw-box 0x14 :bg-purple)

  (draw-box (text "0000000c" :hex [[:plain {:font-weight "light" :font-size 16}] " (12)"])
            [{:span 4} :bg-purple])
  (draw-box (hex-text 6 2 :bold) [:box-first :bg-purple])
  (doseq [val [6 6 3 6 6 6 6 3]]
    (draw-box (hex-text val 2 :bold) [:box-related :bg-purple]))
  (doseq [val [0 0]]
    (draw-box val [:box-related :bg-purple]))
  (draw-box 0 [:box-last :bg-purple]))

(draw-remotedb-header 0x4702 9)

(draw-box 0x11)
(draw-box 0x2104 {:span 4})
(draw-box 0x11)
(draw-box 0 {:span 4})
(draw-box 0x11)
(draw-box (text "length" [:math] [:sub 1]) {:span 4})
(draw-box 0x14)

(draw-box (text "length" [:math] [:sub 1]) {:span 4})
(draw-gap "Cue and loop point bytes")

(draw-box nil :box-below)
(draw-box 0x11)
(draw-box 0x36 {:span 4})
(draw-box 0x11)
(draw-box (text "num" [:math] [:sub "hot"]) {:span 4})
(draw-box 0x11)
(draw-box (text "num" [:math] [:sub "cue"]) {:span 4})

(draw-box 0x11)
(draw-box (text "length" [:math] [:sub 2]) {:span 4})
(draw-box 0x14)
(draw-box (text "length" [:math] [:sub 2]) {:span 4})
(draw-gap "Unknown bytes" {:min-label-columns 6})
(draw-bottom)`,
wavedrom:`{ signal: [
    { name: "clk",         wave: "p.....|..." },
    { name: "Data",        wave: "x.345x|=.x", data: ["head", "body", "tail", "data"] },
    { name: "Request",     wave: "0.1..0|1.0" },
    {},
    { name: "Acknowledge", wave: "1.....|01." }
  ]}`,
diagramsnet:`<mxfile host="Electron" modified="2022-03-26T10:52:07.381Z" agent="5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/17.2.1 Chrome/96.0.4664.174 Electron/16.1.0 Safari/537.36" etag="c7rPkDjiJFuVDdgIdBCQ" version="17.2.1" type="device">
<diagram id="is4nKnoC7knK3tbmEpOL" name="ページ1">
  <mxGraphModel dx="1102" dy="857" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
    <root>
      <mxCell id="0" />
      <mxCell id="1" parent="0" />
      <object placeholders="1" c4Name="Banking Customer" c4Type="Person" c4Description="A customer of the bank, &#xa;with personal bank accounts." label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#cccccc&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;" id="v1w6xJLIwrtz22bP0FQ9-1">
        <mxCell style="html=1;fontSize=11;dashed=0;whitespace=wrap;fillColor=#083F75;strokeColor=#06315C;fontColor=#ffffff;shape=mxgraph.c4.person2;align=center;metaEdit=1;points=[[0.5,0,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0]];resizable=0;" parent="1" vertex="1">
          <mxGeometry x="260" y="40" width="200" height="180" as="geometry" />
        </mxCell>
      </object>
      <mxCell id="v1w6xJLIwrtz22bP0FQ9-2" value="Legend" style="align=left;fontSize=16;fontStyle=1;strokeColor=none;fillColor=none;fontColor=#4D4D4D;spacingTop=-8;resizable=0;" parent="1" vertex="1">
        <mxGeometry x="40" y="10" width="180" height="30" as="geometry" />
      </mxCell>
      <mxCell id="v1w6xJLIwrtz22bP0FQ9-3" value="" style="shape=table;html=1;whiteSpace=wrap;startSize=0;container=1;collapsible=0;childLayout=tableLayout;fillColor=none;align=left;spacingLeft=10;strokeColor=none;rounded=1;arcSize=11;fontColor=#FFFFFF;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];" parent="1" vertex="1">
        <mxGeometry x="40" y="40" width="180" height="180" as="geometry" />
      </mxCell>
      <mxCell id="v1w6xJLIwrtz22bP0FQ9-4" value="Person" style="shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;fillColor=#1E4074;top=0;left=0;bottom=0;right=0;overflow=hidden;pointerEvents=1;align=left;spacingLeft=10;strokeColor=none;fontColor=#FFFFFF;" parent="v1w6xJLIwrtz22bP0FQ9-3" vertex="1">
        <mxGeometry width="180" height="30" as="geometry" />
      </mxCell>
      <mxCell id="v1w6xJLIwrtz22bP0FQ9-5" value="Software System" style="shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;fillColor=#3162AF;top=0;left=0;bottom=0;right=0;overflow=hidden;pointerEvents=1;align=left;spacingLeft=10;fontColor=#FFFFFF;" parent="v1w6xJLIwrtz22bP0FQ9-3" vertex="1">
        <mxGeometry y="30" width="180" height="30" as="geometry" />
      </mxCell>
      <mxCell id="v1w6xJLIwrtz22bP0FQ9-6" value="Container" style="shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;fillColor=#52A2D8;top=0;left=0;bottom=0;right=0;overflow=hidden;pointerEvents=1;align=left;spacingLeft=10;fontColor=#FFFFFF;" parent="v1w6xJLIwrtz22bP0FQ9-3" vertex="1">
        <mxGeometry y="60" width="180" height="30" as="geometry" />
      </mxCell>
      <mxCell id="v1w6xJLIwrtz22bP0FQ9-7" value="Component" style="shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;fillColor=#7CBEF1;top=0;left=0;bottom=0;right=0;overflow=hidden;pointerEvents=1;align=left;spacingLeft=10;fontColor=#FFFFFF;" parent="v1w6xJLIwrtz22bP0FQ9-3" vertex="1">
        <mxGeometry y="90" width="180" height="30" as="geometry" />
      </mxCell>
      <mxCell id="v1w6xJLIwrtz22bP0FQ9-8" value="External Person" style="shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;fillColor=#6B6477;top=0;left=0;bottom=0;right=0;overflow=hidden;pointerEvents=1;align=left;spacingLeft=10;fontColor=#FFFFFF;" parent="v1w6xJLIwrtz22bP0FQ9-3" vertex="1">
        <mxGeometry y="120" width="180" height="30" as="geometry" />
      </mxCell>
      <mxCell id="v1w6xJLIwrtz22bP0FQ9-9" value="External Software System" style="shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;fillColor=#8B8496;top=0;left=0;bottom=0;right=0;overflow=hidden;pointerEvents=1;align=left;spacingLeft=10;fontColor=#FFFFFF;" parent="v1w6xJLIwrtz22bP0FQ9-3" vertex="1">
        <mxGeometry y="150" width="180" height="30" as="geometry" />
      </mxCell>
      <object placeholders="1" c4Name="System name" c4Type="Software System" c4Description="Description of software system." label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#cccccc&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;" id="v1w6xJLIwrtz22bP0FQ9-13">
        <mxCell style="rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#1061B0;fontColor=#ffffff;align=center;arcSize=10;strokeColor=#0D5091;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];" parent="1" vertex="1">
          <mxGeometry x="40" y="280" width="240" height="120" as="geometry" />
        </mxCell>
      </object>
      <object placeholders="1" c4Name="External system name" c4Type="Software System" c4Description="The internal Microsoft&#xa;Exchange e-mail system." label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#cccccc&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;" id="v1w6xJLIwrtz22bP0FQ9-14">
        <mxCell style="rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#8C8496;fontColor=#ffffff;align=center;arcSize=10;strokeColor=#736782;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];" parent="1" vertex="1">
          <mxGeometry x="440" y="280" width="240" height="120" as="geometry" />
        </mxCell>
      </object>
      <object placeholders="1" c4Type="Relationship" c4Description="Uses" label="&lt;div style=&quot;text-align: left&quot;&gt;&lt;div style=&quot;text-align: center&quot;&gt;&lt;b&gt;%c4Description%&lt;/b&gt;&lt;/div&gt;" id="v1w6xJLIwrtz22bP0FQ9-15">
        <mxCell style="endArrow=blockThin;html=1;fontSize=10;fontColor=#404040;strokeWidth=1;endFill=1;strokeColor=#828282;elbow=vertical;metaEdit=1;endSize=14;startSize=14;jumpStyle=arc;jumpSize=16;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0.75;entryY=0;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="v1w6xJLIwrtz22bP0FQ9-1" target="v1w6xJLIwrtz22bP0FQ9-13" edge="1">
          <mxGeometry width="240" relative="1" as="geometry">
            <mxPoint x="30" y="520" as="sourcePoint" />
            <mxPoint x="270" y="520" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </object>
      <object placeholders="1" c4Type="Relationship" c4Description="Sends e-mails to" label="&lt;div style=&quot;text-align: left&quot;&gt;&lt;div style=&quot;text-align: center&quot;&gt;&lt;b&gt;%c4Description%&lt;/b&gt;&lt;/div&gt;" id="v1w6xJLIwrtz22bP0FQ9-16">
        <mxCell style="endArrow=blockThin;html=1;fontSize=10;fontColor=#404040;strokeWidth=1;endFill=1;strokeColor=#828282;elbow=vertical;metaEdit=1;endSize=14;startSize=14;jumpStyle=arc;jumpSize=16;rounded=0;exitX=0.25;exitY=0;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="v1w6xJLIwrtz22bP0FQ9-14" target="v1w6xJLIwrtz22bP0FQ9-1" edge="1">
          <mxGeometry width="240" relative="1" as="geometry">
            <mxPoint x="310" y="230" as="sourcePoint" />
            <mxPoint x="300" y="220" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </object>
      <object placeholders="1" c4Name="Mainframe Banking&#xa;System" c4Type="Software System" c4Description="Stores all of the core banking&#xa;information." label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#cccccc&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;" id="v1w6xJLIwrtz22bP0FQ9-17">
        <mxCell style="rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#8C8496;fontColor=#ffffff;align=center;arcSize=10;strokeColor=#736782;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];" parent="1" vertex="1">
          <mxGeometry x="40" y="520" width="240" height="120" as="geometry" />
        </mxCell>
      </object>
      <object placeholders="1" c4Type="Relationship" c4Description="Uses" label="&lt;div style=&quot;text-align: left&quot;&gt;&lt;div style=&quot;text-align: center&quot;&gt;&lt;b&gt;%c4Description%&lt;/b&gt;&lt;/div&gt;" id="v1w6xJLIwrtz22bP0FQ9-18">
        <mxCell style="endArrow=blockThin;html=1;fontSize=10;fontColor=#404040;strokeWidth=1;endFill=1;strokeColor=#828282;elbow=vertical;metaEdit=1;endSize=14;startSize=14;jumpStyle=arc;jumpSize=16;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="v1w6xJLIwrtz22bP0FQ9-13" target="v1w6xJLIwrtz22bP0FQ9-17" edge="1">
          <mxGeometry width="240" relative="1" as="geometry">
            <mxPoint x="350" y="250" as="sourcePoint" />
            <mxPoint x="278" y="290" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </object>
      <object placeholders="1" c4Type="Relationship" c4Technology="SMTP" c4Description="Sends e-mails" label="&lt;div style=&quot;text-align: left&quot;&gt;&lt;div style=&quot;text-align: center&quot;&gt;&lt;b&gt;%c4Description%&lt;/b&gt;&lt;/div&gt;&lt;div style=&quot;text-align: center&quot;&gt;[%c4Technology%]&lt;/div&gt;&lt;/div&gt;" id="v1w6xJLIwrtz22bP0FQ9-19">
        <mxCell style="endArrow=blockThin;html=1;fontSize=10;fontColor=#404040;strokeWidth=1;endFill=1;strokeColor=#828282;elbow=vertical;metaEdit=1;endSize=14;startSize=14;jumpStyle=arc;jumpSize=16;rounded=0;edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="v1w6xJLIwrtz22bP0FQ9-13" target="v1w6xJLIwrtz22bP0FQ9-14" edge="1">
          <mxGeometry width="240" relative="1" as="geometry">
            <mxPoint x="290" y="450" as="sourcePoint" />
            <mxPoint x="530" y="450" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </object>
    </root>
  </mxGraphModel>
</diagram>
</mxfile>
`
}
