
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMENT SYN_FONT_P_LBRACE SYN_FONT_M_LBRACE SYN_HTML_LBRACE SYN_WIKI_LBRACE SYN_HIGHLIGHT_LBRACE SYN_FOLDING_LBRACE SYN_FONT_COLOR_LBRACE SYNTAX_BRACE TRI_LBRACE TRI_RBRACE MACRO PH_6 PH_5 PH_4 PH_3 PH_2 PH_1 P_6 P_5 P_4 P_3 P_2 P_1 TEXT_BOLD_ITALIC TEXT_BOLD TEXT_ITALIC TEXT_CANCEL1 TEXT_CANCEL2 TEXT_UNDERLINE TEXT_UPPER TEXT_LOWER TABLE HEX_COLOR NAME_COLOR NAME NUMBERwikidoc  : wikidoc expression\n                | expressionexpression : paragraph\n                  | text_effect\n                  | no_markup_expression\n                  | font_p_expression\n                  | font_m_expression\n                  | html_expression\n                  | wiki_expression\n                  | highlight_expression\n                  | folding_expression\n                  | font_color_expression\n                  | brace_expressionno_markup_expression : SYNTAX_BRACEbrace_expression : TRI_LBRACE expression TRI_RBRACEfont_p_expression : SYN_FONT_P_LBRACE NUMBER expression TRI_RBRACEfont_m_expression : SYN_FONT_M_LBRACE NUMBER expression TRI_RBRACEhtml_expression : SYN_HTML_LBRACE expression TRI_RBRACEwiki_expression : SYN_WIKI_LBRACE expression TRI_RBRACEhighlight_expression : SYN_HIGHLIGHT_LBRACE expression TRI_RBRACEfolding_expression : SYN_FOLDING_LBRACE expression TRI_RBRACEfont_color_expression : SYN_FONT_COLOR_LBRACE NAME_COLOR expression TRI_RBRACE\n                            | SYN_FONT_COLOR_LBRACE HEX_COLOR expression TRI_RBRACEparagraph  : PH_6\n                  | PH_5\n                  | PH_4\n                  | PH_3\n                  | PH_2\n                  | PH_1\n                  | P_6\n                  | P_5\n                  | P_4\n                  | P_3\n                  | P_2\n                  | P_1text_effect : TEXT_BOLD_ITALIC\n                    | TEXT_BOLD\n                    | TEXT_ITALIC\n                    | TEXT_CANCEL1\n                    | TEXT_CANCEL2\n                    | TEXT_UNDERLINE\n                    | TEXT_UPPER\n                    | TEXT_LOWER'
    
_lr_action_items = {'PH_6':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[14,14,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,14,14,14,14,14,-1,14,14,14,14,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'PH_5':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[15,15,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,15,15,15,15,15,-1,15,15,15,15,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'PH_4':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[16,16,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,16,16,16,16,16,-1,16,16,16,16,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'PH_3':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[17,17,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,17,17,17,17,17,-1,17,17,17,17,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'PH_2':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[18,18,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,18,18,18,18,18,-1,18,18,18,18,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'PH_1':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[19,19,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,19,19,19,19,19,-1,19,19,19,19,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'P_6':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[20,20,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,20,20,20,20,20,-1,20,20,20,20,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'P_5':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[21,21,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,21,21,21,21,21,-1,21,21,21,21,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'P_4':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[22,22,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,22,22,22,22,22,-1,22,22,22,22,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'P_3':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[23,23,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,23,23,23,23,23,-1,23,23,23,23,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'P_2':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[24,24,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,24,24,24,24,24,-1,24,24,24,24,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'P_1':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[25,25,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,25,25,25,25,25,-1,25,25,25,25,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TEXT_BOLD_ITALIC':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[26,26,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,26,26,26,26,26,-1,26,26,26,26,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TEXT_BOLD':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[27,27,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,27,27,27,27,27,-1,27,27,27,27,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TEXT_ITALIC':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[28,28,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,28,28,28,28,28,-1,28,28,28,28,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TEXT_CANCEL1':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[29,29,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,29,29,29,29,29,-1,29,29,29,29,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TEXT_CANCEL2':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[30,30,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,30,30,30,30,30,-1,30,30,30,30,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TEXT_UNDERLINE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[31,31,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,31,31,31,31,31,-1,31,31,31,31,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TEXT_UPPER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[32,32,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,32,32,32,32,32,-1,32,32,32,32,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TEXT_LOWER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[33,33,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,33,33,33,33,33,-1,33,33,33,33,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'SYNTAX_BRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[34,34,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,34,34,34,34,34,-1,34,34,34,34,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'SYN_FONT_P_LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[35,35,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,35,35,35,35,35,-1,35,35,35,35,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'SYN_FONT_M_LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[36,36,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,36,36,36,36,36,-1,36,36,36,36,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'SYN_HTML_LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[37,37,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,37,37,37,37,37,-1,37,37,37,37,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'SYN_WIKI_LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[38,38,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,38,38,38,38,38,-1,38,38,38,38,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'SYN_HIGHLIGHT_LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[39,39,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,39,39,39,39,39,-1,39,39,39,39,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'SYN_FOLDING_LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[40,40,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,40,40,40,40,40,-1,40,40,40,40,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'SYN_FONT_COLOR_LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[41,41,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,41,41,41,41,41,-1,41,41,41,41,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TRI_LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,50,51,55,56,57,58,61,62,63,64,65,],[42,42,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,42,42,42,42,42,-1,42,42,42,42,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,43,55,56,57,58,61,62,63,64,65,],[0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,-1,-18,-19,-20,-21,-15,-16,-17,-22,-23,]),'TRI_RBRACE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-14,55,56,57,58,61,62,63,-18,-19,-20,-21,64,65,-15,-16,-17,-22,-23,]),'NUMBER':([35,36,],[44,45,]),'NAME_COLOR':([41,],[50,]),'HEX_COLOR':([41,],[51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'wikidoc':([0,],[1,]),'expression':([0,1,37,38,39,40,42,44,45,50,51,],[2,43,46,47,48,49,52,53,54,59,60,]),'paragraph':([0,1,37,38,39,40,42,44,45,50,51,],[3,3,3,3,3,3,3,3,3,3,3,]),'text_effect':([0,1,37,38,39,40,42,44,45,50,51,],[4,4,4,4,4,4,4,4,4,4,4,]),'no_markup_expression':([0,1,37,38,39,40,42,44,45,50,51,],[5,5,5,5,5,5,5,5,5,5,5,]),'font_p_expression':([0,1,37,38,39,40,42,44,45,50,51,],[6,6,6,6,6,6,6,6,6,6,6,]),'font_m_expression':([0,1,37,38,39,40,42,44,45,50,51,],[7,7,7,7,7,7,7,7,7,7,7,]),'html_expression':([0,1,37,38,39,40,42,44,45,50,51,],[8,8,8,8,8,8,8,8,8,8,8,]),'wiki_expression':([0,1,37,38,39,40,42,44,45,50,51,],[9,9,9,9,9,9,9,9,9,9,9,]),'highlight_expression':([0,1,37,38,39,40,42,44,45,50,51,],[10,10,10,10,10,10,10,10,10,10,10,]),'folding_expression':([0,1,37,38,39,40,42,44,45,50,51,],[11,11,11,11,11,11,11,11,11,11,11,]),'font_color_expression':([0,1,37,38,39,40,42,44,45,50,51,],[12,12,12,12,12,12,12,12,12,12,12,]),'brace_expression':([0,1,37,38,39,40,42,44,45,50,51,],[13,13,13,13,13,13,13,13,13,13,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> wikidoc","S'",1,None,None,None),
  ('wikidoc -> wikidoc expression','wikidoc',2,'p_wikidoc','parsing_kiwi.py',299),
  ('wikidoc -> expression','wikidoc',1,'p_wikidoc','parsing_kiwi.py',300),
  ('expression -> paragraph','expression',1,'p_expression','parsing_kiwi.py',303),
  ('expression -> text_effect','expression',1,'p_expression','parsing_kiwi.py',304),
  ('expression -> no_markup_expression','expression',1,'p_expression','parsing_kiwi.py',305),
  ('expression -> font_p_expression','expression',1,'p_expression','parsing_kiwi.py',306),
  ('expression -> font_m_expression','expression',1,'p_expression','parsing_kiwi.py',307),
  ('expression -> html_expression','expression',1,'p_expression','parsing_kiwi.py',308),
  ('expression -> wiki_expression','expression',1,'p_expression','parsing_kiwi.py',309),
  ('expression -> highlight_expression','expression',1,'p_expression','parsing_kiwi.py',310),
  ('expression -> folding_expression','expression',1,'p_expression','parsing_kiwi.py',311),
  ('expression -> font_color_expression','expression',1,'p_expression','parsing_kiwi.py',312),
  ('expression -> brace_expression','expression',1,'p_expression','parsing_kiwi.py',313),
  ('no_markup_expression -> SYNTAX_BRACE','no_markup_expression',1,'p_no_markup_expression','parsing_kiwi.py',316),
  ('brace_expression -> TRI_LBRACE expression TRI_RBRACE','brace_expression',3,'p_brace_expression','parsing_kiwi.py',321),
  ('font_p_expression -> SYN_FONT_P_LBRACE NUMBER expression TRI_RBRACE','font_p_expression',4,'p_font_p_expression','parsing_kiwi.py',326),
  ('font_m_expression -> SYN_FONT_M_LBRACE NUMBER expression TRI_RBRACE','font_m_expression',4,'p_font_m_expression','parsing_kiwi.py',331),
  ('html_expression -> SYN_HTML_LBRACE expression TRI_RBRACE','html_expression',3,'p_html_expression','parsing_kiwi.py',336),
  ('wiki_expression -> SYN_WIKI_LBRACE expression TRI_RBRACE','wiki_expression',3,'p_wiki_expression','parsing_kiwi.py',341),
  ('highlight_expression -> SYN_HIGHLIGHT_LBRACE expression TRI_RBRACE','highlight_expression',3,'p_highlight_expression','parsing_kiwi.py',346),
  ('folding_expression -> SYN_FOLDING_LBRACE expression TRI_RBRACE','folding_expression',3,'p_folding_expression','parsing_kiwi.py',351),
  ('font_color_expression -> SYN_FONT_COLOR_LBRACE NAME_COLOR expression TRI_RBRACE','font_color_expression',4,'p_font_color_expression','parsing_kiwi.py',356),
  ('font_color_expression -> SYN_FONT_COLOR_LBRACE HEX_COLOR expression TRI_RBRACE','font_color_expression',4,'p_font_color_expression','parsing_kiwi.py',357),
  ('paragraph -> PH_6','paragraph',1,'p_paragraph','parsing_kiwi.py',367),
  ('paragraph -> PH_5','paragraph',1,'p_paragraph','parsing_kiwi.py',368),
  ('paragraph -> PH_4','paragraph',1,'p_paragraph','parsing_kiwi.py',369),
  ('paragraph -> PH_3','paragraph',1,'p_paragraph','parsing_kiwi.py',370),
  ('paragraph -> PH_2','paragraph',1,'p_paragraph','parsing_kiwi.py',371),
  ('paragraph -> PH_1','paragraph',1,'p_paragraph','parsing_kiwi.py',372),
  ('paragraph -> P_6','paragraph',1,'p_paragraph','parsing_kiwi.py',373),
  ('paragraph -> P_5','paragraph',1,'p_paragraph','parsing_kiwi.py',374),
  ('paragraph -> P_4','paragraph',1,'p_paragraph','parsing_kiwi.py',375),
  ('paragraph -> P_3','paragraph',1,'p_paragraph','parsing_kiwi.py',376),
  ('paragraph -> P_2','paragraph',1,'p_paragraph','parsing_kiwi.py',377),
  ('paragraph -> P_1','paragraph',1,'p_paragraph','parsing_kiwi.py',378),
  ('text_effect -> TEXT_BOLD_ITALIC','text_effect',1,'p_text_effect','parsing_kiwi.py',383),
  ('text_effect -> TEXT_BOLD','text_effect',1,'p_text_effect','parsing_kiwi.py',384),
  ('text_effect -> TEXT_ITALIC','text_effect',1,'p_text_effect','parsing_kiwi.py',385),
  ('text_effect -> TEXT_CANCEL1','text_effect',1,'p_text_effect','parsing_kiwi.py',386),
  ('text_effect -> TEXT_CANCEL2','text_effect',1,'p_text_effect','parsing_kiwi.py',387),
  ('text_effect -> TEXT_UNDERLINE','text_effect',1,'p_text_effect','parsing_kiwi.py',388),
  ('text_effect -> TEXT_UPPER','text_effect',1,'p_text_effect','parsing_kiwi.py',389),
  ('text_effect -> TEXT_LOWER','text_effect',1,'p_text_effect','parsing_kiwi.py',390),
]
