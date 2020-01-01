## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file lecture_notes.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_328 = Integer(328); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_344 = Integer(344); _sage_const_241 = Integer(241); _sage_const_29 = Integer(29); _sage_const_310 = Integer(310); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_25 = Integer(25); _sage_const_63 = Integer(63); _sage_const_113 = Integer(113); _sage_const_291 = Integer(291); _sage_const_68 = Integer(68); _sage_const_297 = Integer(297); _sage_const_239 = Integer(239); _sage_const_230 = Integer(230); _sage_const_316 = Integer(316); _sage_const_236 = Integer(236); _sage_const_245 = Integer(245); _sage_const_234 = Integer(234); _sage_const_258 = Integer(258); _sage_const_334 = Integer(334); _sage_const_338 = Integer(338); _sage_const_250 = Integer(250); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_320 = Integer(320); _sage_const_89 = Integer(89); _sage_const_109 = Integer(109); _sage_const_126 = Integer(126); _sage_const_124 = Integer(124); _sage_const_283 = Integer(283); _sage_const_91 = Integer(91); _sage_const_103 = Integer(103); _sage_const_106 = Integer(106); _sage_const_94 = Integer(94); _sage_const_225 = Integer(225); _sage_const_301 = Integer(301)## This file (lecture_notes.sagetex.sage) was *autogenerated* from lecture_notes.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('lecture_notes', version='2019/11/14 v3.4', version_check=True)
try:
 _st_.current_tex_line = _sage_const_11 
 _st_.doctest(_sage_const_0 , r"""
    sage: type(ZZ)
  
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_13 )
try:
 _st_.current_tex_line = _sage_const_25 
 _st_.doctest(_sage_const_1 , r"""
    sage: a,b = ZZ(4), 4
    sage: type(a) == type(b)
    sage: a == b
  
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_29 )
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.doctest(_sage_const_2 , r"""
    sage: 2/3
    sage: type(2/3)
    sage: 1/1
    sage: type(1/1)
  
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_68 )
try:
 _st_.current_tex_line = _sage_const_21 
 _st_.doctest(_sage_const_3 , r"""
    sage: def divides0(a,b):
    ....:     return (a/b).is_integer()
    sage: divides0(5,2)
    sage: divides0(6,3)
  
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_26 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.doctest(_sage_const_4 , r"""
  sage: k = 15
  ....: P = Poset((Set([2..k]), lambda a,b: b % a == 0))
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_106 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.plot(_sage_const_0 , format='png', _p_=P.plot(talk=True))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_124 
 _st_.doctest(_sage_const_5 , r"""
    sage: len(P.cover_relations_graph().edges())
  
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_230 
 _st_.doctest(_sage_const_6 , r"""
  sage: P1 = plot(x/log(x), (2, 200), scale='semilogy', \
  ....:     fill=lambda x: prime_pi(x),fillcolor='red')
  ....: P2 = plot(1.13*log(x), (2, 200), \
  ....:     fill=lambda x: nth_prime(x)/floor(x), fillcolor='red')
  ....: P = graphics_array([P1, P2])
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_236 )
try:
 _st_.current_tex_line = _sage_const_239 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=P,figsize=[_sage_const_8 ,_sage_const_4 ])
except:
 _st_.goboom(_sage_const_239 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.doctest(_sage_const_7 , r"""
  sage: P  = points([(k,euler_phi(k)) for k in range(1,1001)])
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=P)
except:
 _st_.goboom(_sage_const_94 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.doctest(_sage_const_8 , r"""
  sage: def make_code_tree(C):
  ....:     G = DiGraph()
  ....:     for c in C:
  ....:         prev = ''
  ....:         for i in range(1,len(c)+1):
  ....:             G.add_edge(prev, c[0:i], c[i-1])
  ....:             prev = c[0:i]
  ....:     return G
  sage: C = {'1011', '1100', '0110', '1110', '1010', '0101', '101'}
  sage: G = make_code_tree(C)
  sage: d = {'#00FF00': [v for v in G.vertices() if v not in C],
  ....:      '#FF0000': list(C)}
  ....: GP = G.plot(layout='tree', vertex_size=2000,
  ....:             vertex_color=d, edge_labels=True)
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.plot(_sage_const_3 , format='png', _p_=GP, figsize=_sage_const_10 )
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_225 
 _st_.doctest(_sage_const_9 , r"""
  sage: abc = ['A', 'B', 'C', 'D', 'E']
  ....: num = [ 16,   8,   7,   6,   3]
  ....: s = sum(num)
  ....: P = [(k/s).n(digits=3) for k in num]
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_230 )
try:
 _st_.current_tex_line = _sage_const_234 
 _st_.inline(_sage_const_10 , latex(table([abc, num, P], header_row=True, header_column=["ch", "db", "$p_i$"], frame=True)))
except:
 _st_.goboom(_sage_const_234 )
try:
 _st_.current_tex_line = _sage_const_241 
 _st_.doctest(_sage_const_11 , r"""
  sage: ell = [ceil(-log(p, 2)) for p in P]
  ....: sc = [(floor(sum(P[0:i]) << ell[i])).binary().rjust(ell[i],'0')
  ....:       for i in range(len(abc))]
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_245 )
try:
 _st_.current_tex_line = _sage_const_250 
 _st_.inline(_sage_const_12 , latex(table([abc, P, ell, sc], header_row=True, header_column=["ch", "$p_i$", "$\ell _i$", "code"], frame=True)))
except:
 _st_.goboom(_sage_const_250 )
try:
 _st_.current_tex_line = _sage_const_258 
 _st_.doctest(_sage_const_13 , r"""
  sage: G = DiGraph()
  ....: maxdepth = 4
  ....: fc = ['' for a in abc]
  ....: def split(u, v, parent, depth, code):
  ....:     if maxdepth <= depth:
  ....:         return
  ....:     if u >= v:
  ....:         fc[u] = code;
  ....:         return
  ....:     i, j = u, v
  ....:     rp, lp = P[i], P[j]
  ....:     rc, lc = abc[i], abc[j]
  ....:     while i+1 < j:
  ....:         if rp < lp:
  ....:             i += 1
  ....:             rp, rc = rp+P[i], rc+abc[i]
  ....:         else:
  ....:             j -= 1
  ....:             lp, lc = lp+P[j], lc+abc[j]
  ....:     rc, lc = rc + '\n' + str(rp), lc + '\n' + str(lp)
  ....:     split(u, i, rc, depth+1, code+'0')
  ....:     G.add_edge(parent, rc, '0')
  ....:     split(j, v, lc, depth+1, code+'1')
  ....:     G.add_edge(parent, lc, '1')
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_283 )
try:
 _st_.current_tex_line = _sage_const_291 
 _st_.doctest(_sage_const_14 , r"""
  sage: maxdepth=1
  ....: G = DiGraph()
  ....: split(0, len(abc)-1, '', 0, '')
  ....: GP = G.plot(layout='tree', edge_labels=True,
  ....:             vertex_size=4000, figsize=3, vertex_color='white')
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_297 )
try:
 _st_.current_tex_line = _sage_const_301 
 _st_.plot(_sage_const_4 , format='png', _p_=GP)
except:
 _st_.goboom(_sage_const_301 )
try:
 _st_.current_tex_line = _sage_const_310 
 _st_.doctest(_sage_const_15 , r"""
  sage: maxdepth=2
  ....: G = DiGraph()
  ....: split(0, len(abc)-1, '', 0, '')
  ....: GP = G.plot(layout='tree', edge_labels=True,
  ....:             vertex_size=4000, figsize=5, vertex_color='white')
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_316 )
try:
 _st_.current_tex_line = _sage_const_320 
 _st_.plot(_sage_const_5 , format='png', _p_=GP)
except:
 _st_.goboom(_sage_const_320 )
try:
 _st_.current_tex_line = _sage_const_328 
 _st_.doctest(_sage_const_16 , r"""
  sage: maxdepth=4
  ....: G = DiGraph()
  ....: split(0, len(abc)-1, '', 0, '')
  ....: GP = G.plot(layout='tree', edge_labels=True,
  ....:             vertex_size=4000, figsize=7, vertex_color='white')
""", globals(), locals(), False)
except:
 _st_.goboom(_sage_const_334 )
try:
 _st_.current_tex_line = _sage_const_338 
 _st_.plot(_sage_const_6 , format='png', _p_=GP)
except:
 _st_.goboom(_sage_const_338 )
try:
 _st_.current_tex_line = _sage_const_344 
 _st_.inline(_sage_const_17 , latex(table([abc, P, fc], header_row=True, header_column=["ch", "$p_i$", "code"], frame=True)))
except:
 _st_.goboom(_sage_const_344 )
_st_.endofdoc()

