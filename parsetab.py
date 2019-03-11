
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CHAR CHARACTER COLON COMMA DIVIDE ELSE EQUALS FOR FUNCTION ID IF INT INTEGER LBRA LOGICAL LPAREN LSBRA MAIN MINUS NOT NUM NUMERIC OR PLUS PROGRAM RBRA READ RELOP RETURN RPAREN RSBRA SEMICOLON TIMES VAR VOID WRITEprograma : PROGRAM ID SEMICOLON programa2 programa3 mainprograma2 : vars programa2\n                | emptyprograma3 : func programa3\n                | emptymain :  MAIN LBRA mainvars main2 RBRAmain2 : estatuto main2\n                | emptymainvars : vars mainvars\n                | emptyvars : type idmv vars2 SEMICOLONvars2 : empty\n             | COMMA idmv vars2bloque : LBRA bloque2 RBRAbloque2 : empty\n               | estatuto bloque2type : BOOL\n            | CHAR\n            | INT\n            | NUMexlog : exlog2 expresion exlog3exlog2 : NOT\n              | emptyexlog3 : AND exlog\n              | OR exlog\n              | emptyexpresion : exp expresion2expresion2 : empty\n                  | RELOP expestatuto : estatuto2 SEMICOLONestatuto2 : condicion\n                | ciclo\n                | funccall\n                | asignacion\n                | read\n                | escritura\n                | returnasignacion : idmv EQUALS exlog SEMICOLONdata : NUMERIC\n            | CHARACTER\n            | LOGICAL\n            | INTEGER\n            | idmv\n            | funccallreturn : RETURN return2return2 : exlog\n               | empty idmvf : ID idmvf2idmvf2 : LSBRA exp RSBRA idmvf3\n              | LPAREN exp RPAREN\n              | emptyidmvf3 : LSBRA exp RSBRA\n              | emptyidmv : ID idmv2idmv2 : LSBRA exp RSBRA idmvf3\n              | emptyargs : type ID args2args2 : COMMA args\n              | emptyfunccall : ID LPAREN funccall2 RPARENfunccall2 : exp funccall3\n              | emptyfunccall3 : COMMA exp funccall3\n              | emptycondicion : IF LPAREN exlog RPAREN bloque condicion2condicion2 : ELSE bloque\n              | emptyexp : term exp2exp2 : empty\n            | PLUS exp\n            | MINUS expterm : factor term2term2 : empty\n             | TIMES term\n             | DIVIDE termfactor : LPAREN expresion RPAREN\n              | PLUS data\n              | MINUS data\n              | dataescritura : WRITE LPAREN interior RPARENinterior : expresion escritura2\n                | CHARACTER escritura2escritura2 : COMMA interior\n                  | emptyread : READ LPAREN read2 RPARENread2 : CHARACTER\n                | emptyfunc : FUNCTION functipo ID LPAREN funcargs RPAREN LBRA funcvars funcest RBRAfunctipo : type\n                | VOIDfuncargs : args\n                | emptyfuncest : estatuto funcest\n                | emptyfuncvars : vars funcvars\n                | emptyciclo : FOR LPAREN ciclo1 SEMICOLON exlog SEMICOLON asignacion RPAREN bloqueciclo1 : asignacion\n                | emptyempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,20,106,],[0,-1,-6,]),'ID':([2,8,9,10,11,12,23,24,25,28,30,32,34,39,40,42,50,51,52,58,59,62,63,68,70,86,87,91,92,102,108,109,110,111,113,116,117,118,125,128,140,147,152,156,157,159,160,161,165,171,173,179,180,],[3,19,-17,-18,-19,-20,33,-89,-90,19,49,-100,-11,49,49,49,82,-100,-10,49,49,49,49,49,82,-100,-9,120,49,49,-30,-100,19,-100,49,-23,49,-22,49,-23,-100,-100,49,-100,-100,82,-100,-96,82,82,-95,82,19,]),'SEMICOLON':([3,18,19,26,27,29,31,35,37,38,41,43,44,45,46,47,48,49,54,55,56,57,60,61,65,66,67,72,73,74,75,76,77,78,79,86,93,94,95,96,97,98,99,100,101,110,114,115,116,122,123,129,130,131,132,139,144,148,149,150,155,158,164,166,168,169,174,176,183,184,188,],[4,-100,-100,34,-12,-54,-56,-100,-100,-100,-79,-39,-40,-41,-42,-43,-44,-100,-13,-100,-68,-69,-72,-73,-100,-77,-78,108,-31,-32,-33,-34,-35,-36,-37,-100,-55,-53,-70,-71,-74,-75,-76,-27,-28,-100,-45,-46,-47,-29,-60,147,-98,-99,148,-100,-52,-38,-85,-80,-21,-26,-100,180,-24,-25,-65,-67,-66,-14,-97,]),'FUNCTION':([4,5,6,7,14,17,34,181,],[-100,16,-100,-3,16,-2,-11,-88,]),'MAIN':([4,5,6,7,13,14,15,17,22,34,181,],[-100,-100,-100,-3,21,-100,-5,-2,-4,-11,-88,]),'BOOL':([4,6,16,32,34,51,53,140,142,160,],[9,9,9,9,-11,9,9,9,9,9,]),'CHAR':([4,6,16,32,34,51,53,140,142,160,],[10,10,10,10,-11,10,10,10,10,10,]),'INT':([4,6,16,32,34,51,53,140,142,160,],[11,11,11,11,-11,11,11,11,11,11,]),'NUM':([4,6,16,32,34,51,53,140,142,160,],[12,12,12,12,-11,12,12,12,12,12,]),'VOID':([16,],[25,]),'COMMA':([18,19,29,31,35,37,38,41,43,44,45,46,47,48,49,55,56,57,60,61,65,66,67,93,94,95,96,97,98,99,100,101,104,120,122,123,137,138,144,145,],[28,-100,-54,-56,28,-100,-100,-79,-39,-40,-41,-42,-43,-44,-100,-100,-68,-69,-72,-73,-100,-77,-78,-55,-53,-70,-71,-74,-75,-76,-27,-28,125,142,-29,-60,152,152,-52,125,]),'LSBRA':([19,49,55,82,],[30,30,92,30,]),'EQUALS':([19,29,31,55,82,83,93,94,144,],[-100,-54,-56,-100,-100,111,-55,-53,-52,]),'LBRA':([21,119,146,175,187,],[32,140,165,165,165,]),'TIMES':([29,31,38,41,43,44,45,46,47,48,49,55,66,67,93,94,99,123,138,144,],[-54,-56,62,-79,-39,-40,-41,-42,-43,-44,-100,-100,-77,-78,-55,-53,-76,-60,-40,-52,]),'DIVIDE':([29,31,38,41,43,44,45,46,47,48,49,55,66,67,93,94,99,123,138,144,],[-54,-56,63,-79,-39,-40,-41,-42,-43,-44,-100,-100,-77,-78,-55,-53,-76,-60,-40,-52,]),'PLUS':([29,30,31,37,38,39,41,43,44,45,46,47,48,49,55,58,59,60,61,62,63,66,67,68,86,92,93,94,97,98,99,102,109,111,113,116,117,118,123,125,128,138,144,147,152,156,157,],[-54,40,-56,58,-100,40,-79,-39,-40,-41,-42,-43,-44,-100,-100,40,40,-72,-73,40,40,-77,-78,40,-100,40,-55,-53,-74,-75,-76,40,-100,-100,40,-23,40,-22,-60,40,-23,-40,-52,-100,40,-100,-100,]),'MINUS':([29,30,31,37,38,39,41,43,44,45,46,47,48,49,55,58,59,60,61,62,63,66,67,68,86,92,93,94,97,98,99,102,109,111,113,116,117,118,123,125,128,138,144,147,152,156,157,],[-54,42,-56,59,-100,42,-79,-39,-40,-41,-42,-43,-44,-100,-100,42,42,-72,-73,42,42,-77,-78,42,-100,42,-55,-53,-74,-75,-76,42,-100,-100,42,-23,42,-22,-60,42,-23,-40,-52,-100,42,-100,-100,]),'RSBRA':([29,31,36,37,38,41,43,44,45,46,47,48,49,55,56,57,60,61,66,67,93,94,95,96,97,98,99,121,123,144,],[-54,-56,55,-100,-100,-79,-39,-40,-41,-42,-43,-44,-100,-100,-68,-69,-72,-73,-77,-78,-55,-53,-70,-71,-74,-75,-76,144,-60,-52,]),'RELOP':([29,31,37,38,41,43,44,45,46,47,48,49,55,56,57,60,61,65,66,67,93,94,95,96,97,98,99,123,138,144,],[-54,-56,-100,-100,-79,-39,-40,-41,-42,-43,-44,-100,-100,-68,-69,-72,-73,102,-77,-78,-55,-53,-70,-71,-74,-75,-76,-60,-40,-52,]),'RPAREN':([29,31,37,38,41,43,44,45,46,47,48,49,53,55,56,57,60,61,64,65,66,67,68,88,89,90,93,94,95,96,97,98,99,100,101,103,104,105,112,120,122,123,124,126,127,133,134,135,136,137,138,139,141,143,144,145,148,151,153,154,155,158,162,163,167,168,169,186,],[-54,-56,-100,-100,-79,-39,-40,-41,-42,-43,-44,-100,-100,-100,-68,-69,-72,-73,99,-100,-77,-78,-100,119,-91,-92,-55,-53,-70,-71,-74,-75,-76,-27,-28,123,-100,-62,-100,-100,-29,-60,-61,-64,146,149,-86,-87,150,-100,-40,-100,-57,-59,-52,-100,-38,-81,-84,-82,-21,-26,-58,-63,-83,-24,-25,187,]),'AND':([29,31,37,38,41,43,44,45,46,47,48,49,55,56,57,60,61,65,66,67,93,94,95,96,97,98,99,100,101,122,123,139,144,],[-54,-56,-100,-100,-79,-39,-40,-41,-42,-43,-44,-100,-100,-68,-69,-72,-73,-100,-77,-78,-55,-53,-70,-71,-74,-75,-76,-27,-28,-29,-60,156,-52,]),'OR':([29,31,37,38,41,43,44,45,46,47,48,49,55,56,57,60,61,65,66,67,93,94,95,96,97,98,99,100,101,122,123,139,144,],[-54,-56,-100,-100,-79,-39,-40,-41,-42,-43,-44,-100,-100,-68,-69,-72,-73,-100,-77,-78,-55,-53,-70,-71,-74,-75,-76,-27,-28,-29,-60,157,-52,]),'LPAREN':([30,33,39,49,58,59,62,63,68,80,81,82,84,85,86,92,102,109,111,113,116,117,118,125,128,147,152,156,157,],[39,53,39,68,39,39,39,39,39,109,110,68,112,113,-100,39,39,-100,-100,39,-23,39,-22,39,-23,-100,39,-100,-100,]),'NUMERIC':([30,39,40,42,58,59,62,63,68,86,92,102,109,111,113,116,117,118,125,128,147,152,156,157,],[43,43,43,43,43,43,43,43,43,-100,43,43,-100,-100,43,-23,43,-22,43,-23,-100,43,-100,-100,]),'CHARACTER':([30,39,40,42,58,59,62,63,68,86,92,102,109,111,112,113,116,117,118,125,128,147,152,156,157,],[44,44,44,44,44,44,44,44,44,-100,44,44,-100,-100,134,138,-23,44,-22,44,-23,-100,138,-100,-100,]),'LOGICAL':([30,39,40,42,58,59,62,63,68,86,92,102,109,111,113,116,117,118,125,128,147,152,156,157,],[45,45,45,45,45,45,45,45,45,-100,45,45,-100,-100,45,-23,45,-22,45,-23,-100,45,-100,-100,]),'INTEGER':([30,39,40,42,58,59,62,63,68,86,92,102,109,111,113,116,117,118,125,128,147,152,156,157,],[46,46,46,46,46,46,46,46,46,-100,46,46,-100,-100,46,-23,46,-22,46,-23,-100,46,-100,-100,]),'IF':([32,34,50,51,52,70,87,108,140,159,160,161,165,171,173,179,],[-100,-11,80,-100,-10,80,-9,-30,-100,80,-100,-96,80,80,-95,80,]),'FOR':([32,34,50,51,52,70,87,108,140,159,160,161,165,171,173,179,],[-100,-11,81,-100,-10,81,-9,-30,-100,81,-100,-96,81,81,-95,81,]),'READ':([32,34,50,51,52,70,87,108,140,159,160,161,165,171,173,179,],[-100,-11,84,-100,-10,84,-9,-30,-100,84,-100,-96,84,84,-95,84,]),'WRITE':([32,34,50,51,52,70,87,108,140,159,160,161,165,171,173,179,],[-100,-11,85,-100,-10,85,-9,-30,-100,85,-100,-96,85,85,-95,85,]),'RETURN':([32,34,50,51,52,70,87,108,140,159,160,161,165,171,173,179,],[-100,-11,86,-100,-10,86,-9,-30,-100,86,-100,-96,86,86,-95,86,]),'RBRA':([32,34,50,51,52,69,70,71,87,107,108,140,159,160,161,165,170,171,172,173,177,178,179,182,185,],[-100,-11,-100,-100,-10,106,-100,-8,-9,-7,-30,-100,-100,-100,-96,-100,181,-100,-94,-95,184,-15,-100,-93,-16,]),'NOT':([86,109,111,147,156,157,],[118,118,118,118,118,118,]),'ELSE':([164,184,],[175,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'programa2':([4,6,],[5,17,]),'vars':([4,6,32,51,140,160,],[6,6,51,51,160,160,]),'empty':([4,5,6,14,18,19,32,35,37,38,49,50,51,53,55,65,68,70,82,86,104,109,110,111,112,120,137,138,139,140,145,147,156,157,159,160,164,165,171,179,],[7,15,7,15,27,31,52,27,57,61,31,71,52,90,94,101,105,71,31,116,126,128,131,128,135,143,153,153,158,161,126,128,128,128,172,161,176,178,172,178,]),'type':([4,6,16,32,51,53,140,142,160,],[8,8,24,8,8,91,8,91,8,]),'programa3':([5,14,],[13,22,]),'func':([5,14,],[14,14,]),'idmv':([8,28,30,39,40,42,50,58,59,62,63,68,70,92,102,110,113,117,125,152,159,165,171,179,180,],[18,35,47,47,47,47,83,47,47,47,47,47,83,47,47,83,47,47,47,47,83,83,83,83,83,]),'main':([13,],[20,]),'functipo':([16,],[23,]),'vars2':([18,35,],[26,54,]),'idmv2':([19,49,82,],[29,29,29,]),'exp':([30,39,58,59,68,92,102,113,117,125,152,],[36,65,95,96,104,121,122,65,65,145,65,]),'term':([30,39,58,59,62,63,68,92,102,113,117,125,152,],[37,37,37,37,97,98,37,37,37,37,37,37,37,]),'factor':([30,39,58,59,62,63,68,92,102,113,117,125,152,],[38,38,38,38,38,38,38,38,38,38,38,38,38,]),'data':([30,39,40,42,58,59,62,63,68,92,102,113,117,125,152,],[41,41,66,67,41,41,41,41,41,41,41,41,41,41,41,]),'funccall':([30,39,40,42,50,58,59,62,63,68,70,92,102,113,117,125,152,159,165,171,179,],[48,48,48,48,75,48,48,48,48,48,75,48,48,48,48,48,48,75,75,75,75,]),'mainvars':([32,51,],[50,87,]),'exp2':([37,],[56,]),'term2':([38,],[60,]),'expresion':([39,113,117,152,],[64,137,139,137,]),'main2':([50,70,],[69,107,]),'estatuto':([50,70,159,165,171,179,],[70,70,171,179,171,179,]),'estatuto2':([50,70,159,165,171,179,],[72,72,72,72,72,72,]),'condicion':([50,70,159,165,171,179,],[73,73,73,73,73,73,]),'ciclo':([50,70,159,165,171,179,],[74,74,74,74,74,74,]),'asignacion':([50,70,110,159,165,171,179,180,],[76,76,130,76,76,76,76,186,]),'read':([50,70,159,165,171,179,],[77,77,77,77,77,77,]),'escritura':([50,70,159,165,171,179,],[78,78,78,78,78,78,]),'return':([50,70,159,165,171,179,],[79,79,79,79,79,79,]),'funcargs':([53,],[88,]),'args':([53,142,],[89,162,]),'idmvf3':([55,],[93,]),'expresion2':([65,],[100,]),'funccall2':([68,],[103,]),'return2':([86,],[114,]),'exlog':([86,109,111,147,156,157,],[115,127,132,166,168,169,]),'exlog2':([86,109,111,147,156,157,],[117,117,117,117,117,117,]),'funccall3':([104,145,],[124,163,]),'ciclo1':([110,],[129,]),'read2':([112,],[133,]),'interior':([113,152,],[136,167,]),'args2':([120,],[141,]),'escritura2':([137,138,],[151,154,]),'exlog3':([139,],[155,]),'funcvars':([140,160,],[159,173,]),'bloque':([146,175,187,],[164,183,188,]),'funcest':([159,171,],[170,182,]),'condicion2':([164,],[174,]),'bloque2':([165,179,],[177,185,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID SEMICOLON programa2 programa3 main','programa',6,'p_programa_start','eva_lex.py',118),
  ('programa2 -> vars programa2','programa2',2,'p_program2','eva_lex.py',121),
  ('programa2 -> empty','programa2',1,'p_program2','eva_lex.py',122),
  ('programa3 -> func programa3','programa3',2,'p_programa3','eva_lex.py',125),
  ('programa3 -> empty','programa3',1,'p_programa3','eva_lex.py',126),
  ('main -> MAIN LBRA mainvars main2 RBRA','main',5,'p_main','eva_lex.py',137),
  ('main2 -> estatuto main2','main2',2,'p_main2','eva_lex.py',140),
  ('main2 -> empty','main2',1,'p_main2','eva_lex.py',141),
  ('mainvars -> vars mainvars','mainvars',2,'p_mainvars','eva_lex.py',144),
  ('mainvars -> empty','mainvars',1,'p_mainvars','eva_lex.py',145),
  ('vars -> type idmv vars2 SEMICOLON','vars',4,'p_vars','eva_lex.py',165),
  ('vars2 -> empty','vars2',1,'p_vars2','eva_lex.py',168),
  ('vars2 -> COMMA idmv vars2','vars2',3,'p_vars2','eva_lex.py',169),
  ('bloque -> LBRA bloque2 RBRA','bloque',3,'p_bloque','eva_lex.py',174),
  ('bloque2 -> empty','bloque2',1,'p_bloque2','eva_lex.py',177),
  ('bloque2 -> estatuto bloque2','bloque2',2,'p_bloque2','eva_lex.py',178),
  ('type -> BOOL','type',1,'p_type','eva_lex.py',182),
  ('type -> CHAR','type',1,'p_type','eva_lex.py',183),
  ('type -> INT','type',1,'p_type','eva_lex.py',184),
  ('type -> NUM','type',1,'p_type','eva_lex.py',185),
  ('exlog -> exlog2 expresion exlog3','exlog',3,'p_exlog','eva_lex.py',190),
  ('exlog2 -> NOT','exlog2',1,'p_exlog2','eva_lex.py',193),
  ('exlog2 -> empty','exlog2',1,'p_exlog2','eva_lex.py',194),
  ('exlog3 -> AND exlog','exlog3',2,'p_exlog3','eva_lex.py',197),
  ('exlog3 -> OR exlog','exlog3',2,'p_exlog3','eva_lex.py',198),
  ('exlog3 -> empty','exlog3',1,'p_exlog3','eva_lex.py',199),
  ('expresion -> exp expresion2','expresion',2,'p_expresion','eva_lex.py',204),
  ('expresion2 -> empty','expresion2',1,'p_expresion2','eva_lex.py',206),
  ('expresion2 -> RELOP exp','expresion2',2,'p_expresion2','eva_lex.py',207),
  ('estatuto -> estatuto2 SEMICOLON','estatuto',2,'p_estatuto','eva_lex.py',211),
  ('estatuto2 -> condicion','estatuto2',1,'p_estatuto2','eva_lex.py',214),
  ('estatuto2 -> ciclo','estatuto2',1,'p_estatuto2','eva_lex.py',215),
  ('estatuto2 -> funccall','estatuto2',1,'p_estatuto2','eva_lex.py',216),
  ('estatuto2 -> asignacion','estatuto2',1,'p_estatuto2','eva_lex.py',217),
  ('estatuto2 -> read','estatuto2',1,'p_estatuto2','eva_lex.py',218),
  ('estatuto2 -> escritura','estatuto2',1,'p_estatuto2','eva_lex.py',219),
  ('estatuto2 -> return','estatuto2',1,'p_estatuto2','eva_lex.py',220),
  ('asignacion -> idmv EQUALS exlog SEMICOLON','asignacion',4,'p_asignacion','eva_lex.py',224),
  ('data -> NUMERIC','data',1,'p_data','eva_lex.py',228),
  ('data -> CHARACTER','data',1,'p_data','eva_lex.py',229),
  ('data -> LOGICAL','data',1,'p_data','eva_lex.py',230),
  ('data -> INTEGER','data',1,'p_data','eva_lex.py',231),
  ('data -> idmv','data',1,'p_data','eva_lex.py',232),
  ('data -> funccall','data',1,'p_data','eva_lex.py',233),
  ('return -> RETURN return2','return',2,'p_return','eva_lex.py',237),
  ('return2 -> exlog','return2',1,'p_return2','eva_lex.py',240),
  ('return2 -> empty','return2',1,'p_return2','eva_lex.py',241),
  ('idmvf -> ID idmvf2','idmvf',2,'p_idmvf','eva_lex.py',245),
  ('idmvf2 -> LSBRA exp RSBRA idmvf3','idmvf2',4,'p_idmvf2','eva_lex.py',249),
  ('idmvf2 -> LPAREN exp RPAREN','idmvf2',3,'p_idmvf2','eva_lex.py',250),
  ('idmvf2 -> empty','idmvf2',1,'p_idmvf2','eva_lex.py',251),
  ('idmvf3 -> LSBRA exp RSBRA','idmvf3',3,'p_idmvf3','eva_lex.py',254),
  ('idmvf3 -> empty','idmvf3',1,'p_idmvf3','eva_lex.py',255),
  ('idmv -> ID idmv2','idmv',2,'p_idmv','eva_lex.py',259),
  ('idmv2 -> LSBRA exp RSBRA idmvf3','idmv2',4,'p_idmv2','eva_lex.py',263),
  ('idmv2 -> empty','idmv2',1,'p_idmv2','eva_lex.py',264),
  ('args -> type ID args2','args',3,'p_args','eva_lex.py',268),
  ('args2 -> COMMA args','args2',2,'p_args2','eva_lex.py',271),
  ('args2 -> empty','args2',1,'p_args2','eva_lex.py',272),
  ('funccall -> ID LPAREN funccall2 RPAREN','funccall',4,'p_funccall','eva_lex.py',276),
  ('funccall2 -> exp funccall3','funccall2',2,'p_funccall2','eva_lex.py',279),
  ('funccall2 -> empty','funccall2',1,'p_funccall2','eva_lex.py',280),
  ('funccall3 -> COMMA exp funccall3','funccall3',3,'p_funccall3','eva_lex.py',283),
  ('funccall3 -> empty','funccall3',1,'p_funccall3','eva_lex.py',284),
  ('condicion -> IF LPAREN exlog RPAREN bloque condicion2','condicion',6,'p_condicion','eva_lex.py',291),
  ('condicion2 -> ELSE bloque','condicion2',2,'p_condicion2','eva_lex.py',294),
  ('condicion2 -> empty','condicion2',1,'p_condicion2','eva_lex.py',295),
  ('exp -> term exp2','exp',2,'p_exp','eva_lex.py',299),
  ('exp2 -> empty','exp2',1,'p_exp2','eva_lex.py',302),
  ('exp2 -> PLUS exp','exp2',2,'p_exp2','eva_lex.py',303),
  ('exp2 -> MINUS exp','exp2',2,'p_exp2','eva_lex.py',304),
  ('term -> factor term2','term',2,'p_term','eva_lex.py',308),
  ('term2 -> empty','term2',1,'p_term2','eva_lex.py',311),
  ('term2 -> TIMES term','term2',2,'p_term2','eva_lex.py',312),
  ('term2 -> DIVIDE term','term2',2,'p_term2','eva_lex.py',313),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','eva_lex.py',316),
  ('factor -> PLUS data','factor',2,'p_factor','eva_lex.py',317),
  ('factor -> MINUS data','factor',2,'p_factor','eva_lex.py',318),
  ('factor -> data','factor',1,'p_factor','eva_lex.py',319),
  ('escritura -> WRITE LPAREN interior RPAREN','escritura',4,'p_escritura','eva_lex.py',330),
  ('interior -> expresion escritura2','interior',2,'p_interior','eva_lex.py',333),
  ('interior -> CHARACTER escritura2','interior',2,'p_interior','eva_lex.py',334),
  ('escritura2 -> COMMA interior','escritura2',2,'p_escritura2','eva_lex.py',337),
  ('escritura2 -> empty','escritura2',1,'p_escritura2','eva_lex.py',338),
  ('read -> READ LPAREN read2 RPAREN','read',4,'p_read','eva_lex.py',341),
  ('read2 -> CHARACTER','read2',1,'p_read2','eva_lex.py',344),
  ('read2 -> empty','read2',1,'p_read2','eva_lex.py',345),
  ('func -> FUNCTION functipo ID LPAREN funcargs RPAREN LBRA funcvars funcest RBRA','func',10,'p_func','eva_lex.py',348),
  ('functipo -> type','functipo',1,'p_functipo','eva_lex.py',351),
  ('functipo -> VOID','functipo',1,'p_functipo','eva_lex.py',352),
  ('funcargs -> args','funcargs',1,'p_funcargs','eva_lex.py',355),
  ('funcargs -> empty','funcargs',1,'p_funcargs','eva_lex.py',356),
  ('funcest -> estatuto funcest','funcest',2,'p_funcEst','eva_lex.py',359),
  ('funcest -> empty','funcest',1,'p_funcEst','eva_lex.py',360),
  ('funcvars -> vars funcvars','funcvars',2,'p_funcvars','eva_lex.py',363),
  ('funcvars -> empty','funcvars',1,'p_funcvars','eva_lex.py',364),
  ('ciclo -> FOR LPAREN ciclo1 SEMICOLON exlog SEMICOLON asignacion RPAREN bloque','ciclo',9,'p_ciclo','eva_lex.py',367),
  ('ciclo1 -> asignacion','ciclo1',1,'p_ciclo1','eva_lex.py',370),
  ('ciclo1 -> empty','ciclo1',1,'p_ciclo1','eva_lex.py',371),
  ('empty -> <empty>','empty',0,'p_empty','eva_lex.py',374),
]
