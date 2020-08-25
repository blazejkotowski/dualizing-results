from jinja2 import Environment, FileSystemLoader
import os
import random

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'layouts')
env = Environment(loader = FileSystemLoader(templates_dir))

cpd_layout = env.get_template('choose_preferred_dualization.html')
# [question_number,original_pattern_sc_id,dualizations_playlist_sc_id]
cpd_data = [[1,877854508,1112897323],
            [2,877855105,1112898085],
            [3,877855996,1112898910],
            [4,877857532,1112900773],
            [5,877858285,1112901385],
            [6,877858966,1112902051],
            [7,877859617,1112902813],
            [8,877860205,1112903380],
            [9,877860808,1112903989],
            [10,877861549,1112904625],
            [11,877862104,1112905288],
            [12,877862863,1112906182],
            [13,877863505,1112907025],
            [14,877864027,1112907709],
            [15,877864930,1112908396],
            [16,877865395,1112909230],
            [17,877866184,1112909950],
            [18,877867393,1112911195],
            [19,877868413,1112912074],
            [20,877869082,1112912704]]
A='A'
B='B'
C='C'
D='D'
cpd_mapping = [[A,B,C,D],
               [A,D,C,B],
               [D,A,B,C],
               [C,A,D,B],
               [D,C,A,B],
               [A,D,B,C],
               [B,C,D,A],
               [D,C,A,B],
               [D,C,A,B],
               [A,B,C,D],
               [C,D,A,B],
               [B,D,A,C],
               [A,C,B,D],
               [C,D,B,A],
               [C,D,B,A],
               [C,B,A,D],
               [A,B,D,C],
               [B,A,C,D],
               [B,A,D,C],
               [A,C,D,B]]
for mapping, (qid, orig_scid, playlist_scid) in zip(cpd_mapping, cpd_data):
  filename = os.path.join(root, 'choose_preferred_dualization', f"{qid}.html")
  with open(filename, 'w') as fh:
    fh.write(cpd_layout.render(
      orig_scid=orig_scid,
      playlist_scid=playlist_scid,
      qid=qid,
      experiments_num=len(cpd_data),
      mapping=mapping
      ))

mdo_data = [[2,877450831,1112511610],
            [3,877452508,1112513206],
            [4,877453819,1112514400],
            [5,877456030,1112516107],
            [6,877456609,1112517778],
            [7,877458115,1112519008],
            [8,877459513,1112520496],
            [9,877460542,1112521429],
            [10,877461652,1112522410],
            [11,877462792,1112523742],
            [12,877464064,1112524774],
            [13,877465180,1112525698],
            [14,877466155,1112526832],
            [15,877467307,1112527750],
            [16,877468342,1112528635],
            [17,877469509,1112530159],
            [18,877471345,1112531380],
            [19,877472698,1112532526],
            [20,877474018,1112533468]]

mdo_mapping = [[C,A,B],
               [A,B,C],
               [C,A,B],
               [B,A,C],
               [B,C,A],
               [C,B,A],
               [A,C,B],
               [B,A,C],
               [B,C,A],
               [B,A,C],
               [B,C,A],
               [A,B,C],
               [C,B,A],
               [C,B,A],
               [B,A,C],
               [B,C,A],
               [A,C,B],
               [A,B,C],
               [B,A,C],
               [A,B,C]]

mdo_layout = env.get_template('match_dualization_with_original.html')
for mapping, (qid, orig_scid, playlist_scid) in zip(mdo_mapping, mdo_data):
  filename = os.path.join(root, 'match_dualization_with_original', f"{qid}.html")

  with open(filename, 'w') as fh:
    fh.write(mdo_layout.render(
      orig_scid=orig_scid,
      playlist_scid=playlist_scid,
      qid=qid,
      experiments_num=len(mdo_data),
      mapping=mapping
      ))