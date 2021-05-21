%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-m
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1361:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knuth-lib.tar.xz
Source1362:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knuth-local.tar.xz
Source1473:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jneurosci.tar.xz
Source1474:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jneurosci.doc.tar.xz
Source1475:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jurabib.tar.xz
Source1476:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jurabib.doc.tar.xz
Source1478:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ksfh_nat.tar.xz
Source1676:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jmn.tar.xz
Source1913:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iwona.tar.xz
Source1914:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iwona.doc.tar.xz
Source1915:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jablantile.tar.xz
Source1916:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jablantile.doc.tar.xz
Source1917:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jamtimes.tar.xz
Source1918:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jamtimes.doc.tar.xz
Source1919:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/junicode.tar.xz
Source1920:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/junicode.doc.tar.xz
Source1921:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kixfont.tar.xz
Source1922:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kixfont.doc.tar.xz
Source1924:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kpfonts.tar.xz
Source1925:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kpfonts.doc.tar.xz
Source1926:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kurier.tar.xz
Source1927:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kurier.doc.tar.xz
Source2349:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kastrup.tar.xz
Source2350:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kastrup.doc.tar.xz
Source2402:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jura.tar.xz
Source2403:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jura.doc.tar.xz
Source2405:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/juraabbrev.tar.xz
Source2406:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/juraabbrev.doc.tar.xz
Source2408:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/juramisc.tar.xz
Source2409:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/juramisc.doc.tar.xz
Source2410:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jurarsp.tar.xz
Source2411:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jurarsp.doc.tar.xz
Source2621:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knuth.doc.tar.xz
Source2764:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/koma-script-examples.doc.tar.xz
Source2818:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kerkis.tar.xz
Source2819:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kerkis.doc.tar.xz
Source2861:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/itnumpar.tar.xz
Source2862:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/itnumpar.doc.tar.xz
Source2879:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/japanese-otf.tar.xz
Source2880:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/japanese-otf.doc.tar.xz
Source2882:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/japanese-otf-uptex.tar.xz
Source2883:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/japanese-otf-uptex.doc.tar.xz
Source2888:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jsclasses.tar.xz
Source2889:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jsclasses.doc.tar.xz
Source2918:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kotex-oblivoir.tar.xz
Source2919:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kotex-oblivoir.doc.tar.xz
Source2923:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kotex-utf.tar.xz
Source2924:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kotex-utf.doc.tar.xz
Source2925:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kotex-plain.tar.xz
Source2926:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kotex-plain.doc.tar.xz
Source3038:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jknapltx.tar.xz
Source3039:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jknapltx.doc.tar.xz
Source3040:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/koma-script.tar.xz
Source3188:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knitting.tar.xz
Source3189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knitting.doc.tar.xz
Source3190:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knittingpattern.tar.xz
Source3191:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knittingpattern.doc.tar.xz
Source4331:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iso.tar.xz
Source4332:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iso.doc.tar.xz
Source4334:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iso10303.tar.xz
Source4335:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iso10303.doc.tar.xz
Source4337:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isodate.tar.xz
Source4338:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isodate.doc.tar.xz
Source4340:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isodoc.tar.xz
Source4341:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isodoc.doc.tar.xz
Source4343:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isonums.tar.xz
Source4344:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isonums.doc.tar.xz
Source4345:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isorot.tar.xz
Source4346:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isorot.doc.tar.xz
Source4348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isotope.tar.xz
Source4349:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isotope.doc.tar.xz
Source4351:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/issuulinks.tar.xz
Source4352:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/issuulinks.doc.tar.xz
Source4354:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iwhdp.tar.xz
Source4355:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iwhdp.doc.tar.xz
Source4356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jlabels.tar.xz
Source4357:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jlabels.doc.tar.xz
Source4358:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jslectureplanner.tar.xz
Source4359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jslectureplanner.doc.tar.xz
Source4360:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jumplines.tar.xz
Source4361:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jumplines.doc.tar.xz
Source4362:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jvlisting.tar.xz
Source4363:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jvlisting.doc.tar.xz
Source4365:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kantlipsum.tar.xz
Source4366:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kantlipsum.doc.tar.xz
Source4368:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kerntest.tar.xz
Source4369:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kerntest.doc.tar.xz
Source4371:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keycommand.tar.xz
Source4372:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keycommand.doc.tar.xz
Source4374:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keyreader.tar.xz
Source4375:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keyreader.doc.tar.xz
Source4376:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keystroke.tar.xz
Source4377:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keystroke.doc.tar.xz
Source4378:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keyval2e.tar.xz
Source4379:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keyval2e.doc.tar.xz
Source4380:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kix.tar.xz
Source4381:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kix.doc.tar.xz
Source4382:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/koma-moderncvclassic.tar.xz
Source4383:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/koma-moderncvclassic.doc.tar.xz
Source4384:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/koma-script-sfs.tar.xz
Source4385:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/koma-script-sfs.doc.tar.xz
Source4386:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/komacv.tar.xz
Source4387:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/komacv.doc.tar.xz
Source4389:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ktv-texdata.tar.xz
Source4390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ktv-texdata.doc.tar.xz
Source5855:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isomath.tar.xz
Source5856:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isomath.doc.tar.xz
Source6093:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/js-misc.tar.xz
Source6094:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/js-misc.doc.tar.xz
Source6414:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jmlr.tar.xz
Source6415:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jmlr.doc.tar.xz
Source6417:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jpsj.tar.xz
Source6418:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jpsj.doc.tar.xz
Source6419:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kdgdocs.tar.xz
Source6420:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kdgdocs.doc.tar.xz
Source6422:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kluwer.tar.xz
Source6423:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kluwer.doc.tar.xz
Source6687:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/karnaugh.tar.xz
Source6688:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/karnaugh.doc.tar.xz
Source6689:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/karnaughmap.tar.xz
Source6690:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/karnaughmap.doc.tar.xz
Source7391:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jacow.tar.xz
Source7392:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jacow.doc.tar.xz
Source7393:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keyvaltable.tar.xz
Source7394:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keyvaltable.doc.tar.xz
Source7396:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ksp-thesis.tar.xz
Source7397:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ksp-thesis.doc.tar.xz
Source7790:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iscram.tar.xz
Source7791:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iscram.doc.tar.xz
Source7792:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isopt.tar.xz
Source7793:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/isopt.doc.tar.xz
Source7794:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/istgame.tar.xz
Source7795:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/istgame.doc.tar.xz
Source7798:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jlreq.tar.xz
Source7799:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jlreq.doc.tar.xz
Source7800:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keyfloat.tar.xz
Source7801:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/keyfloat.doc.tar.xz
Source7802:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knowledge.tar.xz
Source7803:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/knowledge.doc.tar.xz
Source7804:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/komacv-rg.tar.xz
Source7805:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/komacv-rg.doc.tar.xz
Source7806:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ku-template.tar.xz
Source7807:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ku-template.doc.tar.xz
Source8180:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jnuexam.tar.xz
Source8181:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jnuexam.doc.tar.xz
Source8182:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kanaparser.tar.xz
Source8183:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kanaparser.doc.tar.xz
Source8184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/karnaugh-map.tar.xz
Source8185:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/karnaugh-map.doc.tar.xz
Source8186:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kurdishlipsum.tar.xz
Source8187:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kurdishlipsum.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-knuth-lib
Provides:       tex-knuth-lib = %{tl_version}
License:        Knuth
Summary:        A small library of MetaFont sources
Version:        svn35820.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(logo10.tfm) = %{tl_version}, tex(logo8.tfm) = %{tl_version}
Provides:       tex(logo9.tfm) = %{tl_version}, tex(logobf10.tfm) = %{tl_version}
Provides:       tex(logosl10.tfm) = %{tl_version}, tex(manfnt.tfm) = %{tl_version}
Provides:       tex(null.tex) = %{tl_version}, tex(manmac.tex) = %{tl_version}
Provides:       tex(mftmac.tex) = %{tl_version}, tex(story.tex) = %{tl_version}
Provides:       tex(testfont.tex) = %{tl_version}, tex(webmac.tex) = %{tl_version}

%description -n texlive-knuth-lib
A collection of miscellaneous MetaFont source, including the
means to generate the logo font that is used for MetaFont and
MetaPost.

%package -n texlive-knuth-local
Provides:       tex-knuth-local = %{tl_version}
License:        Knuth
Summary:        Knuth's local information
Version:        svn38627

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(domino.tfm) = %{tl_version}, tex(random.tfm) = %{tl_version}
Provides:       tex(snfont.tfm) = %{tl_version}, tex(xepsf.tex) = %{tl_version}

%description -n texlive-knuth-local
A collection of experimental programs and developments based
on, or complementary to, the matter in his distribution
directories.

%package -n texlive-jneurosci
Provides:       tex-jneurosci = %{tl_version}
License:        LPPL
Summary:        BibTeX style for the Journal of Neuroscience
Version:        svn17346.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(jneurosci.sty) = %{tl_version}

%description -n texlive-jneurosci
This is a slightly modified version of the namedplus style,
which fully conforms with the Journal of Neuroscience citation
style. It should be characterised as an author-date citation
style; a BibTeX style and a LaTeX package are provided.

%package -n texlive-jneurosci-doc
Summary:        Documentation for jneurosci
Version:        svn17346.1.00

Provides:       tex-jneurosci-doc
AutoReqProv:    No

%description -n texlive-jneurosci-doc
Documentation for jneurosci

%package -n texlive-jurabib
Provides:       tex-jurabib = %{tl_version}
License:        GPL+
Summary:        Extended BibTeX citation support for the humanities and legal texts
Version:        svn15878.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(keyval.sty), tex(url.sty)
Requires:       tex(array.sty)
Provides:       tex(dajbbib.ldf) = %{tl_version}, tex(dejbbib.ldf) = %{tl_version}
Provides:       tex(dujbbib.ldf) = %{tl_version}, tex(enjbbib.ldf) = %{tl_version}
Provides:       tex(fijbbib.ldf) = %{tl_version}, tex(frjbbib.ldf) = %{tl_version}
Provides:       tex(itjbbib.ldf) = %{tl_version}, tex(jblong.cfg) = %{tl_version}
Provides:       tex(jurabib.cfg) = %{tl_version}, tex(jurabib.sty) = %{tl_version}
Provides:       tex(nojbbib.ldf) = %{tl_version}, tex(ptjbbib.ldf) = %{tl_version}
Provides:       tex(spjbbib.ldf) = %{tl_version}

%description -n texlive-jurabib
This package enables automated citation with BibTeX for legal
studies and the humanities. In addition, the package provides
commands for specifying editors in a commentary in a convenient
way. Simplified formatting of the citation as well as the
bibliography entry is also provided. It is possible to display
the (short) title of a work only if an authors is cited with
multiple works. Giving a full citation in the text, conforming
to the bibliography entry, is supported. Several options are
provided which might be of special interest for those outside
legal studies--for instance, displaying multiple full
citations. In addition, the format of last names and first
names of authors may be changed easily. Cross references to
other footnotes are possible. Language dependent handling of
bibliography entries is possible by the special language field.

%package -n texlive-jurabib-doc
Summary:        Documentation for jurabib
Version:        svn15878.0.6

Provides:       tex-jurabib-doc
AutoReqProv:    No

%description -n texlive-jurabib-doc
Documentation for jurabib

%package -n texlive-ksfh_nat
Provides:       tex-ksfh_nat = %{tl_version}
License:        LPPL 1.3
Summary:        BibTeX style for KSFH Munich
Version:        svn24825.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-ksfh_nat
The package supports bibliographies as standard for KSFH
(Katholische Stiftungsfachhochschule) Munich. BibTeX entries in
article, book, inbook, incollection and misc formats are
supported.

%package -n texlive-jmn
Provides:       tex-jmn = %{tl_version}
License:        LPPL
Summary:        jmn package
Version:        svn45751
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(hans.enc) = %{tl_version}, tex(hans.map) = %{tl_version}
Provides:       tex(hans-sh.tfm) = %{tl_version}, tex(hans.tfm) = %{tl_version}
Provides:       tex(hans-sh.pfb) = %{tl_version}, tex(hans.pfb) = %{tl_version}

%description -n texlive-jmn
jmn package

%package -n texlive-iwona
Provides:       tex-iwona = %{tl_version}
License:        GFSL
Summary:        A two-element sans-serif font
Version:        svn19611.0.995b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(cs-iwona-sc.enc) = %{tl_version}, tex(cs-iwona.enc) = %{tl_version}
Provides:       tex(ec-iwona-sc.enc) = %{tl_version}, tex(ec-iwona.enc) = %{tl_version}
Provides:       tex(ex-iwona.enc) = %{tl_version}, tex(greek-iwona.enc) = %{tl_version}
Provides:       tex(l7x-iwona-sc.enc) = %{tl_version}, tex(l7x-iwona.enc) = %{tl_version}
Provides:       tex(mi-iwona.enc) = %{tl_version}, tex(qx-iwona-sc.enc) = %{tl_version}
Provides:       tex(qx-iwona.enc) = %{tl_version}, tex(rm-iwona-sc.enc) = %{tl_version}
Provides:       tex(rm-iwona.enc) = %{tl_version}, tex(sy-iwona.enc) = %{tl_version}
Provides:       tex(t2a-iwona.enc) = %{tl_version}, tex(t2b-iwona.enc) = %{tl_version}
Provides:       tex(t2c-iwona.enc) = %{tl_version}, tex(t5-iwona-sc.enc) = %{tl_version}
Provides:       tex(t5-iwona.enc) = %{tl_version}, tex(texnansi-iwona-sc.enc) = %{tl_version}
Provides:       tex(texnansi-iwona.enc) = %{tl_version}, tex(ts1-iwona.enc) = %{tl_version}
Provides:       tex(wncy-iwona.enc) = %{tl_version}, tex(iwona-cs.map) = %{tl_version}
Provides:       tex(iwona-ec.map) = %{tl_version}, tex(iwona-ex.map) = %{tl_version}
Provides:       tex(iwona-greek.map) = %{tl_version}, tex(iwona-l7x.map) = %{tl_version}
Provides:       tex(iwona-mi.map) = %{tl_version}, tex(iwona-qx.map) = %{tl_version}
Provides:       tex(iwona-rm.map) = %{tl_version}, tex(iwona-sy.map) = %{tl_version}
Provides:       tex(iwona-t2a.map) = %{tl_version}, tex(iwona-t2b.map) = %{tl_version}
Provides:       tex(iwona-t2c.map) = %{tl_version}, tex(iwona-t5.map) = %{tl_version}
Provides:       tex(iwona-texnansi.map) = %{tl_version}, tex(iwona-ts1.map) = %{tl_version}
Provides:       tex(iwona-wncy.map) = %{tl_version}, tex(iwona.map) = %{tl_version}
Provides:       tex(Iwona-Bold.otf) = %{tl_version}, tex(Iwona-BoldItalic.otf) = %{tl_version}
Provides:       tex(Iwona-Italic.otf) = %{tl_version}, tex(Iwona-Regular.otf) = %{tl_version}
Provides:       tex(IwonaCond-Bold.otf) = %{tl_version}, tex(IwonaCond-BoldItalic.otf) = %{tl_version}
Provides:       tex(IwonaCond-Italic.otf) = %{tl_version}
Provides:       tex(IwonaCond-Regular.otf) = %{tl_version}
Provides:       tex(IwonaCondHeavy-Italic.otf) = %{tl_version}
Provides:       tex(IwonaCondHeavy-Regular.otf) = %{tl_version}
Provides:       tex(IwonaCondLight-Italic.otf) = %{tl_version}
Provides:       tex(IwonaCondLight-Regular.otf) = %{tl_version}
Provides:       tex(IwonaCondMedium-Italic.otf) = %{tl_version}
Provides:       tex(IwonaCondMedium-Regular.otf) = %{tl_version}
Provides:       tex(IwonaHeavy-Italic.otf) = %{tl_version}
Provides:       tex(IwonaHeavy-Regular.otf) = %{tl_version}
Provides:       tex(IwonaLight-Italic.otf) = %{tl_version}
Provides:       tex(IwonaLight-Regular.otf) = %{tl_version}
Provides:       tex(IwonaMedium-Italic.otf) = %{tl_version}
Provides:       tex(IwonaMedium-Regular.otf) = %{tl_version}
Provides:       tex(cs-iwonab-sc.tfm) = %{tl_version}, tex(cs-iwonab.tfm) = %{tl_version}
Provides:       tex(cs-iwonabi-sc.tfm) = %{tl_version}, tex(cs-iwonabi.tfm) = %{tl_version}
Provides:       tex(cs-iwonacb-sc.tfm) = %{tl_version}, tex(cs-iwonacb.tfm) = %{tl_version}
Provides:       tex(cs-iwonacbi-sc.tfm) = %{tl_version}, tex(cs-iwonacbi.tfm) = %{tl_version}
Provides:       tex(cs-iwonach-sc.tfm) = %{tl_version}, tex(cs-iwonach.tfm) = %{tl_version}
Provides:       tex(cs-iwonachi-sc.tfm) = %{tl_version}, tex(cs-iwonachi.tfm) = %{tl_version}
Provides:       tex(cs-iwonacl-sc.tfm) = %{tl_version}, tex(cs-iwonacl.tfm) = %{tl_version}
Provides:       tex(cs-iwonacli-sc.tfm) = %{tl_version}, tex(cs-iwonacli.tfm) = %{tl_version}
Provides:       tex(cs-iwonacm-sc.tfm) = %{tl_version}, tex(cs-iwonacm.tfm) = %{tl_version}
Provides:       tex(cs-iwonacmi-sc.tfm) = %{tl_version}, tex(cs-iwonacmi.tfm) = %{tl_version}
Provides:       tex(cs-iwonacr-sc.tfm) = %{tl_version}, tex(cs-iwonacr.tfm) = %{tl_version}
Provides:       tex(cs-iwonacri-sc.tfm) = %{tl_version}, tex(cs-iwonacri.tfm) = %{tl_version}
Provides:       tex(cs-iwonah-sc.tfm) = %{tl_version}, tex(cs-iwonah.tfm) = %{tl_version}
Provides:       tex(cs-iwonahi-sc.tfm) = %{tl_version}, tex(cs-iwonahi.tfm) = %{tl_version}
Provides:       tex(cs-iwonal-sc.tfm) = %{tl_version}, tex(cs-iwonal.tfm) = %{tl_version}
Provides:       tex(cs-iwonali-sc.tfm) = %{tl_version}, tex(cs-iwonali.tfm) = %{tl_version}
Provides:       tex(cs-iwonam-sc.tfm) = %{tl_version}, tex(cs-iwonam.tfm) = %{tl_version}
Provides:       tex(cs-iwonami-sc.tfm) = %{tl_version}, tex(cs-iwonami.tfm) = %{tl_version}
Provides:       tex(cs-iwonar-sc.tfm) = %{tl_version}, tex(cs-iwonar.tfm) = %{tl_version}
Provides:       tex(cs-iwonari-sc.tfm) = %{tl_version}, tex(cs-iwonari.tfm) = %{tl_version}
Provides:       tex(ec-iwonab-sc.tfm) = %{tl_version}, tex(ec-iwonab.tfm) = %{tl_version}
Provides:       tex(ec-iwonabi-sc.tfm) = %{tl_version}, tex(ec-iwonabi.tfm) = %{tl_version}
Provides:       tex(ec-iwonacb-sc.tfm) = %{tl_version}, tex(ec-iwonacb.tfm) = %{tl_version}
Provides:       tex(ec-iwonacbi-sc.tfm) = %{tl_version}, tex(ec-iwonacbi.tfm) = %{tl_version}
Provides:       tex(ec-iwonach-sc.tfm) = %{tl_version}, tex(ec-iwonach.tfm) = %{tl_version}
Provides:       tex(ec-iwonachi-sc.tfm) = %{tl_version}, tex(ec-iwonachi.tfm) = %{tl_version}
Provides:       tex(ec-iwonacl-sc.tfm) = %{tl_version}, tex(ec-iwonacl.tfm) = %{tl_version}
Provides:       tex(ec-iwonacli-sc.tfm) = %{tl_version}, tex(ec-iwonacli.tfm) = %{tl_version}
Provides:       tex(ec-iwonacm-sc.tfm) = %{tl_version}, tex(ec-iwonacm.tfm) = %{tl_version}
Provides:       tex(ec-iwonacmi-sc.tfm) = %{tl_version}, tex(ec-iwonacmi.tfm) = %{tl_version}
Provides:       tex(ec-iwonacr-sc.tfm) = %{tl_version}, tex(ec-iwonacr.tfm) = %{tl_version}
Provides:       tex(ec-iwonacri-sc.tfm) = %{tl_version}, tex(ec-iwonacri.tfm) = %{tl_version}
Provides:       tex(ec-iwonah-sc.tfm) = %{tl_version}, tex(ec-iwonah.tfm) = %{tl_version}
Provides:       tex(ec-iwonahi-sc.tfm) = %{tl_version}, tex(ec-iwonahi.tfm) = %{tl_version}
Provides:       tex(ec-iwonal-sc.tfm) = %{tl_version}, tex(ec-iwonal.tfm) = %{tl_version}
Provides:       tex(ec-iwonali-sc.tfm) = %{tl_version}, tex(ec-iwonali.tfm) = %{tl_version}
Provides:       tex(ec-iwonam-sc.tfm) = %{tl_version}, tex(ec-iwonam.tfm) = %{tl_version}
Provides:       tex(ec-iwonami-sc.tfm) = %{tl_version}, tex(ec-iwonami.tfm) = %{tl_version}
Provides:       tex(ec-iwonar-sc.tfm) = %{tl_version}, tex(ec-iwonar.tfm) = %{tl_version}
Provides:       tex(ec-iwonari-sc.tfm) = %{tl_version}, tex(ec-iwonari.tfm) = %{tl_version}
Provides:       tex(ex-iwonab.tfm) = %{tl_version}, tex(ex-iwonacb.tfm) = %{tl_version}
Provides:       tex(ex-iwonach.tfm) = %{tl_version}, tex(ex-iwonacl.tfm) = %{tl_version}
Provides:       tex(ex-iwonacm.tfm) = %{tl_version}, tex(ex-iwonacr.tfm) = %{tl_version}
Provides:       tex(ex-iwonah.tfm) = %{tl_version}, tex(ex-iwonal.tfm) = %{tl_version}
Provides:       tex(ex-iwonam.tfm) = %{tl_version}, tex(ex-iwonar.tfm) = %{tl_version}
Provides:       tex(greek-iwonab.tfm) = %{tl_version}, tex(greek-iwonabi.tfm) = %{tl_version}
Provides:       tex(greek-iwonacb.tfm) = %{tl_version}, tex(greek-iwonacbi.tfm) = %{tl_version}
Provides:       tex(greek-iwonach.tfm) = %{tl_version}, tex(greek-iwonachi.tfm) = %{tl_version}
Provides:       tex(greek-iwonacl.tfm) = %{tl_version}, tex(greek-iwonacli.tfm) = %{tl_version}
Provides:       tex(greek-iwonacm.tfm) = %{tl_version}, tex(greek-iwonacmi.tfm) = %{tl_version}
Provides:       tex(greek-iwonacr.tfm) = %{tl_version}, tex(greek-iwonacri.tfm) = %{tl_version}
Provides:       tex(greek-iwonah.tfm) = %{tl_version}, tex(greek-iwonahi.tfm) = %{tl_version}
Provides:       tex(greek-iwonal.tfm) = %{tl_version}, tex(greek-iwonali.tfm) = %{tl_version}
Provides:       tex(greek-iwonam.tfm) = %{tl_version}, tex(greek-iwonami.tfm) = %{tl_version}
Provides:       tex(greek-iwonar.tfm) = %{tl_version}, tex(greek-iwonari.tfm) = %{tl_version}
Provides:       tex(l7x-iwonab-sc.tfm) = %{tl_version}, tex(l7x-iwonab.tfm) = %{tl_version}
Provides:       tex(l7x-iwonabi-sc.tfm) = %{tl_version}, tex(l7x-iwonabi.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacb-sc.tfm) = %{tl_version}, tex(l7x-iwonacb.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacbi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacbi.tfm) = %{tl_version}, tex(l7x-iwonach-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonach.tfm) = %{tl_version}, tex(l7x-iwonachi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonachi.tfm) = %{tl_version}, tex(l7x-iwonacl-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacl.tfm) = %{tl_version}, tex(l7x-iwonacli-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacli.tfm) = %{tl_version}, tex(l7x-iwonacm-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacm.tfm) = %{tl_version}, tex(l7x-iwonacmi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacmi.tfm) = %{tl_version}, tex(l7x-iwonacr-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacr.tfm) = %{tl_version}, tex(l7x-iwonacri-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonacri.tfm) = %{tl_version}, tex(l7x-iwonah-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonah.tfm) = %{tl_version}, tex(l7x-iwonahi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonahi.tfm) = %{tl_version}, tex(l7x-iwonal-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonal.tfm) = %{tl_version}, tex(l7x-iwonali-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonali.tfm) = %{tl_version}, tex(l7x-iwonam-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonam.tfm) = %{tl_version}, tex(l7x-iwonami-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonami.tfm) = %{tl_version}, tex(l7x-iwonar-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonar.tfm) = %{tl_version}, tex(l7x-iwonari-sc.tfm) = %{tl_version}
Provides:       tex(l7x-iwonari.tfm) = %{tl_version}, tex(mi-iwonabi.tfm) = %{tl_version}
Provides:       tex(mi-iwonacbi.tfm) = %{tl_version}, tex(mi-iwonachi.tfm) = %{tl_version}
Provides:       tex(mi-iwonacli.tfm) = %{tl_version}, tex(mi-iwonacmi.tfm) = %{tl_version}
Provides:       tex(mi-iwonacri.tfm) = %{tl_version}, tex(mi-iwonahi.tfm) = %{tl_version}
Provides:       tex(mi-iwonali.tfm) = %{tl_version}, tex(mi-iwonami.tfm) = %{tl_version}
Provides:       tex(mi-iwonari.tfm) = %{tl_version}, tex(qx-iwonab-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonab.tfm) = %{tl_version}, tex(qx-iwonabi-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonabi.tfm) = %{tl_version}, tex(qx-iwonacb-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonacb.tfm) = %{tl_version}, tex(qx-iwonacbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonacbi.tfm) = %{tl_version}, tex(qx-iwonach-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonach.tfm) = %{tl_version}, tex(qx-iwonachi-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonachi.tfm) = %{tl_version}, tex(qx-iwonacl-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonacl.tfm) = %{tl_version}, tex(qx-iwonacli-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonacli.tfm) = %{tl_version}, tex(qx-iwonacm-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonacm.tfm) = %{tl_version}, tex(qx-iwonacmi-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonacmi.tfm) = %{tl_version}, tex(qx-iwonacr-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonacr.tfm) = %{tl_version}, tex(qx-iwonacri-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonacri.tfm) = %{tl_version}, tex(qx-iwonah-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonah.tfm) = %{tl_version}, tex(qx-iwonahi-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonahi.tfm) = %{tl_version}, tex(qx-iwonal-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonal.tfm) = %{tl_version}, tex(qx-iwonali-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonali.tfm) = %{tl_version}, tex(qx-iwonam-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonam.tfm) = %{tl_version}, tex(qx-iwonami-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonami.tfm) = %{tl_version}, tex(qx-iwonar-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonar.tfm) = %{tl_version}, tex(qx-iwonari-sc.tfm) = %{tl_version}
Provides:       tex(qx-iwonari.tfm) = %{tl_version}, tex(rm-iwonab-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonab.tfm) = %{tl_version}, tex(rm-iwonabi-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonabi.tfm) = %{tl_version}, tex(rm-iwonacb-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonacb.tfm) = %{tl_version}, tex(rm-iwonacbi-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonacbi.tfm) = %{tl_version}, tex(rm-iwonach-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonach.tfm) = %{tl_version}, tex(rm-iwonachi-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonachi.tfm) = %{tl_version}, tex(rm-iwonacl-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonacl.tfm) = %{tl_version}, tex(rm-iwonacli-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonacli.tfm) = %{tl_version}, tex(rm-iwonacm-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonacm.tfm) = %{tl_version}, tex(rm-iwonacmi-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonacmi.tfm) = %{tl_version}, tex(rm-iwonacr-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonacr.tfm) = %{tl_version}, tex(rm-iwonacri-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonacri.tfm) = %{tl_version}, tex(rm-iwonah-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonah.tfm) = %{tl_version}, tex(rm-iwonahi-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonahi.tfm) = %{tl_version}, tex(rm-iwonal-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonal.tfm) = %{tl_version}, tex(rm-iwonali-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonali.tfm) = %{tl_version}, tex(rm-iwonam-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonam.tfm) = %{tl_version}, tex(rm-iwonami-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonami.tfm) = %{tl_version}, tex(rm-iwonar-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonar.tfm) = %{tl_version}, tex(rm-iwonari-sc.tfm) = %{tl_version}
Provides:       tex(rm-iwonari.tfm) = %{tl_version}, tex(sy-iwonabz.tfm) = %{tl_version}
Provides:       tex(sy-iwonacbz.tfm) = %{tl_version}, tex(sy-iwonachz.tfm) = %{tl_version}
Provides:       tex(sy-iwonaclz.tfm) = %{tl_version}, tex(sy-iwonacmz.tfm) = %{tl_version}
Provides:       tex(sy-iwonacrz.tfm) = %{tl_version}, tex(sy-iwonahz.tfm) = %{tl_version}
Provides:       tex(sy-iwonalz.tfm) = %{tl_version}, tex(sy-iwonamz.tfm) = %{tl_version}
Provides:       tex(sy-iwonarz.tfm) = %{tl_version}, tex(t2a-iwonab.tfm) = %{tl_version}
Provides:       tex(t2a-iwonabi.tfm) = %{tl_version}, tex(t2a-iwonacb.tfm) = %{tl_version}
Provides:       tex(t2a-iwonacbi.tfm) = %{tl_version}, tex(t2a-iwonach.tfm) = %{tl_version}
Provides:       tex(t2a-iwonachi.tfm) = %{tl_version}, tex(t2a-iwonacl.tfm) = %{tl_version}
Provides:       tex(t2a-iwonacli.tfm) = %{tl_version}, tex(t2a-iwonacm.tfm) = %{tl_version}
Provides:       tex(t2a-iwonacmi.tfm) = %{tl_version}, tex(t2a-iwonacr.tfm) = %{tl_version}
Provides:       tex(t2a-iwonacri.tfm) = %{tl_version}, tex(t2a-iwonah.tfm) = %{tl_version}
Provides:       tex(t2a-iwonahi.tfm) = %{tl_version}, tex(t2a-iwonal.tfm) = %{tl_version}
Provides:       tex(t2a-iwonali.tfm) = %{tl_version}, tex(t2a-iwonam.tfm) = %{tl_version}
Provides:       tex(t2a-iwonami.tfm) = %{tl_version}, tex(t2a-iwonar.tfm) = %{tl_version}
Provides:       tex(t2a-iwonari.tfm) = %{tl_version}, tex(t2b-iwonab.tfm) = %{tl_version}
Provides:       tex(t2b-iwonabi.tfm) = %{tl_version}, tex(t2b-iwonacb.tfm) = %{tl_version}
Provides:       tex(t2b-iwonacbi.tfm) = %{tl_version}, tex(t2b-iwonach.tfm) = %{tl_version}
Provides:       tex(t2b-iwonachi.tfm) = %{tl_version}, tex(t2b-iwonacl.tfm) = %{tl_version}
Provides:       tex(t2b-iwonacli.tfm) = %{tl_version}, tex(t2b-iwonacm.tfm) = %{tl_version}
Provides:       tex(t2b-iwonacmi.tfm) = %{tl_version}, tex(t2b-iwonacr.tfm) = %{tl_version}
Provides:       tex(t2b-iwonacri.tfm) = %{tl_version}, tex(t2b-iwonah.tfm) = %{tl_version}
Provides:       tex(t2b-iwonahi.tfm) = %{tl_version}, tex(t2b-iwonal.tfm) = %{tl_version}
Provides:       tex(t2b-iwonali.tfm) = %{tl_version}, tex(t2b-iwonam.tfm) = %{tl_version}
Provides:       tex(t2b-iwonami.tfm) = %{tl_version}, tex(t2b-iwonar.tfm) = %{tl_version}
Provides:       tex(t2b-iwonari.tfm) = %{tl_version}, tex(t2c-iwonab.tfm) = %{tl_version}
Provides:       tex(t2c-iwonabi.tfm) = %{tl_version}, tex(t2c-iwonacb.tfm) = %{tl_version}
Provides:       tex(t2c-iwonacbi.tfm) = %{tl_version}, tex(t2c-iwonach.tfm) = %{tl_version}
Provides:       tex(t2c-iwonachi.tfm) = %{tl_version}, tex(t2c-iwonacl.tfm) = %{tl_version}
Provides:       tex(t2c-iwonacli.tfm) = %{tl_version}, tex(t2c-iwonacm.tfm) = %{tl_version}
Provides:       tex(t2c-iwonacmi.tfm) = %{tl_version}, tex(t2c-iwonacr.tfm) = %{tl_version}
Provides:       tex(t2c-iwonacri.tfm) = %{tl_version}, tex(t2c-iwonah.tfm) = %{tl_version}
Provides:       tex(t2c-iwonahi.tfm) = %{tl_version}, tex(t2c-iwonal.tfm) = %{tl_version}
Provides:       tex(t2c-iwonali.tfm) = %{tl_version}, tex(t2c-iwonam.tfm) = %{tl_version}
Provides:       tex(t2c-iwonami.tfm) = %{tl_version}, tex(t2c-iwonar.tfm) = %{tl_version}
Provides:       tex(t2c-iwonari.tfm) = %{tl_version}, tex(t5-iwonab-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonab.tfm) = %{tl_version}, tex(t5-iwonabi-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonabi.tfm) = %{tl_version}, tex(t5-iwonacb-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonacb.tfm) = %{tl_version}, tex(t5-iwonacbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonacbi.tfm) = %{tl_version}, tex(t5-iwonach-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonach.tfm) = %{tl_version}, tex(t5-iwonachi-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonachi.tfm) = %{tl_version}, tex(t5-iwonacl-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonacl.tfm) = %{tl_version}, tex(t5-iwonacli-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonacli.tfm) = %{tl_version}, tex(t5-iwonacm-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonacm.tfm) = %{tl_version}, tex(t5-iwonacmi-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonacmi.tfm) = %{tl_version}, tex(t5-iwonacr-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonacr.tfm) = %{tl_version}, tex(t5-iwonacri-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonacri.tfm) = %{tl_version}, tex(t5-iwonah-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonah.tfm) = %{tl_version}, tex(t5-iwonahi-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonahi.tfm) = %{tl_version}, tex(t5-iwonal-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonal.tfm) = %{tl_version}, tex(t5-iwonali-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonali.tfm) = %{tl_version}, tex(t5-iwonam-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonam.tfm) = %{tl_version}, tex(t5-iwonami-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonami.tfm) = %{tl_version}, tex(t5-iwonar-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonar.tfm) = %{tl_version}, tex(t5-iwonari-sc.tfm) = %{tl_version}
Provides:       tex(t5-iwonari.tfm) = %{tl_version}, tex(texnansi-iwonab-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonab.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonabi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonabi.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacb.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacbi.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonach-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonach.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonachi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonachi.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacl-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacl.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacli-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacli.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacm-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacm.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacmi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacmi.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacr.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonacri.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonah-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonah.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonahi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonahi.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonal-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonal.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonali-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonali.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonam-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonam.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonami-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonami.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonar-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonar.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonari-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-iwonari.tfm) = %{tl_version}
Provides:       tex(ts1-iwonab.tfm) = %{tl_version}, tex(ts1-iwonabi.tfm) = %{tl_version}
Provides:       tex(ts1-iwonacb.tfm) = %{tl_version}, tex(ts1-iwonacbi.tfm) = %{tl_version}
Provides:       tex(ts1-iwonach.tfm) = %{tl_version}, tex(ts1-iwonachi.tfm) = %{tl_version}
Provides:       tex(ts1-iwonacl.tfm) = %{tl_version}, tex(ts1-iwonacli.tfm) = %{tl_version}
Provides:       tex(ts1-iwonacm.tfm) = %{tl_version}, tex(ts1-iwonacmi.tfm) = %{tl_version}
Provides:       tex(ts1-iwonacr.tfm) = %{tl_version}, tex(ts1-iwonacri.tfm) = %{tl_version}
Provides:       tex(ts1-iwonah.tfm) = %{tl_version}, tex(ts1-iwonahi.tfm) = %{tl_version}
Provides:       tex(ts1-iwonal.tfm) = %{tl_version}, tex(ts1-iwonali.tfm) = %{tl_version}
Provides:       tex(ts1-iwonam.tfm) = %{tl_version}, tex(ts1-iwonami.tfm) = %{tl_version}
Provides:       tex(ts1-iwonar.tfm) = %{tl_version}, tex(ts1-iwonari.tfm) = %{tl_version}
Provides:       tex(wncy-iwonab.tfm) = %{tl_version}, tex(wncy-iwonabi.tfm) = %{tl_version}
Provides:       tex(wncy-iwonacb.tfm) = %{tl_version}, tex(wncy-iwonacbi.tfm) = %{tl_version}
Provides:       tex(wncy-iwonach.tfm) = %{tl_version}, tex(wncy-iwonachi.tfm) = %{tl_version}
Provides:       tex(wncy-iwonacl.tfm) = %{tl_version}, tex(wncy-iwonacli.tfm) = %{tl_version}
Provides:       tex(wncy-iwonacm.tfm) = %{tl_version}, tex(wncy-iwonacmi.tfm) = %{tl_version}
Provides:       tex(wncy-iwonacr.tfm) = %{tl_version}, tex(wncy-iwonacri.tfm) = %{tl_version}
Provides:       tex(wncy-iwonah.tfm) = %{tl_version}, tex(wncy-iwonahi.tfm) = %{tl_version}
Provides:       tex(wncy-iwonal.tfm) = %{tl_version}, tex(wncy-iwonali.tfm) = %{tl_version}
Provides:       tex(wncy-iwonam.tfm) = %{tl_version}, tex(wncy-iwonami.tfm) = %{tl_version}
Provides:       tex(wncy-iwonar.tfm) = %{tl_version}, tex(wncy-iwonari.tfm) = %{tl_version}
Provides:       tex(iwonab.pfb) = %{tl_version}, tex(iwonabi.pfb) = %{tl_version}
Provides:       tex(iwonacb.pfb) = %{tl_version}, tex(iwonacbi.pfb) = %{tl_version}
Provides:       tex(iwonach.pfb) = %{tl_version}, tex(iwonachi.pfb) = %{tl_version}
Provides:       tex(iwonacl.pfb) = %{tl_version}, tex(iwonacli.pfb) = %{tl_version}
Provides:       tex(iwonacm.pfb) = %{tl_version}, tex(iwonacmi.pfb) = %{tl_version}
Provides:       tex(iwonacr.pfb) = %{tl_version}, tex(iwonacri.pfb) = %{tl_version}
Provides:       tex(iwonah.pfb) = %{tl_version}, tex(iwonahi.pfb) = %{tl_version}
Provides:       tex(iwonal.pfb) = %{tl_version}, tex(iwonali.pfb) = %{tl_version}
Provides:       tex(iwonam.pfb) = %{tl_version}, tex(iwonami.pfb) = %{tl_version}
Provides:       tex(iwonar.pfb) = %{tl_version}, tex(iwonari.pfb) = %{tl_version}
Provides:       tex(il2iwona.fd) = %{tl_version}, tex(il2iwonac.fd) = %{tl_version}
Provides:       tex(il2iwonal.fd) = %{tl_version}, tex(il2iwonalc.fd) = %{tl_version}
Provides:       tex(iwona.sty) = %{tl_version}, tex(l7xiwona.fd) = %{tl_version}
Provides:       tex(l7xiwonac.fd) = %{tl_version}, tex(l7xiwonal.fd) = %{tl_version}
Provides:       tex(l7xiwonalc.fd) = %{tl_version}, tex(ly1iwona.fd) = %{tl_version}
Provides:       tex(ly1iwonac.fd) = %{tl_version}, tex(ly1iwonal.fd) = %{tl_version}
Provides:       tex(ly1iwonalc.fd) = %{tl_version}, tex(omliwona.fd) = %{tl_version}
Provides:       tex(omliwonac.fd) = %{tl_version}, tex(omliwonal.fd) = %{tl_version}
Provides:       tex(omliwonalc.fd) = %{tl_version}, tex(omsiwona.fd) = %{tl_version}
Provides:       tex(omsiwonac.fd) = %{tl_version}, tex(omsiwonal.fd) = %{tl_version}
Provides:       tex(omsiwonalc.fd) = %{tl_version}, tex(omxiwona.fd) = %{tl_version}
Provides:       tex(omxiwonac.fd) = %{tl_version}, tex(omxiwonal.fd) = %{tl_version}
Provides:       tex(omxiwonalc.fd) = %{tl_version}, tex(ot1iwona.fd) = %{tl_version}
Provides:       tex(ot1iwonac.fd) = %{tl_version}, tex(ot1iwonacm.fd) = %{tl_version}
Provides:       tex(ot1iwonal.fd) = %{tl_version}, tex(ot1iwonalc.fd) = %{tl_version}
Provides:       tex(ot1iwonalcm.fd) = %{tl_version}, tex(ot1iwonalm.fd) = %{tl_version}
Provides:       tex(ot1iwonam.fd) = %{tl_version}, tex(ot2iwona.fd) = %{tl_version}
Provides:       tex(ot2iwonac.fd) = %{tl_version}, tex(ot2iwonal.fd) = %{tl_version}
Provides:       tex(ot2iwonalc.fd) = %{tl_version}, tex(ot4iwona.fd) = %{tl_version}
Provides:       tex(ot4iwonac.fd) = %{tl_version}, tex(ot4iwonal.fd) = %{tl_version}
Provides:       tex(ot4iwonalc.fd) = %{tl_version}, tex(qxiwona.fd) = %{tl_version}
Provides:       tex(qxiwonac.fd) = %{tl_version}, tex(qxiwonal.fd) = %{tl_version}
Provides:       tex(qxiwonalc.fd) = %{tl_version}, tex(t1iwona.fd) = %{tl_version}
Provides:       tex(t1iwonac.fd) = %{tl_version}, tex(t1iwonal.fd) = %{tl_version}
Provides:       tex(t1iwonalc.fd) = %{tl_version}, tex(t2aiwona.fd) = %{tl_version}
Provides:       tex(t2aiwonac.fd) = %{tl_version}, tex(t2aiwonal.fd) = %{tl_version}
Provides:       tex(t2aiwonalc.fd) = %{tl_version}, tex(t2biwona.fd) = %{tl_version}
Provides:       tex(t2biwonac.fd) = %{tl_version}, tex(t2biwonal.fd) = %{tl_version}
Provides:       tex(t2biwonalc.fd) = %{tl_version}, tex(t2ciwona.fd) = %{tl_version}
Provides:       tex(t2ciwonac.fd) = %{tl_version}, tex(t2ciwonal.fd) = %{tl_version}
Provides:       tex(t2ciwonalc.fd) = %{tl_version}, tex(t5iwona.fd) = %{tl_version}
Provides:       tex(t5iwonac.fd) = %{tl_version}, tex(t5iwonal.fd) = %{tl_version}
Provides:       tex(t5iwonalc.fd) = %{tl_version}, tex(ts1iwona.fd) = %{tl_version}
Provides:       tex(ts1iwonac.fd) = %{tl_version}, tex(ts1iwonal.fd) = %{tl_version}
Provides:       tex(ts1iwonalc.fd) = %{tl_version}, tex(iwona-math.tex) = %{tl_version}

%description -n texlive-iwona
Iwona is a two-element sans-serif typeface. It was created as
an alternative version of the Kurier typeface, which was
designed in 1975 for a diploma in typeface design at the Warsaw
Academy of Fine Arts under the supervision of Roman
Tomaszewski. This distribution contains a significantly
extended set of characters covering the following modern
alphabets: latin (including Vietnamese), Cyrillic and Greek as
well as a number of additional symbols (including mathematical
symbols). The fonts are prepared in Type 1 and OpenType
formats. For use with TeX the following encoding files have
been prepared: T1 (ec), T2 (abc), and OT2--Cyrillic, T5
(Vietnamese), OT4, QX, texansi and nonstandard (IL2 for the
Czech fonts), as well as supporting macros and files defining
fonts for LaTeX.

%package -n texlive-iwona-doc
Summary:        Documentation for iwona
Version:        svn19611.0.995b

Provides:       tex-iwona-doc
AutoReqProv:    No

%description -n texlive-iwona-doc
Documentation for iwona

%package -n texlive-jablantile
Provides:       tex-jablantile = %{tl_version}
License:        Public Domain
Summary:        Metafont version of tiles in the style of Slavik Jablan
Version:        svn16364.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-jablantile
This is a small Metafont font to implement the modular tiles
described by Slavik Jablan. For an outline of the theoretical
structure of the tiles, see (for example) Jablan's JMM 2006
Exhibit.

%package -n texlive-jablantile-doc
Summary:        Documentation for jablantile
Version:        svn16364.0

Provides:       tex-jablantile-doc
AutoReqProv:    No

%description -n texlive-jablantile-doc
Documentation for jablantile

%package -n texlive-jamtimes
Provides:       tex-jamtimes = %{tl_version}
License:        BSD
Summary:        Expanded Times Roman fonts
Version:        svn20408.1.12

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(eucal.sty), tex(amsfonts.sty)
Provides:       tex(jtm.map) = %{tl_version}, tex(blsy.tfm) = %{tl_version}
Provides:       tex(jtmb7tv.tfm) = %{tl_version}, tex(jtmb8cv.tfm) = %{tl_version}
Provides:       tex(jtmb8rv.tfm) = %{tl_version}, tex(jtmb8tv.tfm) = %{tl_version}
Provides:       tex(jtmbc7tv.tfm) = %{tl_version}, tex(jtmbc8tv.tfm) = %{tl_version}
Provides:       tex(jtmbi7me.tfm) = %{tl_version}, tex(jtmbi7tv.tfm) = %{tl_version}
Provides:       tex(jtmbi8cv.tfm) = %{tl_version}, tex(jtmbi8rv.tfm) = %{tl_version}
Provides:       tex(jtmbi8tv.tfm) = %{tl_version}, tex(jtmbo7tv.tfm) = %{tl_version}
Provides:       tex(jtmbo8cv.tfm) = %{tl_version}, tex(jtmbo8rv.tfm) = %{tl_version}
Provides:       tex(jtmbo8tv.tfm) = %{tl_version}, tex(jtmr7tc.tfm) = %{tl_version}
Provides:       tex(jtmr7te.tfm) = %{tl_version}, tex(jtmr7tw.tfm) = %{tl_version}
Provides:       tex(jtmr7ye.tfm) = %{tl_version}, tex(jtmr7yoe.tfm) = %{tl_version}
Provides:       tex(jtmr8cc.tfm) = %{tl_version}, tex(jtmr8ce.tfm) = %{tl_version}
Provides:       tex(jtmr8cw.tfm) = %{tl_version}, tex(jtmr8rc.tfm) = %{tl_version}
Provides:       tex(jtmr8re.tfm) = %{tl_version}, tex(jtmr8rw.tfm) = %{tl_version}
Provides:       tex(jtmr8tc.tfm) = %{tl_version}, tex(jtmr8te.tfm) = %{tl_version}
Provides:       tex(jtmr8tw.tfm) = %{tl_version}, tex(jtmrc7te.tfm) = %{tl_version}
Provides:       tex(jtmrc7tw.tfm) = %{tl_version}, tex(jtmrc8te.tfm) = %{tl_version}
Provides:       tex(jtmrc8tw.tfm) = %{tl_version}, tex(jtmri7me.tfm) = %{tl_version}
Provides:       tex(jtmri7te.tfm) = %{tl_version}, tex(jtmri7tw.tfm) = %{tl_version}
Provides:       tex(jtmri7ze.tfm) = %{tl_version}, tex(jtmri8ce.tfm) = %{tl_version}
Provides:       tex(jtmri8cw.tfm) = %{tl_version}, tex(jtmri8re.tfm) = %{tl_version}
Provides:       tex(jtmri8rw.tfm) = %{tl_version}, tex(jtmri8te.tfm) = %{tl_version}
Provides:       tex(jtmri8tw.tfm) = %{tl_version}, tex(jtmro7te.tfm) = %{tl_version}
Provides:       tex(jtmro7tw.tfm) = %{tl_version}, tex(jtmro8ce.tfm) = %{tl_version}
Provides:       tex(jtmro8cw.tfm) = %{tl_version}, tex(jtmro8re.tfm) = %{tl_version}
Provides:       tex(jtmro8rw.tfm) = %{tl_version}, tex(jtmro8te.tfm) = %{tl_version}
Provides:       tex(jtmro8tw.tfm) = %{tl_version}, tex(ptmb8a.tfm) = %{tl_version}
Provides:       tex(ptmbi8a.tfm) = %{tl_version}, tex(ptmr8a.tfm) = %{tl_version}
Provides:       tex(ptmri8a.tfm) = %{tl_version}, tex(rblmi.tfm) = %{tl_version}
Provides:       tex(jtmb7tv.vf) = %{tl_version}, tex(jtmb8cv.vf) = %{tl_version}
Provides:       tex(jtmb8tv.vf) = %{tl_version}, tex(jtmbc7tv.vf) = %{tl_version}
Provides:       tex(jtmbc8tv.vf) = %{tl_version}, tex(jtmbi7me.vf) = %{tl_version}
Provides:       tex(jtmbi7tv.vf) = %{tl_version}, tex(jtmbi8cv.vf) = %{tl_version}
Provides:       tex(jtmbi8tv.vf) = %{tl_version}, tex(jtmbo7tv.vf) = %{tl_version}
Provides:       tex(jtmbo8cv.vf) = %{tl_version}, tex(jtmbo8tv.vf) = %{tl_version}
Provides:       tex(jtmr7tc.vf) = %{tl_version}, tex(jtmr7te.vf) = %{tl_version}
Provides:       tex(jtmr7tw.vf) = %{tl_version}, tex(jtmr7ye.vf) = %{tl_version}
Provides:       tex(jtmr8cc.vf) = %{tl_version}, tex(jtmr8ce.vf) = %{tl_version}
Provides:       tex(jtmr8cw.vf) = %{tl_version}, tex(jtmr8tc.vf) = %{tl_version}
Provides:       tex(jtmr8te.vf) = %{tl_version}, tex(jtmr8tw.vf) = %{tl_version}
Provides:       tex(jtmrc7te.vf) = %{tl_version}, tex(jtmrc7tw.vf) = %{tl_version}
Provides:       tex(jtmrc8te.vf) = %{tl_version}, tex(jtmrc8tw.vf) = %{tl_version}
Provides:       tex(jtmri7me.vf) = %{tl_version}, tex(jtmri7te.vf) = %{tl_version}
Provides:       tex(jtmri7tw.vf) = %{tl_version}, tex(jtmri8ce.vf) = %{tl_version}
Provides:       tex(jtmri8cw.vf) = %{tl_version}, tex(jtmri8te.vf) = %{tl_version}
Provides:       tex(jtmri8tw.vf) = %{tl_version}, tex(jtmro7te.vf) = %{tl_version}
Provides:       tex(jtmro7tw.vf) = %{tl_version}, tex(jtmro8ce.vf) = %{tl_version}
Provides:       tex(jtmro8cw.vf) = %{tl_version}, tex(jtmro8te.vf) = %{tl_version}
Provides:       tex(jtmro8tw.vf) = %{tl_version}, tex(jamtimes.sty) = %{tl_version}
Provides:       tex(omljtm.fd) = %{tl_version}, tex(omsjtm.fd) = %{tl_version}
Provides:       tex(ot1jtm.fd) = %{tl_version}, tex(t1jtm.fd) = %{tl_version}
Provides:       tex(ts1jtm.fd) = %{tl_version}

%description -n texlive-jamtimes
The package offers LaTeX support for the expanded Times Roman
font, which has been used for many years in the Journal
d'Analyse Mathematique. Mathematics support is based on the
Belleek fonts.

%package -n texlive-jamtimes-doc
Summary:        Documentation for jamtimes
Version:        svn20408.1.12

Provides:       tex-jamtimes-doc
AutoReqProv:    No

%description -n texlive-jamtimes-doc
Documentation for jamtimes

%package -n texlive-junicode
Provides:       tex-junicode = %{tl_version}
License:        GPL+
Summary:        A TrueType font for mediaevalists
Version:        svn28286.0.7.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Junicode-Bold.ttf) = %{tl_version}, tex(Junicode-BoldItalic.ttf) = %{tl_version}
Provides:       tex(Junicode-Italic.ttf) = %{tl_version}
Provides:       tex(Junicode.ttf) = %{tl_version}, tex(mt-Junicode.cfg) = %{tl_version}

%description -n texlive-junicode
Junicode is a TrueType font with many OpenType features for
antiquarians (especially medievalists) based on typefaces used
by the Oxford Press in the late 17th and early 18th centuries.
It works well with Xe(La)TeX.

%package -n texlive-junicode-doc
Summary:        Documentation for junicode
Version:        svn28286.0.7.7

Provides:       tex-junicode-doc
AutoReqProv:    No

%description -n texlive-junicode-doc
Documentation for junicode

%package -n texlive-kixfont
Provides:       tex-kixfont = %{tl_version}
License:        Copyright only
Summary:        A font for KIX codes
Version:        svn18488.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(kix.tfm) = %{tl_version}

%description -n texlive-kixfont
The KIX code is a barcode-like format used by the Dutch PTT to
encode country codes, zip codes and street numbers in a machine-
readable format. If printed below the address line on bulk
mailings, a discount can be obtained. The font is distributed
in Metafont format, and covers the numbers and upper-case
letters.

%package -n texlive-kixfont-doc
Summary:        Documentation for kixfont
Version:        svn18488.0

Provides:       tex-kixfont-doc
AutoReqProv:    No

%description -n texlive-kixfont-doc
Documentation for kixfont

%package -n texlive-kpfonts
Provides:       tex-kpfonts = %{tl_version}
License:        GPL+
Summary:        A complete set of fonts for text and mathematics
Version:        svn29803.3.31

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(textcomp.sty), tex(amsmath.sty), tex(ifthen.sty)
Provides:       tex(kpfonts-expert-sc.enc) = %{tl_version}
Provides:       tex(kpfonts-expert-tt.enc) = %{tl_version}
Provides:       tex(kpfonts-expert.enc) = %{tl_version}, tex(kpfonts-large-sc.enc) = %{tl_version}
Provides:       tex(kpfonts-expert-sc.enc) = %{tl_version}
Provides:       tex(kpfonts-expert-tt.enc) = %{tl_version}
Provides:       tex(kpfonts-expert.enc) = %{tl_version}, tex(kpfonts-large-sc.enc) = %{tl_version}
Provides:       tex(kpfonts.map) = %{tl_version}, tex(jkpbex.tfm) = %{tl_version}
Provides:       tex(jkpbexa.tfm) = %{tl_version}, tex(jkpbit7c.tfm) = %{tl_version}
Provides:       tex(jkpbit7t.tfm) = %{tl_version}, tex(jkpbit8a.tfm) = %{tl_version}
Provides:       tex(jkpbit8r.tfm) = %{tl_version}, tex(jkpbit8t.tfm) = %{tl_version}
Provides:       tex(jkpbitc.tfm) = %{tl_version}, tex(jkpbite.tfm) = %{tl_version}
Provides:       tex(jkpbmi.tfm) = %{tl_version}, tex(jkpbmia.tfm) = %{tl_version}
Provides:       tex(jkpbmiaw.tfm) = %{tl_version}, tex(jkpbmif.tfm) = %{tl_version}
Provides:       tex(jkpbmifw.tfm) = %{tl_version}, tex(jkpbmiw.tfm) = %{tl_version}
Provides:       tex(jkpbn7c.tfm) = %{tl_version}, tex(jkpbn7t.tfm) = %{tl_version}
Provides:       tex(jkpbn8a.tfm) = %{tl_version}, tex(jkpbn8r.tfm) = %{tl_version}
Provides:       tex(jkpbn8t.tfm) = %{tl_version}, tex(jkpbnc.tfm) = %{tl_version}
Provides:       tex(jkpbne.tfm) = %{tl_version}, tex(jkpbsc7c.tfm) = %{tl_version}
Provides:       tex(jkpbsc7t.tfm) = %{tl_version}, tex(jkpbsc8a.tfm) = %{tl_version}
Provides:       tex(jkpbsc8r.tfm) = %{tl_version}, tex(jkpbsc8t.tfm) = %{tl_version}
Provides:       tex(jkpbsce.tfm) = %{tl_version}, tex(jkpbscsl7c.tfm) = %{tl_version}
Provides:       tex(jkpbscsl7t.tfm) = %{tl_version}, tex(jkpbscsl8r.tfm) = %{tl_version}
Provides:       tex(jkpbscsl8t.tfm) = %{tl_version}, tex(jkpbscsle.tfm) = %{tl_version}
Provides:       tex(jkpbsl7c.tfm) = %{tl_version}, tex(jkpbsl7t.tfm) = %{tl_version}
Provides:       tex(jkpbsl8r.tfm) = %{tl_version}, tex(jkpbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpbslc.tfm) = %{tl_version}, tex(jkpbsle.tfm) = %{tl_version}
Provides:       tex(jkpbsy.tfm) = %{tl_version}, tex(jkpbsya.tfm) = %{tl_version}
Provides:       tex(jkpbsyb.tfm) = %{tl_version}, tex(jkpbsybw.tfm) = %{tl_version}
Provides:       tex(jkpbsyc.tfm) = %{tl_version}, tex(jkpbsyd.tfm) = %{tl_version}
Provides:       tex(jkpbsydw.tfm) = %{tl_version}, tex(jkpbsyw.tfm) = %{tl_version}
Provides:       tex(jkpbxit7c.tfm) = %{tl_version}, tex(jkpbxit7t.tfm) = %{tl_version}
Provides:       tex(jkpbxit8r.tfm) = %{tl_version}, tex(jkpbxit8t.tfm) = %{tl_version}
Provides:       tex(jkpbxitc.tfm) = %{tl_version}, tex(jkpbxite.tfm) = %{tl_version}
Provides:       tex(jkpbxn7c.tfm) = %{tl_version}, tex(jkpbxn7t.tfm) = %{tl_version}
Provides:       tex(jkpbxn8r.tfm) = %{tl_version}, tex(jkpbxn8t.tfm) = %{tl_version}
Provides:       tex(jkpbxnc.tfm) = %{tl_version}, tex(jkpbxne.tfm) = %{tl_version}
Provides:       tex(jkpbxsc7c.tfm) = %{tl_version}, tex(jkpbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkpbxsc8r.tfm) = %{tl_version}, tex(jkpbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkpbxsce.tfm) = %{tl_version}, tex(jkpbxscsl7c.tfm) = %{tl_version}
Provides:       tex(jkpbxscsl7t.tfm) = %{tl_version}, tex(jkpbxscsl8r.tfm) = %{tl_version}
Provides:       tex(jkpbxscsl8t.tfm) = %{tl_version}, tex(jkpbxscsle.tfm) = %{tl_version}
Provides:       tex(jkpbxsl7c.tfm) = %{tl_version}, tex(jkpbxsl7t.tfm) = %{tl_version}
Provides:       tex(jkpbxsl8r.tfm) = %{tl_version}, tex(jkpbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpbxslc.tfm) = %{tl_version}, tex(jkpbxsle.tfm) = %{tl_version}
Provides:       tex(jkpex.tfm) = %{tl_version}, tex(jkpexa.tfm) = %{tl_version}
Provides:       tex(jkpfbit7t.tfm) = %{tl_version}, tex(jkpfbit8t.tfm) = %{tl_version}
Provides:       tex(jkpfbn7t.tfm) = %{tl_version}, tex(jkpfbn8t.tfm) = %{tl_version}
Provides:       tex(jkpfbsl7t.tfm) = %{tl_version}, tex(jkpfbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpfbxit7t.tfm) = %{tl_version}, tex(jkpfbxit8t.tfm) = %{tl_version}
Provides:       tex(jkpfbxn7t.tfm) = %{tl_version}, tex(jkpfbxn8t.tfm) = %{tl_version}
Provides:       tex(jkpfbxsl7t.tfm) = %{tl_version}, tex(jkpfbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpfmit7t.tfm) = %{tl_version}, tex(jkpfmit8t.tfm) = %{tl_version}
Provides:       tex(jkpfmn7t.tfm) = %{tl_version}, tex(jkpfmn8t.tfm) = %{tl_version}
Provides:       tex(jkpfmsl7t.tfm) = %{tl_version}, tex(jkpfmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnbit7t.tfm) = %{tl_version}, tex(jkpfosnbit8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnbn7t.tfm) = %{tl_version}, tex(jkpfosnbn8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnbsl7t.tfm) = %{tl_version}, tex(jkpfosnbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnbxit7t.tfm) = %{tl_version}, tex(jkpfosnbxit8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnbxn7t.tfm) = %{tl_version}, tex(jkpfosnbxn8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnbxsl7t.tfm) = %{tl_version}, tex(jkpfosnbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnmit7t.tfm) = %{tl_version}, tex(jkpfosnmit8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnmn7t.tfm) = %{tl_version}, tex(jkpfosnmn8t.tfm) = %{tl_version}
Provides:       tex(jkpfosnmsl7t.tfm) = %{tl_version}, tex(jkpfosnmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpfssosnbn7t.tfm) = %{tl_version}, tex(jkpfssosnbn8t.tfm) = %{tl_version}
Provides:       tex(jkpfssosnbsl7t.tfm) = %{tl_version}, tex(jkpfssosnbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpfssosnbxn7t.tfm) = %{tl_version}, tex(jkpfssosnbxn8t.tfm) = %{tl_version}
Provides:       tex(jkpfssosnbxsl7t.tfm) = %{tl_version}
Provides:       tex(jkpfssosnbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpfssosnmn7t.tfm) = %{tl_version}, tex(jkpfssosnmn8t.tfm) = %{tl_version}
Provides:       tex(jkpfssosnmsl7t.tfm) = %{tl_version}, tex(jkpfssosnmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkbsc.tfm) = %{tl_version}, tex(jkpkbsc7t.tfm) = %{tl_version}
Provides:       tex(jkpkbsc8t.tfm) = %{tl_version}, tex(jkpkbscsl.tfm) = %{tl_version}
Provides:       tex(jkpkbscsl7t.tfm) = %{tl_version}, tex(jkpkbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkbxsc.tfm) = %{tl_version}, tex(jkpkbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkpkbxsc8t.tfm) = %{tl_version}, tex(jkpkbxscsl.tfm) = %{tl_version}
Provides:       tex(jkpkbxscsl7t.tfm) = %{tl_version}, tex(jkpkbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkmsc.tfm) = %{tl_version}, tex(jkpkmsc7t.tfm) = %{tl_version}
Provides:       tex(jkpkmsc8t.tfm) = %{tl_version}, tex(jkpkmscsl.tfm) = %{tl_version}
Provides:       tex(jkpkmscsl7t.tfm) = %{tl_version}, tex(jkpkmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkosbsc7t.tfm) = %{tl_version}, tex(jkpkosbsc8t.tfm) = %{tl_version}
Provides:       tex(jkpkosbscsl7t.tfm) = %{tl_version}, tex(jkpkosbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkosbxsc7t.tfm) = %{tl_version}, tex(jkpkosbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkpkosbxscsl7t.tfm) = %{tl_version}, tex(jkpkosbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkosmsc7t.tfm) = %{tl_version}, tex(jkpkosmsc8t.tfm) = %{tl_version}
Provides:       tex(jkpkosmscsl7t.tfm) = %{tl_version}, tex(jkpkosmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkosnbsc7t.tfm) = %{tl_version}, tex(jkpkosnbsc8t.tfm) = %{tl_version}
Provides:       tex(jkpkosnbscsl7t.tfm) = %{tl_version}, tex(jkpkosnbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkosnbxsc7t.tfm) = %{tl_version}, tex(jkpkosnbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkpkosnbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpkosnbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpkosnmsc7t.tfm) = %{tl_version}, tex(jkpkosnmsc8t.tfm) = %{tl_version}
Provides:       tex(jkpkosnmscsl7t.tfm) = %{tl_version}, tex(jkpkosnmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplbex.tfm) = %{tl_version}, tex(jkplbexa.tfm) = %{tl_version}
Provides:       tex(jkplbit7c.tfm) = %{tl_version}, tex(jkplbit7t.tfm) = %{tl_version}
Provides:       tex(jkplbit8a.tfm) = %{tl_version}, tex(jkplbit8r.tfm) = %{tl_version}
Provides:       tex(jkplbit8t.tfm) = %{tl_version}, tex(jkplbitc.tfm) = %{tl_version}
Provides:       tex(jkplbite.tfm) = %{tl_version}, tex(jkplbmi.tfm) = %{tl_version}
Provides:       tex(jkplbmia.tfm) = %{tl_version}, tex(jkplbmiaw.tfm) = %{tl_version}
Provides:       tex(jkplbmif.tfm) = %{tl_version}, tex(jkplbmifw.tfm) = %{tl_version}
Provides:       tex(jkplbmiw.tfm) = %{tl_version}, tex(jkplbn7c.tfm) = %{tl_version}
Provides:       tex(jkplbn7t.tfm) = %{tl_version}, tex(jkplbn8a.tfm) = %{tl_version}
Provides:       tex(jkplbn8r.tfm) = %{tl_version}, tex(jkplbn8t.tfm) = %{tl_version}
Provides:       tex(jkplbnc.tfm) = %{tl_version}, tex(jkplbne.tfm) = %{tl_version}
Provides:       tex(jkplbsc7c.tfm) = %{tl_version}, tex(jkplbsc7t.tfm) = %{tl_version}
Provides:       tex(jkplbsc8a.tfm) = %{tl_version}, tex(jkplbsc8r.tfm) = %{tl_version}
Provides:       tex(jkplbsc8t.tfm) = %{tl_version}, tex(jkplbsce.tfm) = %{tl_version}
Provides:       tex(jkplbscsl7c.tfm) = %{tl_version}, tex(jkplbscsl7t.tfm) = %{tl_version}
Provides:       tex(jkplbscsl8r.tfm) = %{tl_version}, tex(jkplbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplbscsle.tfm) = %{tl_version}, tex(jkplbsl7c.tfm) = %{tl_version}
Provides:       tex(jkplbsl7t.tfm) = %{tl_version}, tex(jkplbsl8r.tfm) = %{tl_version}
Provides:       tex(jkplbsl8t.tfm) = %{tl_version}, tex(jkplbslc.tfm) = %{tl_version}
Provides:       tex(jkplbsle.tfm) = %{tl_version}, tex(jkplbsy.tfm) = %{tl_version}
Provides:       tex(jkplbsyb.tfm) = %{tl_version}, tex(jkplbsybw.tfm) = %{tl_version}
Provides:       tex(jkplbsyc.tfm) = %{tl_version}, tex(jkplbsyd.tfm) = %{tl_version}
Provides:       tex(jkplbsydw.tfm) = %{tl_version}, tex(jkplbsyw.tfm) = %{tl_version}
Provides:       tex(jkplbxit7c.tfm) = %{tl_version}, tex(jkplbxit7t.tfm) = %{tl_version}
Provides:       tex(jkplbxit8r.tfm) = %{tl_version}, tex(jkplbxit8t.tfm) = %{tl_version}
Provides:       tex(jkplbxitc.tfm) = %{tl_version}, tex(jkplbxite.tfm) = %{tl_version}
Provides:       tex(jkplbxn7c.tfm) = %{tl_version}, tex(jkplbxn7t.tfm) = %{tl_version}
Provides:       tex(jkplbxn8r.tfm) = %{tl_version}, tex(jkplbxn8t.tfm) = %{tl_version}
Provides:       tex(jkplbxnc.tfm) = %{tl_version}, tex(jkplbxne.tfm) = %{tl_version}
Provides:       tex(jkplbxsc7c.tfm) = %{tl_version}, tex(jkplbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkplbxsc8r.tfm) = %{tl_version}, tex(jkplbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkplbxsce.tfm) = %{tl_version}, tex(jkplbxscsl7c.tfm) = %{tl_version}
Provides:       tex(jkplbxscsl7t.tfm) = %{tl_version}, tex(jkplbxscsl8r.tfm) = %{tl_version}
Provides:       tex(jkplbxscsl8t.tfm) = %{tl_version}, tex(jkplbxscsle.tfm) = %{tl_version}
Provides:       tex(jkplbxsl7c.tfm) = %{tl_version}, tex(jkplbxsl7t.tfm) = %{tl_version}
Provides:       tex(jkplbxsl8r.tfm) = %{tl_version}, tex(jkplbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkplbxslc.tfm) = %{tl_version}, tex(jkplbxsle.tfm) = %{tl_version}
Provides:       tex(jkplex.tfm) = %{tl_version}, tex(jkplexa.tfm) = %{tl_version}
Provides:       tex(jkplfbit7t.tfm) = %{tl_version}, tex(jkplfbit8t.tfm) = %{tl_version}
Provides:       tex(jkplfbn7t.tfm) = %{tl_version}, tex(jkplfbn8t.tfm) = %{tl_version}
Provides:       tex(jkplfbsl7t.tfm) = %{tl_version}, tex(jkplfbsl8t.tfm) = %{tl_version}
Provides:       tex(jkplfbxit7t.tfm) = %{tl_version}, tex(jkplfbxit8t.tfm) = %{tl_version}
Provides:       tex(jkplfbxn7t.tfm) = %{tl_version}, tex(jkplfbxn8t.tfm) = %{tl_version}
Provides:       tex(jkplfbxsl7t.tfm) = %{tl_version}, tex(jkplfbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkplfmit7t.tfm) = %{tl_version}, tex(jkplfmit8t.tfm) = %{tl_version}
Provides:       tex(jkplfmn7t.tfm) = %{tl_version}, tex(jkplfmn8t.tfm) = %{tl_version}
Provides:       tex(jkplfmsl7t.tfm) = %{tl_version}, tex(jkplfmsl8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnbit7t.tfm) = %{tl_version}, tex(jkplfosnbit8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnbn7t.tfm) = %{tl_version}, tex(jkplfosnbn8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnbsl7t.tfm) = %{tl_version}, tex(jkplfosnbsl8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnbxit7t.tfm) = %{tl_version}, tex(jkplfosnbxit8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnbxn7t.tfm) = %{tl_version}, tex(jkplfosnbxn8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnbxsl7t.tfm) = %{tl_version}, tex(jkplfosnbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnmit7t.tfm) = %{tl_version}, tex(jkplfosnmit8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnmn7t.tfm) = %{tl_version}, tex(jkplfosnmn8t.tfm) = %{tl_version}
Provides:       tex(jkplfosnmsl7t.tfm) = %{tl_version}, tex(jkplfosnmsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkbsc.tfm) = %{tl_version}, tex(jkplkbsc7t.tfm) = %{tl_version}
Provides:       tex(jkplkbsc8t.tfm) = %{tl_version}, tex(jkplkbscsl.tfm) = %{tl_version}
Provides:       tex(jkplkbscsl7t.tfm) = %{tl_version}, tex(jkplkbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkbxsc.tfm) = %{tl_version}, tex(jkplkbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkplkbxsc8t.tfm) = %{tl_version}, tex(jkplkbxscsl.tfm) = %{tl_version}
Provides:       tex(jkplkbxscsl7t.tfm) = %{tl_version}, tex(jkplkbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkmsc.tfm) = %{tl_version}, tex(jkplkmsc7t.tfm) = %{tl_version}
Provides:       tex(jkplkmsc8t.tfm) = %{tl_version}, tex(jkplkmscsl.tfm) = %{tl_version}
Provides:       tex(jkplkmscsl7t.tfm) = %{tl_version}, tex(jkplkmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkosbsc7t.tfm) = %{tl_version}, tex(jkplkosbsc8t.tfm) = %{tl_version}
Provides:       tex(jkplkosbscsl7t.tfm) = %{tl_version}, tex(jkplkosbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkosbxsc7t.tfm) = %{tl_version}, tex(jkplkosbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkplkosbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkplkosbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkosmsc7t.tfm) = %{tl_version}, tex(jkplkosmsc8t.tfm) = %{tl_version}
Provides:       tex(jkplkosmscsl7t.tfm) = %{tl_version}, tex(jkplkosmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkosnbsc7t.tfm) = %{tl_version}, tex(jkplkosnbsc8t.tfm) = %{tl_version}
Provides:       tex(jkplkosnbscsl7t.tfm) = %{tl_version}
Provides:       tex(jkplkosnbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkosnbxsc7t.tfm) = %{tl_version}, tex(jkplkosnbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkplkosnbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkplkosnbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplkosnmsc7t.tfm) = %{tl_version}, tex(jkplkosnmsc8t.tfm) = %{tl_version}
Provides:       tex(jkplkosnmscsl7t.tfm) = %{tl_version}
Provides:       tex(jkplkosnmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplmi.tfm) = %{tl_version}, tex(jkplmia.tfm) = %{tl_version}
Provides:       tex(jkplmiaw.tfm) = %{tl_version}, tex(jkplmif.tfm) = %{tl_version}
Provides:       tex(jkplmifw.tfm) = %{tl_version}, tex(jkplmit7c.tfm) = %{tl_version}
Provides:       tex(jkplmit7t.tfm) = %{tl_version}, tex(jkplmit8a.tfm) = %{tl_version}
Provides:       tex(jkplmit8r.tfm) = %{tl_version}, tex(jkplmit8t.tfm) = %{tl_version}
Provides:       tex(jkplmitc.tfm) = %{tl_version}, tex(jkplmite.tfm) = %{tl_version}
Provides:       tex(jkplmiw.tfm) = %{tl_version}, tex(jkplmn7c.tfm) = %{tl_version}
Provides:       tex(jkplmn7t.tfm) = %{tl_version}, tex(jkplmn8a.tfm) = %{tl_version}
Provides:       tex(jkplmn8r.tfm) = %{tl_version}, tex(jkplmn8t.tfm) = %{tl_version}
Provides:       tex(jkplmnc.tfm) = %{tl_version}, tex(jkplmne.tfm) = %{tl_version}
Provides:       tex(jkplmsc7c.tfm) = %{tl_version}, tex(jkplmsc7t.tfm) = %{tl_version}
Provides:       tex(jkplmsc8a.tfm) = %{tl_version}, tex(jkplmsc8r.tfm) = %{tl_version}
Provides:       tex(jkplmsc8t.tfm) = %{tl_version}, tex(jkplmsce.tfm) = %{tl_version}
Provides:       tex(jkplmscsl7c.tfm) = %{tl_version}, tex(jkplmscsl7t.tfm) = %{tl_version}
Provides:       tex(jkplmscsl8r.tfm) = %{tl_version}, tex(jkplmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplmscsle.tfm) = %{tl_version}, tex(jkplmsl7c.tfm) = %{tl_version}
Provides:       tex(jkplmsl7t.tfm) = %{tl_version}, tex(jkplmsl8r.tfm) = %{tl_version}
Provides:       tex(jkplmsl8t.tfm) = %{tl_version}, tex(jkplmslc.tfm) = %{tl_version}
Provides:       tex(jkplmsle.tfm) = %{tl_version}, tex(jkplosbit7c.tfm) = %{tl_version}
Provides:       tex(jkplosbit7t.tfm) = %{tl_version}, tex(jkplosbit8t.tfm) = %{tl_version}
Provides:       tex(jkplosbn7c.tfm) = %{tl_version}, tex(jkplosbn7t.tfm) = %{tl_version}
Provides:       tex(jkplosbn8t.tfm) = %{tl_version}, tex(jkplosbsc7c.tfm) = %{tl_version}
Provides:       tex(jkplosbsc7t.tfm) = %{tl_version}, tex(jkplosbsc8t.tfm) = %{tl_version}
Provides:       tex(jkplosbscsl7t.tfm) = %{tl_version}, tex(jkplosbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplosbsl7c.tfm) = %{tl_version}, tex(jkplosbsl7t.tfm) = %{tl_version}
Provides:       tex(jkplosbsl8t.tfm) = %{tl_version}, tex(jkplosbxit7c.tfm) = %{tl_version}
Provides:       tex(jkplosbxit7t.tfm) = %{tl_version}, tex(jkplosbxit8t.tfm) = %{tl_version}
Provides:       tex(jkplosbxn7c.tfm) = %{tl_version}, tex(jkplosbxn7t.tfm) = %{tl_version}
Provides:       tex(jkplosbxn8t.tfm) = %{tl_version}, tex(jkplosbxsc7c.tfm) = %{tl_version}
Provides:       tex(jkplosbxsc7t.tfm) = %{tl_version}, tex(jkplosbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkplosbxscsl7t.tfm) = %{tl_version}, tex(jkplosbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplosbxsl7c.tfm) = %{tl_version}, tex(jkplosbxsl7t.tfm) = %{tl_version}
Provides:       tex(jkplosbxsl8t.tfm) = %{tl_version}, tex(jkplosmit7c.tfm) = %{tl_version}
Provides:       tex(jkplosmit7t.tfm) = %{tl_version}, tex(jkplosmit8t.tfm) = %{tl_version}
Provides:       tex(jkplosmn7c.tfm) = %{tl_version}, tex(jkplosmn7t.tfm) = %{tl_version}
Provides:       tex(jkplosmn8t.tfm) = %{tl_version}, tex(jkplosmsc7c.tfm) = %{tl_version}
Provides:       tex(jkplosmsc7t.tfm) = %{tl_version}, tex(jkplosmsc8t.tfm) = %{tl_version}
Provides:       tex(jkplosmscsl7t.tfm) = %{tl_version}, tex(jkplosmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplosmsl7c.tfm) = %{tl_version}, tex(jkplosmsl7t.tfm) = %{tl_version}
Provides:       tex(jkplosmsl8t.tfm) = %{tl_version}, tex(jkplosnbit7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbit8t.tfm) = %{tl_version}, tex(jkplosnbn7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbn8t.tfm) = %{tl_version}, tex(jkplosnbsc7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbsc8t.tfm) = %{tl_version}, tex(jkplosnbscsl7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbscsl8t.tfm) = %{tl_version}, tex(jkplosnbsl7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbsl8t.tfm) = %{tl_version}, tex(jkplosnbxit7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbxit8t.tfm) = %{tl_version}, tex(jkplosnbxn7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbxn8t.tfm) = %{tl_version}, tex(jkplosnbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbxsc8t.tfm) = %{tl_version}, tex(jkplosnbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkplosnbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplosnbxsl7t.tfm) = %{tl_version}, tex(jkplosnbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkplosnmit7t.tfm) = %{tl_version}, tex(jkplosnmit8t.tfm) = %{tl_version}
Provides:       tex(jkplosnmn7t.tfm) = %{tl_version}, tex(jkplosnmn8t.tfm) = %{tl_version}
Provides:       tex(jkplosnmsc7t.tfm) = %{tl_version}, tex(jkplosnmsc8t.tfm) = %{tl_version}
Provides:       tex(jkplosnmscsl7t.tfm) = %{tl_version}, tex(jkplosnmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkplosnmsl7t.tfm) = %{tl_version}, tex(jkplosnmsl8t.tfm) = %{tl_version}
Provides:       tex(jkplsy.tfm) = %{tl_version}, tex(jkplsyb.tfm) = %{tl_version}
Provides:       tex(jkplsybw.tfm) = %{tl_version}, tex(jkplsyc.tfm) = %{tl_version}
Provides:       tex(jkplsyd.tfm) = %{tl_version}, tex(jkplsydw.tfm) = %{tl_version}
Provides:       tex(jkplsyw.tfm) = %{tl_version}, tex(jkplvosbit7t.tfm) = %{tl_version}
Provides:       tex(jkplvosbit8t.tfm) = %{tl_version}, tex(jkplvosbmi.tfm) = %{tl_version}
Provides:       tex(jkplvosbmif.tfm) = %{tl_version}, tex(jkplvosbmifw.tfm) = %{tl_version}
Provides:       tex(jkplvosbmiw.tfm) = %{tl_version}, tex(jkplvosbn7t.tfm) = %{tl_version}
Provides:       tex(jkplvosbn8t.tfm) = %{tl_version}, tex(jkplvosbsl7t.tfm) = %{tl_version}
Provides:       tex(jkplvosbsl8t.tfm) = %{tl_version}, tex(jkplvosbxit7t.tfm) = %{tl_version}
Provides:       tex(jkplvosbxit8t.tfm) = %{tl_version}, tex(jkplvosbxn7t.tfm) = %{tl_version}
Provides:       tex(jkplvosbxn8t.tfm) = %{tl_version}, tex(jkplvosbxsl7t.tfm) = %{tl_version}
Provides:       tex(jkplvosbxsl8t.tfm) = %{tl_version}, tex(jkplvosmi.tfm) = %{tl_version}
Provides:       tex(jkplvosmif.tfm) = %{tl_version}, tex(jkplvosmifw.tfm) = %{tl_version}
Provides:       tex(jkplvosmit7t.tfm) = %{tl_version}, tex(jkplvosmit8t.tfm) = %{tl_version}
Provides:       tex(jkplvosmiw.tfm) = %{tl_version}, tex(jkplvosmn7t.tfm) = %{tl_version}
Provides:       tex(jkplvosmn8t.tfm) = %{tl_version}, tex(jkplvosmsl7t.tfm) = %{tl_version}
Provides:       tex(jkplvosmsl8t.tfm) = %{tl_version}, tex(jkpmi.tfm) = %{tl_version}
Provides:       tex(jkpmia.tfm) = %{tl_version}, tex(jkpmiaw.tfm) = %{tl_version}
Provides:       tex(jkpmif.tfm) = %{tl_version}, tex(jkpmifw.tfm) = %{tl_version}
Provides:       tex(jkpmit7c.tfm) = %{tl_version}, tex(jkpmit7t.tfm) = %{tl_version}
Provides:       tex(jkpmit8a.tfm) = %{tl_version}, tex(jkpmit8r.tfm) = %{tl_version}
Provides:       tex(jkpmit8t.tfm) = %{tl_version}, tex(jkpmitc.tfm) = %{tl_version}
Provides:       tex(jkpmite.tfm) = %{tl_version}, tex(jkpmiw.tfm) = %{tl_version}
Provides:       tex(jkpmn7c.tfm) = %{tl_version}, tex(jkpmn7t.tfm) = %{tl_version}
Provides:       tex(jkpmn8a.tfm) = %{tl_version}, tex(jkpmn8r.tfm) = %{tl_version}
Provides:       tex(jkpmn8t.tfm) = %{tl_version}, tex(jkpmnc.tfm) = %{tl_version}
Provides:       tex(jkpmne.tfm) = %{tl_version}, tex(jkpmsc7c.tfm) = %{tl_version}
Provides:       tex(jkpmsc7t.tfm) = %{tl_version}, tex(jkpmsc8a.tfm) = %{tl_version}
Provides:       tex(jkpmsc8r.tfm) = %{tl_version}, tex(jkpmsc8t.tfm) = %{tl_version}
Provides:       tex(jkpmsce.tfm) = %{tl_version}, tex(jkpmscsl7c.tfm) = %{tl_version}
Provides:       tex(jkpmscsl7t.tfm) = %{tl_version}, tex(jkpmscsl8r.tfm) = %{tl_version}
Provides:       tex(jkpmscsl8t.tfm) = %{tl_version}, tex(jkpmscsle.tfm) = %{tl_version}
Provides:       tex(jkpmsl7c.tfm) = %{tl_version}, tex(jkpmsl7t.tfm) = %{tl_version}
Provides:       tex(jkpmsl8r.tfm) = %{tl_version}, tex(jkpmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpmslc.tfm) = %{tl_version}, tex(jkpmsle.tfm) = %{tl_version}
Provides:       tex(jkposbit7c.tfm) = %{tl_version}, tex(jkposbit7t.tfm) = %{tl_version}
Provides:       tex(jkposbit8t.tfm) = %{tl_version}, tex(jkposbn7c.tfm) = %{tl_version}
Provides:       tex(jkposbn7t.tfm) = %{tl_version}, tex(jkposbn8t.tfm) = %{tl_version}
Provides:       tex(jkposbsc7c.tfm) = %{tl_version}, tex(jkposbsc7t.tfm) = %{tl_version}
Provides:       tex(jkposbsc8t.tfm) = %{tl_version}, tex(jkposbscsl7t.tfm) = %{tl_version}
Provides:       tex(jkposbscsl8t.tfm) = %{tl_version}, tex(jkposbsl7c.tfm) = %{tl_version}
Provides:       tex(jkposbsl7t.tfm) = %{tl_version}, tex(jkposbsl8t.tfm) = %{tl_version}
Provides:       tex(jkposbxit7c.tfm) = %{tl_version}, tex(jkposbxit7t.tfm) = %{tl_version}
Provides:       tex(jkposbxit8t.tfm) = %{tl_version}, tex(jkposbxn7c.tfm) = %{tl_version}
Provides:       tex(jkposbxn7t.tfm) = %{tl_version}, tex(jkposbxn8t.tfm) = %{tl_version}
Provides:       tex(jkposbxsc7c.tfm) = %{tl_version}, tex(jkposbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkposbxsc8t.tfm) = %{tl_version}, tex(jkposbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkposbxscsl8t.tfm) = %{tl_version}, tex(jkposbxsl7c.tfm) = %{tl_version}
Provides:       tex(jkposbxsl7t.tfm) = %{tl_version}, tex(jkposbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkposmit7c.tfm) = %{tl_version}, tex(jkposmit7t.tfm) = %{tl_version}
Provides:       tex(jkposmit8t.tfm) = %{tl_version}, tex(jkposmn7c.tfm) = %{tl_version}
Provides:       tex(jkposmn7t.tfm) = %{tl_version}, tex(jkposmn8t.tfm) = %{tl_version}
Provides:       tex(jkposmsc7c.tfm) = %{tl_version}, tex(jkposmsc7t.tfm) = %{tl_version}
Provides:       tex(jkposmsc8t.tfm) = %{tl_version}, tex(jkposmscsl7t.tfm) = %{tl_version}
Provides:       tex(jkposmscsl8t.tfm) = %{tl_version}, tex(jkposmsl7c.tfm) = %{tl_version}
Provides:       tex(jkposmsl7t.tfm) = %{tl_version}, tex(jkposmsl8t.tfm) = %{tl_version}
Provides:       tex(jkposnbit7t.tfm) = %{tl_version}, tex(jkposnbit8t.tfm) = %{tl_version}
Provides:       tex(jkposnbn7t.tfm) = %{tl_version}, tex(jkposnbn8t.tfm) = %{tl_version}
Provides:       tex(jkposnbsc7t.tfm) = %{tl_version}, tex(jkposnbsc8t.tfm) = %{tl_version}
Provides:       tex(jkposnbscsl7t.tfm) = %{tl_version}, tex(jkposnbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkposnbsl7t.tfm) = %{tl_version}, tex(jkposnbsl8t.tfm) = %{tl_version}
Provides:       tex(jkposnbxit7t.tfm) = %{tl_version}, tex(jkposnbxit8t.tfm) = %{tl_version}
Provides:       tex(jkposnbxn7t.tfm) = %{tl_version}, tex(jkposnbxn8t.tfm) = %{tl_version}
Provides:       tex(jkposnbxsc7t.tfm) = %{tl_version}, tex(jkposnbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkposnbxscsl7t.tfm) = %{tl_version}, tex(jkposnbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkposnbxsl7t.tfm) = %{tl_version}, tex(jkposnbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkposnmit7t.tfm) = %{tl_version}, tex(jkposnmit8t.tfm) = %{tl_version}
Provides:       tex(jkposnmn7t.tfm) = %{tl_version}, tex(jkposnmn8t.tfm) = %{tl_version}
Provides:       tex(jkposnmsc7t.tfm) = %{tl_version}, tex(jkposnmsc8t.tfm) = %{tl_version}
Provides:       tex(jkposnmscsl7t.tfm) = %{tl_version}, tex(jkposnmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkposnmsl7t.tfm) = %{tl_version}, tex(jkposnmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssbex.tfm) = %{tl_version}, tex(jkpssbmi.tfm) = %{tl_version}
Provides:       tex(jkpssbmia.tfm) = %{tl_version}, tex(jkpssbmif.tfm) = %{tl_version}
Provides:       tex(jkpssbn7c.tfm) = %{tl_version}, tex(jkpssbn7t.tfm) = %{tl_version}
Provides:       tex(jkpssbn8a.tfm) = %{tl_version}, tex(jkpssbn8r.tfm) = %{tl_version}
Provides:       tex(jkpssbn8t.tfm) = %{tl_version}, tex(jkpssbnc.tfm) = %{tl_version}
Provides:       tex(jkpssbne.tfm) = %{tl_version}, tex(jkpssbsc7c.tfm) = %{tl_version}
Provides:       tex(jkpssbsc7t.tfm) = %{tl_version}, tex(jkpssbsc8a.tfm) = %{tl_version}
Provides:       tex(jkpssbsc8r.tfm) = %{tl_version}, tex(jkpssbsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssbsce.tfm) = %{tl_version}, tex(jkpssbscsl7c.tfm) = %{tl_version}
Provides:       tex(jkpssbscsl7t.tfm) = %{tl_version}, tex(jkpssbscsl8r.tfm) = %{tl_version}
Provides:       tex(jkpssbscsl8t.tfm) = %{tl_version}, tex(jkpssbscsle.tfm) = %{tl_version}
Provides:       tex(jkpssbsl7c.tfm) = %{tl_version}, tex(jkpssbsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssbsl8r.tfm) = %{tl_version}, tex(jkpssbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssbslc.tfm) = %{tl_version}, tex(jkpssbsle.tfm) = %{tl_version}
Provides:       tex(jkpssbsyb.tfm) = %{tl_version}, tex(jkpssbsybw.tfm) = %{tl_version}
Provides:       tex(jkpssbxn7c.tfm) = %{tl_version}, tex(jkpssbxn7t.tfm) = %{tl_version}
Provides:       tex(jkpssbxn8r.tfm) = %{tl_version}, tex(jkpssbxn8t.tfm) = %{tl_version}
Provides:       tex(jkpssbxnc.tfm) = %{tl_version}, tex(jkpssbxne.tfm) = %{tl_version}
Provides:       tex(jkpssbxsc7c.tfm) = %{tl_version}, tex(jkpssbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkpssbxsc8r.tfm) = %{tl_version}, tex(jkpssbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssbxsce.tfm) = %{tl_version}, tex(jkpssbxscsl7c.tfm) = %{tl_version}
Provides:       tex(jkpssbxscsl7t.tfm) = %{tl_version}, tex(jkpssbxscsl8r.tfm) = %{tl_version}
Provides:       tex(jkpssbxscsl8t.tfm) = %{tl_version}, tex(jkpssbxscsle.tfm) = %{tl_version}
Provides:       tex(jkpssbxsl7c.tfm) = %{tl_version}, tex(jkpssbxsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssbxsl8r.tfm) = %{tl_version}, tex(jkpssbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssbxslc.tfm) = %{tl_version}, tex(jkpssbxsle.tfm) = %{tl_version}
Provides:       tex(jkpssex.tfm) = %{tl_version}, tex(jkpssfbn7t.tfm) = %{tl_version}
Provides:       tex(jkpssfbn8t.tfm) = %{tl_version}, tex(jkpssfbsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssfbsl8t.tfm) = %{tl_version}, tex(jkpssfbxn7t.tfm) = %{tl_version}
Provides:       tex(jkpssfbxn8t.tfm) = %{tl_version}, tex(jkpssfbxsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssfbxsl8t.tfm) = %{tl_version}, tex(jkpssfmn7t.tfm) = %{tl_version}
Provides:       tex(jkpssfmn8t.tfm) = %{tl_version}, tex(jkpssfmsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssfmsl8t.tfm) = %{tl_version}, tex(jkpssfosnbn7t.tfm) = %{tl_version}
Provides:       tex(jkpssfosnbn8t.tfm) = %{tl_version}, tex(jkpssfosnbsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssfosnbsl8t.tfm) = %{tl_version}, tex(jkpssfosnbxn7t.tfm) = %{tl_version}
Provides:       tex(jkpssfosnbxn8t.tfm) = %{tl_version}, tex(jkpssfosnbxsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssfosnbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssfosnmn7t.tfm) = %{tl_version}, tex(jkpssfosnmn8t.tfm) = %{tl_version}
Provides:       tex(jkpssfosnmsl7t.tfm) = %{tl_version}, tex(jkpssfosnmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskbsc.tfm) = %{tl_version}, tex(jkpsskbsc7t.tfm) = %{tl_version}
Provides:       tex(jkpsskbsc8t.tfm) = %{tl_version}, tex(jkpsskbscsl.tfm) = %{tl_version}
Provides:       tex(jkpsskbscsl7t.tfm) = %{tl_version}, tex(jkpsskbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskbxsc.tfm) = %{tl_version}, tex(jkpsskbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkpsskbxsc8t.tfm) = %{tl_version}, tex(jkpsskbxscsl.tfm) = %{tl_version}
Provides:       tex(jkpsskbxscsl7t.tfm) = %{tl_version}, tex(jkpsskbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskmsc.tfm) = %{tl_version}, tex(jkpsskmsc7t.tfm) = %{tl_version}
Provides:       tex(jkpsskmsc8t.tfm) = %{tl_version}, tex(jkpsskmscsl.tfm) = %{tl_version}
Provides:       tex(jkpsskmscsl7t.tfm) = %{tl_version}, tex(jkpsskmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosbsc7t.tfm) = %{tl_version}, tex(jkpsskosbsc8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosbscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpsskosbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosbxsc7t.tfm) = %{tl_version}, tex(jkpsskosbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpsskosbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosmsc7t.tfm) = %{tl_version}, tex(jkpsskosmsc8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosmscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpsskosmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnbsc7t.tfm) = %{tl_version}, tex(jkpsskosnbsc8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnbscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnmsc7t.tfm) = %{tl_version}, tex(jkpsskosnmsc8t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnmscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpsskosnmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsslbsyb.tfm) = %{tl_version}, tex(jkpsslbsybw.tfm) = %{tl_version}
Provides:       tex(jkpsslsyb.tfm) = %{tl_version}, tex(jkpsslsybw.tfm) = %{tl_version}
Provides:       tex(jkpssmi.tfm) = %{tl_version}, tex(jkpssmia.tfm) = %{tl_version}
Provides:       tex(jkpssmif.tfm) = %{tl_version}, tex(jkpssmn7c.tfm) = %{tl_version}
Provides:       tex(jkpssmn7t.tfm) = %{tl_version}, tex(jkpssmn8a.tfm) = %{tl_version}
Provides:       tex(jkpssmn8r.tfm) = %{tl_version}, tex(jkpssmn8t.tfm) = %{tl_version}
Provides:       tex(jkpssmnc.tfm) = %{tl_version}, tex(jkpssmne.tfm) = %{tl_version}
Provides:       tex(jkpssmsc7c.tfm) = %{tl_version}, tex(jkpssmsc7t.tfm) = %{tl_version}
Provides:       tex(jkpssmsc8a.tfm) = %{tl_version}, tex(jkpssmsc8r.tfm) = %{tl_version}
Provides:       tex(jkpssmsc8t.tfm) = %{tl_version}, tex(jkpssmsce.tfm) = %{tl_version}
Provides:       tex(jkpssmscsl7c.tfm) = %{tl_version}, tex(jkpssmscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssmscsl8r.tfm) = %{tl_version}, tex(jkpssmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssmscsle.tfm) = %{tl_version}, tex(jkpssmsl7c.tfm) = %{tl_version}
Provides:       tex(jkpssmsl7t.tfm) = %{tl_version}, tex(jkpssmsl8r.tfm) = %{tl_version}
Provides:       tex(jkpssmsl8t.tfm) = %{tl_version}, tex(jkpssmslc.tfm) = %{tl_version}
Provides:       tex(jkpssmsle.tfm) = %{tl_version}, tex(jkpssosbn7t.tfm) = %{tl_version}
Provides:       tex(jkpssosbn8t.tfm) = %{tl_version}, tex(jkpssosbsc7t.tfm) = %{tl_version}
Provides:       tex(jkpssosbsc8t.tfm) = %{tl_version}, tex(jkpssosbscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssosbscsl8t.tfm) = %{tl_version}, tex(jkpssosbsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssosbsl8t.tfm) = %{tl_version}, tex(jkpssosbxn7t.tfm) = %{tl_version}
Provides:       tex(jkpssosbxn8t.tfm) = %{tl_version}, tex(jkpssosbxsc7t.tfm) = %{tl_version}
Provides:       tex(jkpssosbxsc8t.tfm) = %{tl_version}, tex(jkpssosbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssosbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosbxsl7t.tfm) = %{tl_version}, tex(jkpssosbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosmn7t.tfm) = %{tl_version}, tex(jkpssosmn8t.tfm) = %{tl_version}
Provides:       tex(jkpssosmsc7t.tfm) = %{tl_version}, tex(jkpssosmsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssosmscsl7t.tfm) = %{tl_version}, tex(jkpssosmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosmsl7t.tfm) = %{tl_version}, tex(jkpssosmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbn7t.tfm) = %{tl_version}, tex(jkpssosnbn8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbsc7t.tfm) = %{tl_version}, tex(jkpssosnbsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbsl7t.tfm) = %{tl_version}, tex(jkpssosnbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbxn7t.tfm) = %{tl_version}, tex(jkpssosnbxn8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbxsc7t.tfm) = %{tl_version}, tex(jkpssosnbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbxscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbxscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnbxsl7t.tfm) = %{tl_version}, tex(jkpssosnbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnmn7t.tfm) = %{tl_version}, tex(jkpssosnmn8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnmsc7t.tfm) = %{tl_version}, tex(jkpssosnmsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnmscsl7t.tfm) = %{tl_version}
Provides:       tex(jkpssosnmscsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssosnmsl7t.tfm) = %{tl_version}, tex(jkpssosnmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsssyb.tfm) = %{tl_version}, tex(jkpsssybw.tfm) = %{tl_version}
Provides:       tex(jkpssvosbmi.tfm) = %{tl_version}, tex(jkpssvosbmif.tfm) = %{tl_version}
Provides:       tex(jkpssvosbn7t.tfm) = %{tl_version}, tex(jkpssvosbn8t.tfm) = %{tl_version}
Provides:       tex(jkpssvosbsc7t.tfm) = %{tl_version}, tex(jkpssvosbsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssvosbsl7t.tfm) = %{tl_version}, tex(jkpssvosbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssvosbxn7t.tfm) = %{tl_version}, tex(jkpssvosbxn8t.tfm) = %{tl_version}
Provides:       tex(jkpssvosbxsc7t.tfm) = %{tl_version}, tex(jkpssvosbxsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssvosbxsl7t.tfm) = %{tl_version}, tex(jkpssvosbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpssvosmi.tfm) = %{tl_version}, tex(jkpssvosmif.tfm) = %{tl_version}
Provides:       tex(jkpssvosmn7t.tfm) = %{tl_version}, tex(jkpssvosmn8t.tfm) = %{tl_version}
Provides:       tex(jkpssvosmsc7t.tfm) = %{tl_version}, tex(jkpssvosmsc8t.tfm) = %{tl_version}
Provides:       tex(jkpssvosmsl7t.tfm) = %{tl_version}, tex(jkpssvosmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpsy.tfm) = %{tl_version}, tex(jkpsya.tfm) = %{tl_version}
Provides:       tex(jkpsyb.tfm) = %{tl_version}, tex(jkpsybw.tfm) = %{tl_version}
Provides:       tex(jkpsyc.tfm) = %{tl_version}, tex(jkpsyd.tfm) = %{tl_version}
Provides:       tex(jkpsydw.tfm) = %{tl_version}, tex(jkpsyw.tfm) = %{tl_version}
Provides:       tex(jkpttbn7c.tfm) = %{tl_version}, tex(jkpttbn7t.tfm) = %{tl_version}
Provides:       tex(jkpttbn8a.tfm) = %{tl_version}, tex(jkpttbn8r.tfm) = %{tl_version}
Provides:       tex(jkpttbn8t.tfm) = %{tl_version}, tex(jkpttbnc.tfm) = %{tl_version}
Provides:       tex(jkpttbne.tfm) = %{tl_version}, tex(jkpttbsl7c.tfm) = %{tl_version}
Provides:       tex(jkpttbsl7t.tfm) = %{tl_version}, tex(jkpttbsl8r.tfm) = %{tl_version}
Provides:       tex(jkpttbsl8t.tfm) = %{tl_version}, tex(jkpttbslc.tfm) = %{tl_version}
Provides:       tex(jkpttbsle.tfm) = %{tl_version}, tex(jkpttmn7c.tfm) = %{tl_version}
Provides:       tex(jkpttmn7t.tfm) = %{tl_version}, tex(jkpttmn8a.tfm) = %{tl_version}
Provides:       tex(jkpttmn8r.tfm) = %{tl_version}, tex(jkpttmn8t.tfm) = %{tl_version}
Provides:       tex(jkpttmnc.tfm) = %{tl_version}, tex(jkpttmne.tfm) = %{tl_version}
Provides:       tex(jkpttmsl7c.tfm) = %{tl_version}, tex(jkpttmsl7t.tfm) = %{tl_version}
Provides:       tex(jkpttmsl8r.tfm) = %{tl_version}, tex(jkpttmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpttmslc.tfm) = %{tl_version}, tex(jkpttmsle.tfm) = %{tl_version}
Provides:       tex(jkpttosbn7t.tfm) = %{tl_version}, tex(jkpttosbn8t.tfm) = %{tl_version}
Provides:       tex(jkpttosbsl7t.tfm) = %{tl_version}, tex(jkpttosbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpttosmn7t.tfm) = %{tl_version}, tex(jkpttosmn8t.tfm) = %{tl_version}
Provides:       tex(jkpttosmsl7t.tfm) = %{tl_version}, tex(jkpttosmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpttosnbn7t.tfm) = %{tl_version}, tex(jkpttosnbn8t.tfm) = %{tl_version}
Provides:       tex(jkpttosnbsl7t.tfm) = %{tl_version}, tex(jkpttosnbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpttosnmn7t.tfm) = %{tl_version}, tex(jkpttosnmn8t.tfm) = %{tl_version}
Provides:       tex(jkpttosnmsl7t.tfm) = %{tl_version}, tex(jkpttosnmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpttvosbn7t.tfm) = %{tl_version}, tex(jkpttvosbn8t.tfm) = %{tl_version}
Provides:       tex(jkpttvosbsl7t.tfm) = %{tl_version}, tex(jkpttvosbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpttvosmn7t.tfm) = %{tl_version}, tex(jkpttvosmn8t.tfm) = %{tl_version}
Provides:       tex(jkpttvosmsl7t.tfm) = %{tl_version}, tex(jkpttvosmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpvosbit7t.tfm) = %{tl_version}, tex(jkpvosbit8t.tfm) = %{tl_version}
Provides:       tex(jkpvosbmi.tfm) = %{tl_version}, tex(jkpvosbmif.tfm) = %{tl_version}
Provides:       tex(jkpvosbmifw.tfm) = %{tl_version}, tex(jkpvosbmiw.tfm) = %{tl_version}
Provides:       tex(jkpvosbn7t.tfm) = %{tl_version}, tex(jkpvosbn8t.tfm) = %{tl_version}
Provides:       tex(jkpvosbsl7t.tfm) = %{tl_version}, tex(jkpvosbsl8t.tfm) = %{tl_version}
Provides:       tex(jkpvosbxit7t.tfm) = %{tl_version}, tex(jkpvosbxit8t.tfm) = %{tl_version}
Provides:       tex(jkpvosbxn7t.tfm) = %{tl_version}, tex(jkpvosbxn8t.tfm) = %{tl_version}
Provides:       tex(jkpvosbxsl7t.tfm) = %{tl_version}, tex(jkpvosbxsl8t.tfm) = %{tl_version}
Provides:       tex(jkpvosmi.tfm) = %{tl_version}, tex(jkpvosmif.tfm) = %{tl_version}
Provides:       tex(jkpvosmifw.tfm) = %{tl_version}, tex(jkpvosmit7t.tfm) = %{tl_version}
Provides:       tex(jkpvosmit8t.tfm) = %{tl_version}, tex(jkpvosmiw.tfm) = %{tl_version}
Provides:       tex(jkpvosmn7t.tfm) = %{tl_version}, tex(jkpvosmn8t.tfm) = %{tl_version}
Provides:       tex(jkpvosmsl7t.tfm) = %{tl_version}, tex(jkpvosmsl8t.tfm) = %{tl_version}
Provides:       tex(jkpbex.pfb) = %{tl_version}, tex(jkpbexa.pfb) = %{tl_version}
Provides:       tex(jkpbit8a.pfb) = %{tl_version}, tex(jkpbitc.pfb) = %{tl_version}
Provides:       tex(jkpbite.pfb) = %{tl_version}, tex(jkpbmi.pfb) = %{tl_version}
Provides:       tex(jkpbmia.pfb) = %{tl_version}, tex(jkpbn8a.pfb) = %{tl_version}
Provides:       tex(jkpbnc.pfb) = %{tl_version}, tex(jkpbne.pfb) = %{tl_version}
Provides:       tex(jkpbsc8a.pfb) = %{tl_version}, tex(jkpbsce.pfb) = %{tl_version}
Provides:       tex(jkpbsy.pfb) = %{tl_version}, tex(jkpbsya.pfb) = %{tl_version}
Provides:       tex(jkpbsyb.pfb) = %{tl_version}, tex(jkpbsyc.pfb) = %{tl_version}
Provides:       tex(jkpbsyd.pfb) = %{tl_version}, tex(jkpex.pfb) = %{tl_version}
Provides:       tex(jkpexa.pfb) = %{tl_version}, tex(jkpkbsc.pfb) = %{tl_version}
Provides:       tex(jkpkmsc.pfb) = %{tl_version}, tex(jkplbex.pfb) = %{tl_version}
Provides:       tex(jkplbexa.pfb) = %{tl_version}, tex(jkplbit8a.pfb) = %{tl_version}
Provides:       tex(jkplbitc.pfb) = %{tl_version}, tex(jkplbite.pfb) = %{tl_version}
Provides:       tex(jkplbmi.pfb) = %{tl_version}, tex(jkplbmia.pfb) = %{tl_version}
Provides:       tex(jkplbn8a.pfb) = %{tl_version}, tex(jkplbnc.pfb) = %{tl_version}
Provides:       tex(jkplbne.pfb) = %{tl_version}, tex(jkplbsc8a.pfb) = %{tl_version}
Provides:       tex(jkplbsce.pfb) = %{tl_version}, tex(jkplbsy.pfb) = %{tl_version}
Provides:       tex(jkplbsyb.pfb) = %{tl_version}, tex(jkplbsyc.pfb) = %{tl_version}
Provides:       tex(jkplbsyd.pfb) = %{tl_version}, tex(jkplex.pfb) = %{tl_version}
Provides:       tex(jkplexa.pfb) = %{tl_version}, tex(jkplkbsc.pfb) = %{tl_version}
Provides:       tex(jkplkmsc.pfb) = %{tl_version}, tex(jkplmi.pfb) = %{tl_version}
Provides:       tex(jkplmia.pfb) = %{tl_version}, tex(jkplmit8a.pfb) = %{tl_version}
Provides:       tex(jkplmitc.pfb) = %{tl_version}, tex(jkplmite.pfb) = %{tl_version}
Provides:       tex(jkplmn8a.pfb) = %{tl_version}, tex(jkplmnc.pfb) = %{tl_version}
Provides:       tex(jkplmne.pfb) = %{tl_version}, tex(jkplmsc8a.pfb) = %{tl_version}
Provides:       tex(jkplmsce.pfb) = %{tl_version}, tex(jkplsy.pfb) = %{tl_version}
Provides:       tex(jkplsyb.pfb) = %{tl_version}, tex(jkplsyc.pfb) = %{tl_version}
Provides:       tex(jkplsyd.pfb) = %{tl_version}, tex(jkpmi.pfb) = %{tl_version}
Provides:       tex(jkpmia.pfb) = %{tl_version}, tex(jkpmit8a.pfb) = %{tl_version}
Provides:       tex(jkpmitc.pfb) = %{tl_version}, tex(jkpmite.pfb) = %{tl_version}
Provides:       tex(jkpmn8a.pfb) = %{tl_version}, tex(jkpmnc.pfb) = %{tl_version}
Provides:       tex(jkpmne.pfb) = %{tl_version}, tex(jkpmsc8a.pfb) = %{tl_version}
Provides:       tex(jkpmsce.pfb) = %{tl_version}, tex(jkpssbn8a.pfb) = %{tl_version}
Provides:       tex(jkpssbnc.pfb) = %{tl_version}, tex(jkpssbne.pfb) = %{tl_version}
Provides:       tex(jkpssbsc8a.pfb) = %{tl_version}, tex(jkpssbsce.pfb) = %{tl_version}
Provides:       tex(jkpsskbsc.pfb) = %{tl_version}, tex(jkpsskmsc.pfb) = %{tl_version}
Provides:       tex(jkpssmn8a.pfb) = %{tl_version}, tex(jkpssmnc.pfb) = %{tl_version}
Provides:       tex(jkpssmne.pfb) = %{tl_version}, tex(jkpssmsc8a.pfb) = %{tl_version}
Provides:       tex(jkpssmsce.pfb) = %{tl_version}, tex(jkpsy.pfb) = %{tl_version}
Provides:       tex(jkpsya.pfb) = %{tl_version}, tex(jkpsyb.pfb) = %{tl_version}
Provides:       tex(jkpsyc.pfb) = %{tl_version}, tex(jkpsyd.pfb) = %{tl_version}
Provides:       tex(jkpttbn8a.pfb) = %{tl_version}, tex(jkpttbnc.pfb) = %{tl_version}
Provides:       tex(jkpttbne.pfb) = %{tl_version}, tex(jkpttmn8a.pfb) = %{tl_version}
Provides:       tex(jkpttmnc.pfb) = %{tl_version}, tex(jkpttmne.pfb) = %{tl_version}
Provides:       tex(jkpbit7c.vf) = %{tl_version}, tex(jkpbit7t.vf) = %{tl_version}
Provides:       tex(jkpbit8t.vf) = %{tl_version}, tex(jkpbmiaw.vf) = %{tl_version}
Provides:       tex(jkpbmif.vf) = %{tl_version}, tex(jkpbmifw.vf) = %{tl_version}
Provides:       tex(jkpbmiw.vf) = %{tl_version}, tex(jkpbn7c.vf) = %{tl_version}
Provides:       tex(jkpbn7t.vf) = %{tl_version}, tex(jkpbn8t.vf) = %{tl_version}
Provides:       tex(jkpbsc7c.vf) = %{tl_version}, tex(jkpbsc7t.vf) = %{tl_version}
Provides:       tex(jkpbsc8t.vf) = %{tl_version}, tex(jkpbscsl7c.vf) = %{tl_version}
Provides:       tex(jkpbscsl7t.vf) = %{tl_version}, tex(jkpbscsl8t.vf) = %{tl_version}
Provides:       tex(jkpbsl7c.vf) = %{tl_version}, tex(jkpbsl7t.vf) = %{tl_version}
Provides:       tex(jkpbsl8t.vf) = %{tl_version}, tex(jkpbsybw.vf) = %{tl_version}
Provides:       tex(jkpbsydw.vf) = %{tl_version}, tex(jkpbsyw.vf) = %{tl_version}
Provides:       tex(jkpbxit7c.vf) = %{tl_version}, tex(jkpbxit7t.vf) = %{tl_version}
Provides:       tex(jkpbxit8t.vf) = %{tl_version}, tex(jkpbxn7c.vf) = %{tl_version}
Provides:       tex(jkpbxn7t.vf) = %{tl_version}, tex(jkpbxn8t.vf) = %{tl_version}
Provides:       tex(jkpbxsc7c.vf) = %{tl_version}, tex(jkpbxsc7t.vf) = %{tl_version}
Provides:       tex(jkpbxsc8t.vf) = %{tl_version}, tex(jkpbxscsl7c.vf) = %{tl_version}
Provides:       tex(jkpbxscsl7t.vf) = %{tl_version}, tex(jkpbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkpbxsl7c.vf) = %{tl_version}, tex(jkpbxsl7t.vf) = %{tl_version}
Provides:       tex(jkpbxsl8t.vf) = %{tl_version}, tex(jkpfbit7t.vf) = %{tl_version}
Provides:       tex(jkpfbit8t.vf) = %{tl_version}, tex(jkpfbn7t.vf) = %{tl_version}
Provides:       tex(jkpfbn8t.vf) = %{tl_version}, tex(jkpfbsl7t.vf) = %{tl_version}
Provides:       tex(jkpfbsl8t.vf) = %{tl_version}, tex(jkpfbxit7t.vf) = %{tl_version}
Provides:       tex(jkpfbxit8t.vf) = %{tl_version}, tex(jkpfbxn7t.vf) = %{tl_version}
Provides:       tex(jkpfbxn8t.vf) = %{tl_version}, tex(jkpfbxsl7t.vf) = %{tl_version}
Provides:       tex(jkpfbxsl8t.vf) = %{tl_version}, tex(jkpfmit7t.vf) = %{tl_version}
Provides:       tex(jkpfmit8t.vf) = %{tl_version}, tex(jkpfmn7t.vf) = %{tl_version}
Provides:       tex(jkpfmn8t.vf) = %{tl_version}, tex(jkpfmsl7t.vf) = %{tl_version}
Provides:       tex(jkpfmsl8t.vf) = %{tl_version}, tex(jkpfosnbit7t.vf) = %{tl_version}
Provides:       tex(jkpfosnbit8t.vf) = %{tl_version}, tex(jkpfosnbn7t.vf) = %{tl_version}
Provides:       tex(jkpfosnbn8t.vf) = %{tl_version}, tex(jkpfosnbsl7t.vf) = %{tl_version}
Provides:       tex(jkpfosnbsl8t.vf) = %{tl_version}, tex(jkpfosnbxit7t.vf) = %{tl_version}
Provides:       tex(jkpfosnbxit8t.vf) = %{tl_version}, tex(jkpfosnbxn7t.vf) = %{tl_version}
Provides:       tex(jkpfosnbxn8t.vf) = %{tl_version}, tex(jkpfosnbxsl7t.vf) = %{tl_version}
Provides:       tex(jkpfosnbxsl8t.vf) = %{tl_version}, tex(jkpfosnmit7t.vf) = %{tl_version}
Provides:       tex(jkpfosnmit8t.vf) = %{tl_version}, tex(jkpfosnmn7t.vf) = %{tl_version}
Provides:       tex(jkpfosnmn8t.vf) = %{tl_version}, tex(jkpfosnmsl7t.vf) = %{tl_version}
Provides:       tex(jkpfosnmsl8t.vf) = %{tl_version}, tex(jkpfssosnbn7t.vf) = %{tl_version}
Provides:       tex(jkpfssosnbn8t.vf) = %{tl_version}, tex(jkpfssosnbsl7t.vf) = %{tl_version}
Provides:       tex(jkpfssosnbsl8t.vf) = %{tl_version}, tex(jkpfssosnbxn7t.vf) = %{tl_version}
Provides:       tex(jkpfssosnbxn8t.vf) = %{tl_version}, tex(jkpfssosnbxsl7t.vf) = %{tl_version}
Provides:       tex(jkpfssosnbxsl8t.vf) = %{tl_version}, tex(jkpfssosnmn7t.vf) = %{tl_version}
Provides:       tex(jkpfssosnmn8t.vf) = %{tl_version}, tex(jkpfssosnmsl7t.vf) = %{tl_version}
Provides:       tex(jkpfssosnmsl8t.vf) = %{tl_version}, tex(jkpkbsc7t.vf) = %{tl_version}
Provides:       tex(jkpkbsc8t.vf) = %{tl_version}, tex(jkpkbscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkbscsl8t.vf) = %{tl_version}, tex(jkpkbxsc7t.vf) = %{tl_version}
Provides:       tex(jkpkbxsc8t.vf) = %{tl_version}, tex(jkpkbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkbxscsl8t.vf) = %{tl_version}, tex(jkpkmsc7t.vf) = %{tl_version}
Provides:       tex(jkpkmsc8t.vf) = %{tl_version}, tex(jkpkmscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkmscsl8t.vf) = %{tl_version}, tex(jkpkosbsc7t.vf) = %{tl_version}
Provides:       tex(jkpkosbsc8t.vf) = %{tl_version}, tex(jkpkosbscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkosbscsl8t.vf) = %{tl_version}, tex(jkpkosbxsc7t.vf) = %{tl_version}
Provides:       tex(jkpkosbxsc8t.vf) = %{tl_version}, tex(jkpkosbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkosbxscsl8t.vf) = %{tl_version}, tex(jkpkosmsc7t.vf) = %{tl_version}
Provides:       tex(jkpkosmsc8t.vf) = %{tl_version}, tex(jkpkosmscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkosmscsl8t.vf) = %{tl_version}, tex(jkpkosnbsc7t.vf) = %{tl_version}
Provides:       tex(jkpkosnbsc8t.vf) = %{tl_version}, tex(jkpkosnbscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkosnbscsl8t.vf) = %{tl_version}, tex(jkpkosnbxsc7t.vf) = %{tl_version}
Provides:       tex(jkpkosnbxsc8t.vf) = %{tl_version}, tex(jkpkosnbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkosnbxscsl8t.vf) = %{tl_version}, tex(jkpkosnmsc7t.vf) = %{tl_version}
Provides:       tex(jkpkosnmsc8t.vf) = %{tl_version}, tex(jkpkosnmscsl7t.vf) = %{tl_version}
Provides:       tex(jkpkosnmscsl8t.vf) = %{tl_version}, tex(jkplbit7c.vf) = %{tl_version}
Provides:       tex(jkplbit7t.vf) = %{tl_version}, tex(jkplbit8t.vf) = %{tl_version}
Provides:       tex(jkplbmiaw.vf) = %{tl_version}, tex(jkplbmif.vf) = %{tl_version}
Provides:       tex(jkplbmifw.vf) = %{tl_version}, tex(jkplbmiw.vf) = %{tl_version}
Provides:       tex(jkplbn7c.vf) = %{tl_version}, tex(jkplbn7t.vf) = %{tl_version}
Provides:       tex(jkplbn8t.vf) = %{tl_version}, tex(jkplbsc7c.vf) = %{tl_version}
Provides:       tex(jkplbsc7t.vf) = %{tl_version}, tex(jkplbsc8t.vf) = %{tl_version}
Provides:       tex(jkplbscsl7c.vf) = %{tl_version}, tex(jkplbscsl7t.vf) = %{tl_version}
Provides:       tex(jkplbscsl8t.vf) = %{tl_version}, tex(jkplbsl7c.vf) = %{tl_version}
Provides:       tex(jkplbsl7t.vf) = %{tl_version}, tex(jkplbsl8t.vf) = %{tl_version}
Provides:       tex(jkplbsybw.vf) = %{tl_version}, tex(jkplbsydw.vf) = %{tl_version}
Provides:       tex(jkplbsyw.vf) = %{tl_version}, tex(jkplbxit7c.vf) = %{tl_version}
Provides:       tex(jkplbxit7t.vf) = %{tl_version}, tex(jkplbxit8t.vf) = %{tl_version}
Provides:       tex(jkplbxn7c.vf) = %{tl_version}, tex(jkplbxn7t.vf) = %{tl_version}
Provides:       tex(jkplbxn8t.vf) = %{tl_version}, tex(jkplbxsc7c.vf) = %{tl_version}
Provides:       tex(jkplbxsc7t.vf) = %{tl_version}, tex(jkplbxsc8t.vf) = %{tl_version}
Provides:       tex(jkplbxscsl7c.vf) = %{tl_version}, tex(jkplbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkplbxscsl8t.vf) = %{tl_version}, tex(jkplbxsl7c.vf) = %{tl_version}
Provides:       tex(jkplbxsl7t.vf) = %{tl_version}, tex(jkplbxsl8t.vf) = %{tl_version}
Provides:       tex(jkplfbit7t.vf) = %{tl_version}, tex(jkplfbit8t.vf) = %{tl_version}
Provides:       tex(jkplfbn7t.vf) = %{tl_version}, tex(jkplfbn8t.vf) = %{tl_version}
Provides:       tex(jkplfbsl7t.vf) = %{tl_version}, tex(jkplfbsl8t.vf) = %{tl_version}
Provides:       tex(jkplfbxit7t.vf) = %{tl_version}, tex(jkplfbxit8t.vf) = %{tl_version}
Provides:       tex(jkplfbxn7t.vf) = %{tl_version}, tex(jkplfbxn8t.vf) = %{tl_version}
Provides:       tex(jkplfbxsl7t.vf) = %{tl_version}, tex(jkplfbxsl8t.vf) = %{tl_version}
Provides:       tex(jkplfmit7t.vf) = %{tl_version}, tex(jkplfmit8t.vf) = %{tl_version}
Provides:       tex(jkplfmn7t.vf) = %{tl_version}, tex(jkplfmn8t.vf) = %{tl_version}
Provides:       tex(jkplfmsl7t.vf) = %{tl_version}, tex(jkplfmsl8t.vf) = %{tl_version}
Provides:       tex(jkplfosnbit7t.vf) = %{tl_version}, tex(jkplfosnbit8t.vf) = %{tl_version}
Provides:       tex(jkplfosnbn7t.vf) = %{tl_version}, tex(jkplfosnbn8t.vf) = %{tl_version}
Provides:       tex(jkplfosnbsl7t.vf) = %{tl_version}, tex(jkplfosnbsl8t.vf) = %{tl_version}
Provides:       tex(jkplfosnbxit7t.vf) = %{tl_version}, tex(jkplfosnbxit8t.vf) = %{tl_version}
Provides:       tex(jkplfosnbxn7t.vf) = %{tl_version}, tex(jkplfosnbxn8t.vf) = %{tl_version}
Provides:       tex(jkplfosnbxsl7t.vf) = %{tl_version}, tex(jkplfosnbxsl8t.vf) = %{tl_version}
Provides:       tex(jkplfosnmit7t.vf) = %{tl_version}, tex(jkplfosnmit8t.vf) = %{tl_version}
Provides:       tex(jkplfosnmn7t.vf) = %{tl_version}, tex(jkplfosnmn8t.vf) = %{tl_version}
Provides:       tex(jkplfosnmsl7t.vf) = %{tl_version}, tex(jkplfosnmsl8t.vf) = %{tl_version}
Provides:       tex(jkplkbsc7t.vf) = %{tl_version}, tex(jkplkbsc8t.vf) = %{tl_version}
Provides:       tex(jkplkbscsl7t.vf) = %{tl_version}, tex(jkplkbscsl8t.vf) = %{tl_version}
Provides:       tex(jkplkbxsc7t.vf) = %{tl_version}, tex(jkplkbxsc8t.vf) = %{tl_version}
Provides:       tex(jkplkbxscsl7t.vf) = %{tl_version}, tex(jkplkbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkplkmsc7t.vf) = %{tl_version}, tex(jkplkmsc8t.vf) = %{tl_version}
Provides:       tex(jkplkmscsl7t.vf) = %{tl_version}, tex(jkplkmscsl8t.vf) = %{tl_version}
Provides:       tex(jkplkosbsc7t.vf) = %{tl_version}, tex(jkplkosbsc8t.vf) = %{tl_version}
Provides:       tex(jkplkosbscsl7t.vf) = %{tl_version}, tex(jkplkosbscsl8t.vf) = %{tl_version}
Provides:       tex(jkplkosbxsc7t.vf) = %{tl_version}, tex(jkplkosbxsc8t.vf) = %{tl_version}
Provides:       tex(jkplkosbxscsl7t.vf) = %{tl_version}, tex(jkplkosbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkplkosmsc7t.vf) = %{tl_version}, tex(jkplkosmsc8t.vf) = %{tl_version}
Provides:       tex(jkplkosmscsl7t.vf) = %{tl_version}, tex(jkplkosmscsl8t.vf) = %{tl_version}
Provides:       tex(jkplkosnbsc7t.vf) = %{tl_version}, tex(jkplkosnbsc8t.vf) = %{tl_version}
Provides:       tex(jkplkosnbscsl7t.vf) = %{tl_version}, tex(jkplkosnbscsl8t.vf) = %{tl_version}
Provides:       tex(jkplkosnbxsc7t.vf) = %{tl_version}, tex(jkplkosnbxsc8t.vf) = %{tl_version}
Provides:       tex(jkplkosnbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkplkosnbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkplkosnmsc7t.vf) = %{tl_version}, tex(jkplkosnmsc8t.vf) = %{tl_version}
Provides:       tex(jkplkosnmscsl7t.vf) = %{tl_version}, tex(jkplkosnmscsl8t.vf) = %{tl_version}
Provides:       tex(jkplmiaw.vf) = %{tl_version}, tex(jkplmif.vf) = %{tl_version}
Provides:       tex(jkplmifw.vf) = %{tl_version}, tex(jkplmit7c.vf) = %{tl_version}
Provides:       tex(jkplmit7t.vf) = %{tl_version}, tex(jkplmit8t.vf) = %{tl_version}
Provides:       tex(jkplmiw.vf) = %{tl_version}, tex(jkplmn7c.vf) = %{tl_version}
Provides:       tex(jkplmn7t.vf) = %{tl_version}, tex(jkplmn8t.vf) = %{tl_version}
Provides:       tex(jkplmsc7c.vf) = %{tl_version}, tex(jkplmsc7t.vf) = %{tl_version}
Provides:       tex(jkplmsc8t.vf) = %{tl_version}, tex(jkplmscsl7c.vf) = %{tl_version}
Provides:       tex(jkplmscsl7t.vf) = %{tl_version}, tex(jkplmscsl8t.vf) = %{tl_version}
Provides:       tex(jkplmsl7c.vf) = %{tl_version}, tex(jkplmsl7t.vf) = %{tl_version}
Provides:       tex(jkplmsl8t.vf) = %{tl_version}, tex(jkplosbit7c.vf) = %{tl_version}
Provides:       tex(jkplosbit7t.vf) = %{tl_version}, tex(jkplosbit8t.vf) = %{tl_version}
Provides:       tex(jkplosbn7c.vf) = %{tl_version}, tex(jkplosbn7t.vf) = %{tl_version}
Provides:       tex(jkplosbn8t.vf) = %{tl_version}, tex(jkplosbsc7c.vf) = %{tl_version}
Provides:       tex(jkplosbsc7t.vf) = %{tl_version}, tex(jkplosbsc8t.vf) = %{tl_version}
Provides:       tex(jkplosbscsl7t.vf) = %{tl_version}, tex(jkplosbscsl8t.vf) = %{tl_version}
Provides:       tex(jkplosbsl7c.vf) = %{tl_version}, tex(jkplosbsl7t.vf) = %{tl_version}
Provides:       tex(jkplosbsl8t.vf) = %{tl_version}, tex(jkplosbxit7c.vf) = %{tl_version}
Provides:       tex(jkplosbxit7t.vf) = %{tl_version}, tex(jkplosbxit8t.vf) = %{tl_version}
Provides:       tex(jkplosbxn7c.vf) = %{tl_version}, tex(jkplosbxn7t.vf) = %{tl_version}
Provides:       tex(jkplosbxn8t.vf) = %{tl_version}, tex(jkplosbxsc7c.vf) = %{tl_version}
Provides:       tex(jkplosbxsc7t.vf) = %{tl_version}, tex(jkplosbxsc8t.vf) = %{tl_version}
Provides:       tex(jkplosbxscsl7t.vf) = %{tl_version}, tex(jkplosbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkplosbxsl7c.vf) = %{tl_version}, tex(jkplosbxsl7t.vf) = %{tl_version}
Provides:       tex(jkplosbxsl8t.vf) = %{tl_version}, tex(jkplosmit7c.vf) = %{tl_version}
Provides:       tex(jkplosmit7t.vf) = %{tl_version}, tex(jkplosmit8t.vf) = %{tl_version}
Provides:       tex(jkplosmn7c.vf) = %{tl_version}, tex(jkplosmn7t.vf) = %{tl_version}
Provides:       tex(jkplosmn8t.vf) = %{tl_version}, tex(jkplosmsc7c.vf) = %{tl_version}
Provides:       tex(jkplosmsc7t.vf) = %{tl_version}, tex(jkplosmsc8t.vf) = %{tl_version}
Provides:       tex(jkplosmscsl7t.vf) = %{tl_version}, tex(jkplosmscsl8t.vf) = %{tl_version}
Provides:       tex(jkplosmsl7c.vf) = %{tl_version}, tex(jkplosmsl7t.vf) = %{tl_version}
Provides:       tex(jkplosmsl8t.vf) = %{tl_version}, tex(jkplosnbit7t.vf) = %{tl_version}
Provides:       tex(jkplosnbit8t.vf) = %{tl_version}, tex(jkplosnbn7t.vf) = %{tl_version}
Provides:       tex(jkplosnbn8t.vf) = %{tl_version}, tex(jkplosnbsc7t.vf) = %{tl_version}
Provides:       tex(jkplosnbsc8t.vf) = %{tl_version}, tex(jkplosnbscsl7t.vf) = %{tl_version}
Provides:       tex(jkplosnbscsl8t.vf) = %{tl_version}, tex(jkplosnbsl7t.vf) = %{tl_version}
Provides:       tex(jkplosnbsl8t.vf) = %{tl_version}, tex(jkplosnbxit7t.vf) = %{tl_version}
Provides:       tex(jkplosnbxit8t.vf) = %{tl_version}, tex(jkplosnbxn7t.vf) = %{tl_version}
Provides:       tex(jkplosnbxn8t.vf) = %{tl_version}, tex(jkplosnbxsc7t.vf) = %{tl_version}
Provides:       tex(jkplosnbxsc8t.vf) = %{tl_version}, tex(jkplosnbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkplosnbxscsl8t.vf) = %{tl_version}, tex(jkplosnbxsl7t.vf) = %{tl_version}
Provides:       tex(jkplosnbxsl8t.vf) = %{tl_version}, tex(jkplosnmit7t.vf) = %{tl_version}
Provides:       tex(jkplosnmit8t.vf) = %{tl_version}, tex(jkplosnmn7t.vf) = %{tl_version}
Provides:       tex(jkplosnmn8t.vf) = %{tl_version}, tex(jkplosnmsc7t.vf) = %{tl_version}
Provides:       tex(jkplosnmsc8t.vf) = %{tl_version}, tex(jkplosnmscsl7t.vf) = %{tl_version}
Provides:       tex(jkplosnmscsl8t.vf) = %{tl_version}, tex(jkplosnmsl7t.vf) = %{tl_version}
Provides:       tex(jkplosnmsl8t.vf) = %{tl_version}, tex(jkplsybw.vf) = %{tl_version}
Provides:       tex(jkplsydw.vf) = %{tl_version}, tex(jkplsyw.vf) = %{tl_version}
Provides:       tex(jkplvosbit7t.vf) = %{tl_version}, tex(jkplvosbit8t.vf) = %{tl_version}
Provides:       tex(jkplvosbmi.vf) = %{tl_version}, tex(jkplvosbmif.vf) = %{tl_version}
Provides:       tex(jkplvosbmifw.vf) = %{tl_version}, tex(jkplvosbmiw.vf) = %{tl_version}
Provides:       tex(jkplvosbn7t.vf) = %{tl_version}, tex(jkplvosbn8t.vf) = %{tl_version}
Provides:       tex(jkplvosbsl7t.vf) = %{tl_version}, tex(jkplvosbsl8t.vf) = %{tl_version}
Provides:       tex(jkplvosbxit7t.vf) = %{tl_version}, tex(jkplvosbxit8t.vf) = %{tl_version}
Provides:       tex(jkplvosbxn7t.vf) = %{tl_version}, tex(jkplvosbxn8t.vf) = %{tl_version}
Provides:       tex(jkplvosbxsl7t.vf) = %{tl_version}, tex(jkplvosbxsl8t.vf) = %{tl_version}
Provides:       tex(jkplvosmi.vf) = %{tl_version}, tex(jkplvosmif.vf) = %{tl_version}
Provides:       tex(jkplvosmifw.vf) = %{tl_version}, tex(jkplvosmit7t.vf) = %{tl_version}
Provides:       tex(jkplvosmit8t.vf) = %{tl_version}, tex(jkplvosmiw.vf) = %{tl_version}
Provides:       tex(jkplvosmn7t.vf) = %{tl_version}, tex(jkplvosmn8t.vf) = %{tl_version}
Provides:       tex(jkplvosmsl7t.vf) = %{tl_version}, tex(jkplvosmsl8t.vf) = %{tl_version}
Provides:       tex(jkpmiaw.vf) = %{tl_version}, tex(jkpmif.vf) = %{tl_version}
Provides:       tex(jkpmifw.vf) = %{tl_version}, tex(jkpmit7c.vf) = %{tl_version}
Provides:       tex(jkpmit7t.vf) = %{tl_version}, tex(jkpmit8t.vf) = %{tl_version}
Provides:       tex(jkpmiw.vf) = %{tl_version}, tex(jkpmn7c.vf) = %{tl_version}
Provides:       tex(jkpmn7t.vf) = %{tl_version}, tex(jkpmn8t.vf) = %{tl_version}
Provides:       tex(jkpmsc7c.vf) = %{tl_version}, tex(jkpmsc7t.vf) = %{tl_version}
Provides:       tex(jkpmsc8t.vf) = %{tl_version}, tex(jkpmscsl7c.vf) = %{tl_version}
Provides:       tex(jkpmscsl7t.vf) = %{tl_version}, tex(jkpmscsl8t.vf) = %{tl_version}
Provides:       tex(jkpmsl7c.vf) = %{tl_version}, tex(jkpmsl7t.vf) = %{tl_version}
Provides:       tex(jkpmsl8t.vf) = %{tl_version}, tex(jkposbit7c.vf) = %{tl_version}
Provides:       tex(jkposbit7t.vf) = %{tl_version}, tex(jkposbit8t.vf) = %{tl_version}
Provides:       tex(jkposbn7c.vf) = %{tl_version}, tex(jkposbn7t.vf) = %{tl_version}
Provides:       tex(jkposbn8t.vf) = %{tl_version}, tex(jkposbsc7c.vf) = %{tl_version}
Provides:       tex(jkposbsc7t.vf) = %{tl_version}, tex(jkposbsc8t.vf) = %{tl_version}
Provides:       tex(jkposbscsl7t.vf) = %{tl_version}, tex(jkposbscsl8t.vf) = %{tl_version}
Provides:       tex(jkposbsl7c.vf) = %{tl_version}, tex(jkposbsl7t.vf) = %{tl_version}
Provides:       tex(jkposbsl8t.vf) = %{tl_version}, tex(jkposbxit7c.vf) = %{tl_version}
Provides:       tex(jkposbxit7t.vf) = %{tl_version}, tex(jkposbxit8t.vf) = %{tl_version}
Provides:       tex(jkposbxn7c.vf) = %{tl_version}, tex(jkposbxn7t.vf) = %{tl_version}
Provides:       tex(jkposbxn8t.vf) = %{tl_version}, tex(jkposbxsc7c.vf) = %{tl_version}
Provides:       tex(jkposbxsc7t.vf) = %{tl_version}, tex(jkposbxsc8t.vf) = %{tl_version}
Provides:       tex(jkposbxscsl7t.vf) = %{tl_version}, tex(jkposbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkposbxsl7c.vf) = %{tl_version}, tex(jkposbxsl7t.vf) = %{tl_version}
Provides:       tex(jkposbxsl8t.vf) = %{tl_version}, tex(jkposmit7c.vf) = %{tl_version}
Provides:       tex(jkposmit7t.vf) = %{tl_version}, tex(jkposmit8t.vf) = %{tl_version}
Provides:       tex(jkposmn7c.vf) = %{tl_version}, tex(jkposmn7t.vf) = %{tl_version}
Provides:       tex(jkposmn8t.vf) = %{tl_version}, tex(jkposmsc7c.vf) = %{tl_version}
Provides:       tex(jkposmsc7t.vf) = %{tl_version}, tex(jkposmsc8t.vf) = %{tl_version}
Provides:       tex(jkposmscsl7t.vf) = %{tl_version}, tex(jkposmscsl8t.vf) = %{tl_version}
Provides:       tex(jkposmsl7c.vf) = %{tl_version}, tex(jkposmsl7t.vf) = %{tl_version}
Provides:       tex(jkposmsl8t.vf) = %{tl_version}, tex(jkposnbit7t.vf) = %{tl_version}
Provides:       tex(jkposnbit8t.vf) = %{tl_version}, tex(jkposnbn7t.vf) = %{tl_version}
Provides:       tex(jkposnbn8t.vf) = %{tl_version}, tex(jkposnbsc7t.vf) = %{tl_version}
Provides:       tex(jkposnbsc8t.vf) = %{tl_version}, tex(jkposnbscsl7t.vf) = %{tl_version}
Provides:       tex(jkposnbscsl8t.vf) = %{tl_version}, tex(jkposnbsl7t.vf) = %{tl_version}
Provides:       tex(jkposnbsl8t.vf) = %{tl_version}, tex(jkposnbxit7t.vf) = %{tl_version}
Provides:       tex(jkposnbxit8t.vf) = %{tl_version}, tex(jkposnbxn7t.vf) = %{tl_version}
Provides:       tex(jkposnbxn8t.vf) = %{tl_version}, tex(jkposnbxsc7t.vf) = %{tl_version}
Provides:       tex(jkposnbxsc8t.vf) = %{tl_version}, tex(jkposnbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkposnbxscsl8t.vf) = %{tl_version}, tex(jkposnbxsl7t.vf) = %{tl_version}
Provides:       tex(jkposnbxsl8t.vf) = %{tl_version}, tex(jkposnmit7t.vf) = %{tl_version}
Provides:       tex(jkposnmit8t.vf) = %{tl_version}, tex(jkposnmn7t.vf) = %{tl_version}
Provides:       tex(jkposnmn8t.vf) = %{tl_version}, tex(jkposnmsc7t.vf) = %{tl_version}
Provides:       tex(jkposnmsc8t.vf) = %{tl_version}, tex(jkposnmscsl7t.vf) = %{tl_version}
Provides:       tex(jkposnmscsl8t.vf) = %{tl_version}, tex(jkposnmsl7t.vf) = %{tl_version}
Provides:       tex(jkposnmsl8t.vf) = %{tl_version}, tex(jkpssbex.vf) = %{tl_version}
Provides:       tex(jkpssbmi.vf) = %{tl_version}, tex(jkpssbmia.vf) = %{tl_version}
Provides:       tex(jkpssbmif.vf) = %{tl_version}, tex(jkpssbn7c.vf) = %{tl_version}
Provides:       tex(jkpssbn7t.vf) = %{tl_version}, tex(jkpssbn8t.vf) = %{tl_version}
Provides:       tex(jkpssbsc7c.vf) = %{tl_version}, tex(jkpssbsc7t.vf) = %{tl_version}
Provides:       tex(jkpssbsc8t.vf) = %{tl_version}, tex(jkpssbscsl7c.vf) = %{tl_version}
Provides:       tex(jkpssbscsl7t.vf) = %{tl_version}, tex(jkpssbscsl8t.vf) = %{tl_version}
Provides:       tex(jkpssbsl7c.vf) = %{tl_version}, tex(jkpssbsl7t.vf) = %{tl_version}
Provides:       tex(jkpssbsl8t.vf) = %{tl_version}, tex(jkpssbsyb.vf) = %{tl_version}
Provides:       tex(jkpssbsybw.vf) = %{tl_version}, tex(jkpssbxn7c.vf) = %{tl_version}
Provides:       tex(jkpssbxn7t.vf) = %{tl_version}, tex(jkpssbxn8t.vf) = %{tl_version}
Provides:       tex(jkpssbxsc7c.vf) = %{tl_version}, tex(jkpssbxsc7t.vf) = %{tl_version}
Provides:       tex(jkpssbxsc8t.vf) = %{tl_version}, tex(jkpssbxscsl7c.vf) = %{tl_version}
Provides:       tex(jkpssbxscsl7t.vf) = %{tl_version}, tex(jkpssbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkpssbxsl7c.vf) = %{tl_version}, tex(jkpssbxsl7t.vf) = %{tl_version}
Provides:       tex(jkpssbxsl8t.vf) = %{tl_version}, tex(jkpssex.vf) = %{tl_version}
Provides:       tex(jkpssfbn7t.vf) = %{tl_version}, tex(jkpssfbn8t.vf) = %{tl_version}
Provides:       tex(jkpssfbsl7t.vf) = %{tl_version}, tex(jkpssfbsl8t.vf) = %{tl_version}
Provides:       tex(jkpssfbxn7t.vf) = %{tl_version}, tex(jkpssfbxn8t.vf) = %{tl_version}
Provides:       tex(jkpssfbxsl7t.vf) = %{tl_version}, tex(jkpssfbxsl8t.vf) = %{tl_version}
Provides:       tex(jkpssfmn7t.vf) = %{tl_version}, tex(jkpssfmn8t.vf) = %{tl_version}
Provides:       tex(jkpssfmsl7t.vf) = %{tl_version}, tex(jkpssfmsl8t.vf) = %{tl_version}
Provides:       tex(jkpssfosnbn7t.vf) = %{tl_version}, tex(jkpssfosnbn8t.vf) = %{tl_version}
Provides:       tex(jkpssfosnbsl7t.vf) = %{tl_version}, tex(jkpssfosnbsl8t.vf) = %{tl_version}
Provides:       tex(jkpssfosnbxn7t.vf) = %{tl_version}, tex(jkpssfosnbxn8t.vf) = %{tl_version}
Provides:       tex(jkpssfosnbxsl7t.vf) = %{tl_version}, tex(jkpssfosnbxsl8t.vf) = %{tl_version}
Provides:       tex(jkpssfosnmn7t.vf) = %{tl_version}, tex(jkpssfosnmn8t.vf) = %{tl_version}
Provides:       tex(jkpssfosnmsl7t.vf) = %{tl_version}, tex(jkpssfosnmsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskbsc7t.vf) = %{tl_version}, tex(jkpsskbsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskbscsl7t.vf) = %{tl_version}, tex(jkpsskbscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskbxsc7t.vf) = %{tl_version}, tex(jkpsskbxsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskbxscsl7t.vf) = %{tl_version}, tex(jkpsskbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskmsc7t.vf) = %{tl_version}, tex(jkpsskmsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskmscsl7t.vf) = %{tl_version}, tex(jkpsskmscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskosbsc7t.vf) = %{tl_version}, tex(jkpsskosbsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskosbscsl7t.vf) = %{tl_version}, tex(jkpsskosbscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskosbxsc7t.vf) = %{tl_version}, tex(jkpsskosbxsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskosbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkpsskosbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskosmsc7t.vf) = %{tl_version}, tex(jkpsskosmsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskosmscsl7t.vf) = %{tl_version}, tex(jkpsskosmscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskosnbsc7t.vf) = %{tl_version}, tex(jkpsskosnbsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskosnbscsl7t.vf) = %{tl_version}
Provides:       tex(jkpsskosnbscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskosnbxsc7t.vf) = %{tl_version}, tex(jkpsskosnbxsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskosnbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkpsskosnbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsskosnmsc7t.vf) = %{tl_version}, tex(jkpsskosnmsc8t.vf) = %{tl_version}
Provides:       tex(jkpsskosnmscsl7t.vf) = %{tl_version}
Provides:       tex(jkpsskosnmscsl8t.vf) = %{tl_version}
Provides:       tex(jkpsslbsyb.vf) = %{tl_version}, tex(jkpsslbsybw.vf) = %{tl_version}
Provides:       tex(jkpsslsyb.vf) = %{tl_version}, tex(jkpsslsybw.vf) = %{tl_version}
Provides:       tex(jkpssmi.vf) = %{tl_version}, tex(jkpssmia.vf) = %{tl_version}
Provides:       tex(jkpssmif.vf) = %{tl_version}, tex(jkpssmn7c.vf) = %{tl_version}
Provides:       tex(jkpssmn7t.vf) = %{tl_version}, tex(jkpssmn8t.vf) = %{tl_version}
Provides:       tex(jkpssmsc7c.vf) = %{tl_version}, tex(jkpssmsc7t.vf) = %{tl_version}
Provides:       tex(jkpssmsc8t.vf) = %{tl_version}, tex(jkpssmscsl7c.vf) = %{tl_version}
Provides:       tex(jkpssmscsl7t.vf) = %{tl_version}, tex(jkpssmscsl8t.vf) = %{tl_version}
Provides:       tex(jkpssmsl7c.vf) = %{tl_version}, tex(jkpssmsl7t.vf) = %{tl_version}
Provides:       tex(jkpssmsl8t.vf) = %{tl_version}, tex(jkpssosbn7t.vf) = %{tl_version}
Provides:       tex(jkpssosbn8t.vf) = %{tl_version}, tex(jkpssosbsc7t.vf) = %{tl_version}
Provides:       tex(jkpssosbsc8t.vf) = %{tl_version}, tex(jkpssosbscsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosbscsl8t.vf) = %{tl_version}, tex(jkpssosbsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosbsl8t.vf) = %{tl_version}, tex(jkpssosbxn7t.vf) = %{tl_version}
Provides:       tex(jkpssosbxn8t.vf) = %{tl_version}, tex(jkpssosbxsc7t.vf) = %{tl_version}
Provides:       tex(jkpssosbxsc8t.vf) = %{tl_version}, tex(jkpssosbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosbxscsl8t.vf) = %{tl_version}, tex(jkpssosbxsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosbxsl8t.vf) = %{tl_version}, tex(jkpssosmn7t.vf) = %{tl_version}
Provides:       tex(jkpssosmn8t.vf) = %{tl_version}, tex(jkpssosmsc7t.vf) = %{tl_version}
Provides:       tex(jkpssosmsc8t.vf) = %{tl_version}, tex(jkpssosmscsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosmscsl8t.vf) = %{tl_version}, tex(jkpssosmsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosmsl8t.vf) = %{tl_version}, tex(jkpssosnbn7t.vf) = %{tl_version}
Provides:       tex(jkpssosnbn8t.vf) = %{tl_version}, tex(jkpssosnbsc7t.vf) = %{tl_version}
Provides:       tex(jkpssosnbsc8t.vf) = %{tl_version}, tex(jkpssosnbscsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosnbscsl8t.vf) = %{tl_version}, tex(jkpssosnbsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosnbsl8t.vf) = %{tl_version}, tex(jkpssosnbxn7t.vf) = %{tl_version}
Provides:       tex(jkpssosnbxn8t.vf) = %{tl_version}, tex(jkpssosnbxsc7t.vf) = %{tl_version}
Provides:       tex(jkpssosnbxsc8t.vf) = %{tl_version}, tex(jkpssosnbxscsl7t.vf) = %{tl_version}
Provides:       tex(jkpssosnbxscsl8t.vf) = %{tl_version}
Provides:       tex(jkpssosnbxsl7t.vf) = %{tl_version}, tex(jkpssosnbxsl8t.vf) = %{tl_version}
Provides:       tex(jkpssosnmn7t.vf) = %{tl_version}, tex(jkpssosnmn8t.vf) = %{tl_version}
Provides:       tex(jkpssosnmsc7t.vf) = %{tl_version}, tex(jkpssosnmsc8t.vf) = %{tl_version}
Provides:       tex(jkpssosnmscsl7t.vf) = %{tl_version}, tex(jkpssosnmscsl8t.vf) = %{tl_version}
Provides:       tex(jkpssosnmsl7t.vf) = %{tl_version}, tex(jkpssosnmsl8t.vf) = %{tl_version}
Provides:       tex(jkpsssyb.vf) = %{tl_version}, tex(jkpsssybw.vf) = %{tl_version}
Provides:       tex(jkpssvosbmi.vf) = %{tl_version}, tex(jkpssvosbmif.vf) = %{tl_version}
Provides:       tex(jkpssvosbn7t.vf) = %{tl_version}, tex(jkpssvosbn8t.vf) = %{tl_version}
Provides:       tex(jkpssvosbsc7t.vf) = %{tl_version}, tex(jkpssvosbsc8t.vf) = %{tl_version}
Provides:       tex(jkpssvosbsl7t.vf) = %{tl_version}, tex(jkpssvosbsl8t.vf) = %{tl_version}
Provides:       tex(jkpssvosbxn7t.vf) = %{tl_version}, tex(jkpssvosbxn8t.vf) = %{tl_version}
Provides:       tex(jkpssvosbxsc7t.vf) = %{tl_version}, tex(jkpssvosbxsc8t.vf) = %{tl_version}
Provides:       tex(jkpssvosbxsl7t.vf) = %{tl_version}, tex(jkpssvosbxsl8t.vf) = %{tl_version}
Provides:       tex(jkpssvosmi.vf) = %{tl_version}, tex(jkpssvosmif.vf) = %{tl_version}
Provides:       tex(jkpssvosmn7t.vf) = %{tl_version}, tex(jkpssvosmn8t.vf) = %{tl_version}
Provides:       tex(jkpssvosmsc7t.vf) = %{tl_version}, tex(jkpssvosmsc8t.vf) = %{tl_version}
Provides:       tex(jkpssvosmsl7t.vf) = %{tl_version}, tex(jkpssvosmsl8t.vf) = %{tl_version}
Provides:       tex(jkpsybw.vf) = %{tl_version}, tex(jkpsydw.vf) = %{tl_version}
Provides:       tex(jkpsyw.vf) = %{tl_version}, tex(jkpttbn7c.vf) = %{tl_version}
Provides:       tex(jkpttbn7t.vf) = %{tl_version}, tex(jkpttbn8t.vf) = %{tl_version}
Provides:       tex(jkpttbsl7c.vf) = %{tl_version}, tex(jkpttbsl7t.vf) = %{tl_version}
Provides:       tex(jkpttbsl8t.vf) = %{tl_version}, tex(jkpttmn7c.vf) = %{tl_version}
Provides:       tex(jkpttmn7t.vf) = %{tl_version}, tex(jkpttmn8t.vf) = %{tl_version}
Provides:       tex(jkpttmsl7c.vf) = %{tl_version}, tex(jkpttmsl7t.vf) = %{tl_version}
Provides:       tex(jkpttmsl8t.vf) = %{tl_version}, tex(jkpttosbn7t.vf) = %{tl_version}
Provides:       tex(jkpttosbn8t.vf) = %{tl_version}, tex(jkpttosbsl7t.vf) = %{tl_version}
Provides:       tex(jkpttosbsl8t.vf) = %{tl_version}, tex(jkpttosmn7t.vf) = %{tl_version}
Provides:       tex(jkpttosmn8t.vf) = %{tl_version}, tex(jkpttosmsl7t.vf) = %{tl_version}
Provides:       tex(jkpttosmsl8t.vf) = %{tl_version}, tex(jkpttosnbn7t.vf) = %{tl_version}
Provides:       tex(jkpttosnbn8t.vf) = %{tl_version}, tex(jkpttosnbsl7t.vf) = %{tl_version}
Provides:       tex(jkpttosnbsl8t.vf) = %{tl_version}, tex(jkpttosnmn7t.vf) = %{tl_version}
Provides:       tex(jkpttosnmn8t.vf) = %{tl_version}, tex(jkpttosnmsl7t.vf) = %{tl_version}
Provides:       tex(jkpttosnmsl8t.vf) = %{tl_version}, tex(jkpttvosbn7t.vf) = %{tl_version}
Provides:       tex(jkpttvosbn8t.vf) = %{tl_version}, tex(jkpttvosbsl7t.vf) = %{tl_version}
Provides:       tex(jkpttvosbsl8t.vf) = %{tl_version}, tex(jkpttvosmn7t.vf) = %{tl_version}
Provides:       tex(jkpttvosmn8t.vf) = %{tl_version}, tex(jkpttvosmsl7t.vf) = %{tl_version}
Provides:       tex(jkpttvosmsl8t.vf) = %{tl_version}, tex(jkpvosbit7t.vf) = %{tl_version}
Provides:       tex(jkpvosbit8t.vf) = %{tl_version}, tex(jkpvosbmi.vf) = %{tl_version}
Provides:       tex(jkpvosbmif.vf) = %{tl_version}, tex(jkpvosbmifw.vf) = %{tl_version}
Provides:       tex(jkpvosbmiw.vf) = %{tl_version}, tex(jkpvosbn7t.vf) = %{tl_version}
Provides:       tex(jkpvosbn8t.vf) = %{tl_version}, tex(jkpvosbsl7t.vf) = %{tl_version}
Provides:       tex(jkpvosbsl8t.vf) = %{tl_version}, tex(jkpvosbxit7t.vf) = %{tl_version}
Provides:       tex(jkpvosbxit8t.vf) = %{tl_version}, tex(jkpvosbxn7t.vf) = %{tl_version}
Provides:       tex(jkpvosbxn8t.vf) = %{tl_version}, tex(jkpvosbxsl7t.vf) = %{tl_version}
Provides:       tex(jkpvosbxsl8t.vf) = %{tl_version}, tex(jkpvosmi.vf) = %{tl_version}
Provides:       tex(jkpvosmif.vf) = %{tl_version}, tex(jkpvosmifw.vf) = %{tl_version}
Provides:       tex(jkpvosmit7t.vf) = %{tl_version}, tex(jkpvosmit8t.vf) = %{tl_version}
Provides:       tex(jkpvosmiw.vf) = %{tl_version}, tex(jkpvosmn7t.vf) = %{tl_version}
Provides:       tex(jkpvosmn8t.vf) = %{tl_version}, tex(jkpvosmsl7t.vf) = %{tl_version}
Provides:       tex(jkpvosmsl8t.vf) = %{tl_version}, tex(kpfonts.sty) = %{tl_version}
Provides:       tex(omljkp.fd) = %{tl_version}, tex(omljkpl.fd) = %{tl_version}
Provides:       tex(omljkplvos.fd) = %{tl_version}, tex(omljkplvosw.fd) = %{tl_version}
Provides:       tex(omljkplw.fd) = %{tl_version}, tex(omljkpss.fd) = %{tl_version}
Provides:       tex(omljkpssvos.fd) = %{tl_version}, tex(omljkpvos.fd) = %{tl_version}
Provides:       tex(omljkpvosw.fd) = %{tl_version}, tex(omljkpw.fd) = %{tl_version}
Provides:       tex(omsjkp.fd) = %{tl_version}, tex(omsjkpl.fd) = %{tl_version}
Provides:       tex(omsjkplw.fd) = %{tl_version}, tex(omsjkpw.fd) = %{tl_version}
Provides:       tex(omxjkp.fd) = %{tl_version}, tex(omxjkpl.fd) = %{tl_version}
Provides:       tex(omxjkpss.fd) = %{tl_version}, tex(ot1jkp.fd) = %{tl_version}
Provides:       tex(ot1jkpf.fd) = %{tl_version}, tex(ot1jkpfosn.fd) = %{tl_version}
Provides:       tex(ot1jkpk.fd) = %{tl_version}, tex(ot1jkpkf.fd) = %{tl_version}
Provides:       tex(ot1jkpkfosn.fd) = %{tl_version}, tex(ot1jkpkos.fd) = %{tl_version}
Provides:       tex(ot1jkpkosn.fd) = %{tl_version}, tex(ot1jkpkvos.fd) = %{tl_version}
Provides:       tex(ot1jkpl.fd) = %{tl_version}, tex(ot1jkplf.fd) = %{tl_version}
Provides:       tex(ot1jkplfosn.fd) = %{tl_version}, tex(ot1jkplk.fd) = %{tl_version}
Provides:       tex(ot1jkplkf.fd) = %{tl_version}, tex(ot1jkplkfosn.fd) = %{tl_version}
Provides:       tex(ot1jkplkos.fd) = %{tl_version}, tex(ot1jkplkosn.fd) = %{tl_version}
Provides:       tex(ot1jkplkvos.fd) = %{tl_version}, tex(ot1jkplos.fd) = %{tl_version}
Provides:       tex(ot1jkplosn.fd) = %{tl_version}, tex(ot1jkplvos.fd) = %{tl_version}
Provides:       tex(ot1jkpos.fd) = %{tl_version}, tex(ot1jkposn.fd) = %{tl_version}
Provides:       tex(ot1jkpss.fd) = %{tl_version}, tex(ot1jkpssf.fd) = %{tl_version}
Provides:       tex(ot1jkpssfosn.fd) = %{tl_version}, tex(ot1jkpssk.fd) = %{tl_version}
Provides:       tex(ot1jkpsskf.fd) = %{tl_version}, tex(ot1jkpsskfosn.fd) = %{tl_version}
Provides:       tex(ot1jkpsskos.fd) = %{tl_version}, tex(ot1jkpsskosn.fd) = %{tl_version}
Provides:       tex(ot1jkpsskvos.fd) = %{tl_version}, tex(ot1jkpssos.fd) = %{tl_version}
Provides:       tex(ot1jkpssosn.fd) = %{tl_version}, tex(ot1jkpssvos.fd) = %{tl_version}
Provides:       tex(ot1jkptt.fd) = %{tl_version}, tex(ot1jkpttos.fd) = %{tl_version}
Provides:       tex(ot1jkpttosn.fd) = %{tl_version}, tex(ot1jkpttvos.fd) = %{tl_version}
Provides:       tex(ot1jkpvos.fd) = %{tl_version}, tex(ot1jkpx.fd) = %{tl_version}
Provides:       tex(ot1jkpxf.fd) = %{tl_version}, tex(ot1jkpxfosn.fd) = %{tl_version}
Provides:       tex(ot1jkpxk.fd) = %{tl_version}, tex(ot1jkpxkf.fd) = %{tl_version}
Provides:       tex(ot1jkpxkfosn.fd) = %{tl_version}, tex(ot1jkpxkos.fd) = %{tl_version}
Provides:       tex(ot1jkpxkosn.fd) = %{tl_version}, tex(ot1jkpxkvos.fd) = %{tl_version}
Provides:       tex(ot1jkpxos.fd) = %{tl_version}, tex(ot1jkpxosn.fd) = %{tl_version}
Provides:       tex(ot1jkpxvos.fd) = %{tl_version}, tex(t1jkp.fd) = %{tl_version}
Provides:       tex(t1jkpf.fd) = %{tl_version}, tex(t1jkpfosn.fd) = %{tl_version}
Provides:       tex(t1jkpk.fd) = %{tl_version}, tex(t1jkpkf.fd) = %{tl_version}
Provides:       tex(t1jkpkfosn.fd) = %{tl_version}, tex(t1jkpkos.fd) = %{tl_version}
Provides:       tex(t1jkpkosn.fd) = %{tl_version}, tex(t1jkpkvos.fd) = %{tl_version}
Provides:       tex(t1jkpl.fd) = %{tl_version}, tex(t1jkplf.fd) = %{tl_version}
Provides:       tex(t1jkplfosn.fd) = %{tl_version}, tex(t1jkplk.fd) = %{tl_version}
Provides:       tex(t1jkplkf.fd) = %{tl_version}, tex(t1jkplkfosn.fd) = %{tl_version}
Provides:       tex(t1jkplkos.fd) = %{tl_version}, tex(t1jkplkosn.fd) = %{tl_version}
Provides:       tex(t1jkplkvos.fd) = %{tl_version}, tex(t1jkplos.fd) = %{tl_version}
Provides:       tex(t1jkplosn.fd) = %{tl_version}, tex(t1jkplvos.fd) = %{tl_version}
Provides:       tex(t1jkpos.fd) = %{tl_version}, tex(t1jkposn.fd) = %{tl_version}
Provides:       tex(t1jkpss.fd) = %{tl_version}, tex(t1jkpssf.fd) = %{tl_version}
Provides:       tex(t1jkpssfosn.fd) = %{tl_version}, tex(t1jkpssk.fd) = %{tl_version}
Provides:       tex(t1jkpsskf.fd) = %{tl_version}, tex(t1jkpsskfosn.fd) = %{tl_version}
Provides:       tex(t1jkpsskos.fd) = %{tl_version}, tex(t1jkpsskosn.fd) = %{tl_version}
Provides:       tex(t1jkpsskvos.fd) = %{tl_version}, tex(t1jkpssos.fd) = %{tl_version}
Provides:       tex(t1jkpssosn.fd) = %{tl_version}, tex(t1jkpssvos.fd) = %{tl_version}
Provides:       tex(t1jkptt.fd) = %{tl_version}, tex(t1jkpttos.fd) = %{tl_version}
Provides:       tex(t1jkpttosn.fd) = %{tl_version}, tex(t1jkpttvos.fd) = %{tl_version}
Provides:       tex(t1jkpvos.fd) = %{tl_version}, tex(t1jkpx.fd) = %{tl_version}
Provides:       tex(t1jkpxf.fd) = %{tl_version}, tex(t1jkpxfosn.fd) = %{tl_version}
Provides:       tex(t1jkpxk.fd) = %{tl_version}, tex(t1jkpxkf.fd) = %{tl_version}
Provides:       tex(t1jkpxkfosn.fd) = %{tl_version}, tex(t1jkpxkos.fd) = %{tl_version}
Provides:       tex(t1jkpxkosn.fd) = %{tl_version}, tex(t1jkpxkvos.fd) = %{tl_version}
Provides:       tex(t1jkpxos.fd) = %{tl_version}, tex(t1jkpxosn.fd) = %{tl_version}
Provides:       tex(t1jkpxvos.fd) = %{tl_version}, tex(ts1jkp.fd) = %{tl_version}
Provides:       tex(ts1jkpf.fd) = %{tl_version}, tex(ts1jkpfosn.fd) = %{tl_version}
Provides:       tex(ts1jkpk.fd) = %{tl_version}, tex(ts1jkpkf.fd) = %{tl_version}
Provides:       tex(ts1jkpkfosn.fd) = %{tl_version}, tex(ts1jkpkos.fd) = %{tl_version}
Provides:       tex(ts1jkpkosn.fd) = %{tl_version}, tex(ts1jkpkvos.fd) = %{tl_version}
Provides:       tex(ts1jkpl.fd) = %{tl_version}, tex(ts1jkplf.fd) = %{tl_version}
Provides:       tex(ts1jkplfosn.fd) = %{tl_version}, tex(ts1jkplk.fd) = %{tl_version}
Provides:       tex(ts1jkplkf.fd) = %{tl_version}, tex(ts1jkplkfosn.fd) = %{tl_version}
Provides:       tex(ts1jkplkos.fd) = %{tl_version}, tex(ts1jkplkosn.fd) = %{tl_version}
Provides:       tex(ts1jkplkvos.fd) = %{tl_version}, tex(ts1jkplos.fd) = %{tl_version}
Provides:       tex(ts1jkplosn.fd) = %{tl_version}, tex(ts1jkplvos.fd) = %{tl_version}
Provides:       tex(ts1jkpos.fd) = %{tl_version}, tex(ts1jkposn.fd) = %{tl_version}
Provides:       tex(ts1jkpss.fd) = %{tl_version}, tex(ts1jkpssf.fd) = %{tl_version}
Provides:       tex(ts1jkpssfosn.fd) = %{tl_version}, tex(ts1jkpssk.fd) = %{tl_version}
Provides:       tex(ts1jkpsskf.fd) = %{tl_version}, tex(ts1jkpsskfosn.fd) = %{tl_version}
Provides:       tex(ts1jkpsskos.fd) = %{tl_version}, tex(ts1jkpsskosn.fd) = %{tl_version}
Provides:       tex(ts1jkpsskvos.fd) = %{tl_version}, tex(ts1jkpssos.fd) = %{tl_version}
Provides:       tex(ts1jkpssosn.fd) = %{tl_version}, tex(ts1jkpssvos.fd) = %{tl_version}
Provides:       tex(ts1jkptt.fd) = %{tl_version}, tex(ts1jkpttos.fd) = %{tl_version}
Provides:       tex(ts1jkpttosn.fd) = %{tl_version}, tex(ts1jkpttvos.fd) = %{tl_version}
Provides:       tex(ts1jkpvos.fd) = %{tl_version}, tex(ts1jkpx.fd) = %{tl_version}
Provides:       tex(ts1jkpxf.fd) = %{tl_version}, tex(ts1jkpxfosn.fd) = %{tl_version}
Provides:       tex(ts1jkpxk.fd) = %{tl_version}, tex(ts1jkpxkf.fd) = %{tl_version}
Provides:       tex(ts1jkpxkfosn.fd) = %{tl_version}, tex(ts1jkpxkos.fd) = %{tl_version}
Provides:       tex(ts1jkpxkosn.fd) = %{tl_version}, tex(ts1jkpxkvos.fd) = %{tl_version}
Provides:       tex(ts1jkpxos.fd) = %{tl_version}, tex(ts1jkpxosn.fd) = %{tl_version}
Provides:       tex(ts1jkpxvos.fd) = %{tl_version}, tex(ujkpexa.fd) = %{tl_version}
Provides:       tex(ujkplexa.fd) = %{tl_version}, tex(ujkplmia.fd) = %{tl_version}
Provides:       tex(ujkplmiaw.fd) = %{tl_version}, tex(ujkplsyb.fd) = %{tl_version}
Provides:       tex(ujkplsybw.fd) = %{tl_version}, tex(ujkplsyc.fd) = %{tl_version}
Provides:       tex(ujkplsyd.fd) = %{tl_version}, tex(ujkplsydw.fd) = %{tl_version}
Provides:       tex(ujkpmia.fd) = %{tl_version}, tex(ujkpmiaw.fd) = %{tl_version}
Provides:       tex(ujkpsslsyb.fd) = %{tl_version}, tex(ujkpsslsybw.fd) = %{tl_version}
Provides:       tex(ujkpssmia.fd) = %{tl_version}, tex(ujkpsssyb.fd) = %{tl_version}
Provides:       tex(ujkpsssybw.fd) = %{tl_version}, tex(ujkpsya.fd) = %{tl_version}
Provides:       tex(ujkpsyb.fd) = %{tl_version}, tex(ujkpsybw.fd) = %{tl_version}
Provides:       tex(ujkpsyc.fd) = %{tl_version}, tex(ujkpsyd.fd) = %{tl_version}
Provides:       tex(ujkpsydw.fd) = %{tl_version}

%description -n texlive-kpfonts
The family contains text fonts in roman, sans-serif and
monospaced shapes, with true small caps and old-style numbers;
the package offers full support of the textcomp package. The
mathematics fonts include all the AMS fonts, in both normal and
bold weights. Each of the font types is available in two main
versions: default and 'light'. Each version is available in
four variants: default; oldstyle numbers; oldstyle numbers with
old ligatures such as ct and st, and long-tailed capital Q; and
veryoldstyle with long s. Other variants include small caps as
default or 'large small caps', and for mathematics both upright
and slanted shapes for Greek letters, as well as default and
narrow versions of multiple integrals. The fonts were
originally derived from URW Palladio (with URW's agreement)
though the fonts are very clearly different in appearance from
their parent.

%package -n texlive-kpfonts-doc
Summary:        Documentation for kpfonts
Version:        svn29803.3.31

Provides:       tex-kpfonts-doc
AutoReqProv:    No

%description -n texlive-kpfonts-doc
Documentation for kpfonts

%package -n texlive-kurier
Provides:       tex-kurier = %{tl_version}
License:        GFSL
Summary:        A two-element sans-serif typeface
Version:        svn19612.0.995b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(cs-kurier-sc.enc) = %{tl_version}, tex(cs-kurier.enc) = %{tl_version}
Provides:       tex(ec-kurier-sc.enc) = %{tl_version}, tex(ec-kurier.enc) = %{tl_version}
Provides:       tex(ex-kurier.enc) = %{tl_version}, tex(greek-kurier.enc) = %{tl_version}
Provides:       tex(l7x-kurier-sc.enc) = %{tl_version}, tex(l7x-kurier.enc) = %{tl_version}
Provides:       tex(mi-kurier.enc) = %{tl_version}, tex(qx-kurier-sc.enc) = %{tl_version}
Provides:       tex(qx-kurier.enc) = %{tl_version}, tex(rm-kurier-sc.enc) = %{tl_version}
Provides:       tex(rm-kurier.enc) = %{tl_version}, tex(sy-kurier.enc) = %{tl_version}
Provides:       tex(t2a-kurier.enc) = %{tl_version}, tex(t2b-kurier.enc) = %{tl_version}
Provides:       tex(t2c-kurier.enc) = %{tl_version}, tex(t5-kurier-sc.enc) = %{tl_version}
Provides:       tex(t5-kurier.enc) = %{tl_version}, tex(texnansi-kurier-sc.enc) = %{tl_version}
Provides:       tex(texnansi-kurier.enc) = %{tl_version}
Provides:       tex(ts1-kurier.enc) = %{tl_version}, tex(wncy-kurier.enc) = %{tl_version}
Provides:       tex(kurier-cs.map) = %{tl_version}, tex(kurier-ec.map) = %{tl_version}
Provides:       tex(kurier-ex.map) = %{tl_version}, tex(kurier-greek.map) = %{tl_version}
Provides:       tex(kurier-l7x.map) = %{tl_version}, tex(kurier-mi.map) = %{tl_version}
Provides:       tex(kurier-qx.map) = %{tl_version}, tex(kurier-rm.map) = %{tl_version}
Provides:       tex(kurier-sy.map) = %{tl_version}, tex(kurier-t2a.map) = %{tl_version}
Provides:       tex(kurier-t2b.map) = %{tl_version}, tex(kurier-t2c.map) = %{tl_version}
Provides:       tex(kurier-t5.map) = %{tl_version}, tex(kurier-texnansi.map) = %{tl_version}
Provides:       tex(kurier-ts1.map) = %{tl_version}, tex(kurier-wncy.map) = %{tl_version}
Provides:       tex(kurier.map) = %{tl_version}, tex(Kurier-Bold.otf) = %{tl_version}
Provides:       tex(Kurier-BoldItalic.otf) = %{tl_version}
Provides:       tex(Kurier-Italic.otf) = %{tl_version}, tex(Kurier-Regular.otf) = %{tl_version}
Provides:       tex(KurierCond-Bold.otf) = %{tl_version}
Provides:       tex(KurierCond-BoldItalic.otf) = %{tl_version}
Provides:       tex(KurierCond-Italic.otf) = %{tl_version}
Provides:       tex(KurierCond-Regular.otf) = %{tl_version}
Provides:       tex(KurierCondHeavy-Italic.otf) = %{tl_version}
Provides:       tex(KurierCondHeavy-Regular.otf) = %{tl_version}
Provides:       tex(KurierCondLight-Italic.otf) = %{tl_version}
Provides:       tex(KurierCondLight-Regular.otf) = %{tl_version}
Provides:       tex(KurierCondMedium-Italic.otf) = %{tl_version}
Provides:       tex(KurierCondMedium-Regular.otf) = %{tl_version}
Provides:       tex(KurierHeavy-Italic.otf) = %{tl_version}
Provides:       tex(KurierHeavy-Regular.otf) = %{tl_version}
Provides:       tex(KurierLight-Italic.otf) = %{tl_version}
Provides:       tex(KurierLight-Regular.otf) = %{tl_version}
Provides:       tex(KurierMedium-Italic.otf) = %{tl_version}
Provides:       tex(KurierMedium-Regular.otf) = %{tl_version}
Provides:       tex(cs-kurierb-sc.tfm) = %{tl_version}, tex(cs-kurierb.tfm) = %{tl_version}
Provides:       tex(cs-kurierbi-sc.tfm) = %{tl_version}, tex(cs-kurierbi.tfm) = %{tl_version}
Provides:       tex(cs-kuriercb-sc.tfm) = %{tl_version}, tex(cs-kuriercb.tfm) = %{tl_version}
Provides:       tex(cs-kuriercbi-sc.tfm) = %{tl_version}
Provides:       tex(cs-kuriercbi.tfm) = %{tl_version}, tex(cs-kurierch-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierch.tfm) = %{tl_version}, tex(cs-kurierchi-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierchi.tfm) = %{tl_version}, tex(cs-kuriercl-sc.tfm) = %{tl_version}
Provides:       tex(cs-kuriercl.tfm) = %{tl_version}, tex(cs-kuriercli-sc.tfm) = %{tl_version}
Provides:       tex(cs-kuriercli.tfm) = %{tl_version}, tex(cs-kuriercm-sc.tfm) = %{tl_version}
Provides:       tex(cs-kuriercm.tfm) = %{tl_version}, tex(cs-kuriercmi-sc.tfm) = %{tl_version}
Provides:       tex(cs-kuriercmi.tfm) = %{tl_version}, tex(cs-kuriercr-sc.tfm) = %{tl_version}
Provides:       tex(cs-kuriercr.tfm) = %{tl_version}, tex(cs-kuriercri-sc.tfm) = %{tl_version}
Provides:       tex(cs-kuriercri.tfm) = %{tl_version}, tex(cs-kurierh-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierh.tfm) = %{tl_version}, tex(cs-kurierhi-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierhi.tfm) = %{tl_version}, tex(cs-kurierl-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierl.tfm) = %{tl_version}, tex(cs-kurierli-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierli.tfm) = %{tl_version}, tex(cs-kurierm-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierm.tfm) = %{tl_version}, tex(cs-kuriermi-sc.tfm) = %{tl_version}
Provides:       tex(cs-kuriermi.tfm) = %{tl_version}, tex(cs-kurierr-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierr.tfm) = %{tl_version}, tex(cs-kurierri-sc.tfm) = %{tl_version}
Provides:       tex(cs-kurierri.tfm) = %{tl_version}, tex(ec-kurierb-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierb.tfm) = %{tl_version}, tex(ec-kurierbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierbi.tfm) = %{tl_version}, tex(ec-kuriercb-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriercb.tfm) = %{tl_version}, tex(ec-kuriercbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriercbi.tfm) = %{tl_version}, tex(ec-kurierch-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierch.tfm) = %{tl_version}, tex(ec-kurierchi-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierchi.tfm) = %{tl_version}, tex(ec-kuriercl-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriercl.tfm) = %{tl_version}, tex(ec-kuriercli-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriercli.tfm) = %{tl_version}, tex(ec-kuriercm-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriercm.tfm) = %{tl_version}, tex(ec-kuriercmi-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriercmi.tfm) = %{tl_version}, tex(ec-kuriercr-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriercr.tfm) = %{tl_version}, tex(ec-kuriercri-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriercri.tfm) = %{tl_version}, tex(ec-kurierh-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierh.tfm) = %{tl_version}, tex(ec-kurierhi-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierhi.tfm) = %{tl_version}, tex(ec-kurierl-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierl.tfm) = %{tl_version}, tex(ec-kurierli-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierli.tfm) = %{tl_version}, tex(ec-kurierm-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierm.tfm) = %{tl_version}, tex(ec-kuriermi-sc.tfm) = %{tl_version}
Provides:       tex(ec-kuriermi.tfm) = %{tl_version}, tex(ec-kurierr-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierr.tfm) = %{tl_version}, tex(ec-kurierri-sc.tfm) = %{tl_version}
Provides:       tex(ec-kurierri.tfm) = %{tl_version}, tex(ex-kurierb.tfm) = %{tl_version}
Provides:       tex(ex-kuriercb.tfm) = %{tl_version}, tex(ex-kurierch.tfm) = %{tl_version}
Provides:       tex(ex-kuriercl.tfm) = %{tl_version}, tex(ex-kuriercm.tfm) = %{tl_version}
Provides:       tex(ex-kuriercr.tfm) = %{tl_version}, tex(ex-kurierh.tfm) = %{tl_version}
Provides:       tex(ex-kurierl.tfm) = %{tl_version}, tex(ex-kurierm.tfm) = %{tl_version}
Provides:       tex(ex-kurierr.tfm) = %{tl_version}, tex(greek-kurierb.tfm) = %{tl_version}
Provides:       tex(greek-kurierbi.tfm) = %{tl_version}, tex(greek-kuriercb.tfm) = %{tl_version}
Provides:       tex(greek-kuriercbi.tfm) = %{tl_version}
Provides:       tex(greek-kurierch.tfm) = %{tl_version}, tex(greek-kurierchi.tfm) = %{tl_version}
Provides:       tex(greek-kuriercl.tfm) = %{tl_version}, tex(greek-kuriercli.tfm) = %{tl_version}
Provides:       tex(greek-kuriercm.tfm) = %{tl_version}, tex(greek-kuriercmi.tfm) = %{tl_version}
Provides:       tex(greek-kuriercr.tfm) = %{tl_version}, tex(greek-kuriercri.tfm) = %{tl_version}
Provides:       tex(greek-kurierh.tfm) = %{tl_version}, tex(greek-kurierhi.tfm) = %{tl_version}
Provides:       tex(greek-kurierl.tfm) = %{tl_version}, tex(greek-kurierli.tfm) = %{tl_version}
Provides:       tex(greek-kurierm.tfm) = %{tl_version}, tex(greek-kuriermi.tfm) = %{tl_version}
Provides:       tex(greek-kurierr.tfm) = %{tl_version}, tex(greek-kurierri.tfm) = %{tl_version}
Provides:       tex(l7x-kurierb-sc.tfm) = %{tl_version}, tex(l7x-kurierb.tfm) = %{tl_version}
Provides:       tex(l7x-kurierbi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierbi.tfm) = %{tl_version}, tex(l7x-kuriercb-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriercb.tfm) = %{tl_version}, tex(l7x-kuriercbi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriercbi.tfm) = %{tl_version}, tex(l7x-kurierch-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierch.tfm) = %{tl_version}, tex(l7x-kurierchi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierchi.tfm) = %{tl_version}, tex(l7x-kuriercl-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriercl.tfm) = %{tl_version}, tex(l7x-kuriercli-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriercli.tfm) = %{tl_version}, tex(l7x-kuriercm-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriercm.tfm) = %{tl_version}, tex(l7x-kuriercmi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriercmi.tfm) = %{tl_version}, tex(l7x-kuriercr-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriercr.tfm) = %{tl_version}, tex(l7x-kuriercri-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriercri.tfm) = %{tl_version}, tex(l7x-kurierh-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierh.tfm) = %{tl_version}, tex(l7x-kurierhi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierhi.tfm) = %{tl_version}, tex(l7x-kurierl-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierl.tfm) = %{tl_version}, tex(l7x-kurierli-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierli.tfm) = %{tl_version}, tex(l7x-kurierm-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierm.tfm) = %{tl_version}, tex(l7x-kuriermi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kuriermi.tfm) = %{tl_version}, tex(l7x-kurierr-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierr.tfm) = %{tl_version}, tex(l7x-kurierri-sc.tfm) = %{tl_version}
Provides:       tex(l7x-kurierri.tfm) = %{tl_version}, tex(mi-kurierbi.tfm) = %{tl_version}
Provides:       tex(mi-kuriercbi.tfm) = %{tl_version}, tex(mi-kurierchi.tfm) = %{tl_version}
Provides:       tex(mi-kuriercli.tfm) = %{tl_version}, tex(mi-kuriercmi.tfm) = %{tl_version}
Provides:       tex(mi-kuriercri.tfm) = %{tl_version}, tex(mi-kurierhi.tfm) = %{tl_version}
Provides:       tex(mi-kurierli.tfm) = %{tl_version}, tex(mi-kuriermi.tfm) = %{tl_version}
Provides:       tex(mi-kurierri.tfm) = %{tl_version}, tex(qx-kurierb-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierb.tfm) = %{tl_version}, tex(qx-kurierbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierbi.tfm) = %{tl_version}, tex(qx-kuriercb-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriercb.tfm) = %{tl_version}, tex(qx-kuriercbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriercbi.tfm) = %{tl_version}, tex(qx-kurierch-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierch.tfm) = %{tl_version}, tex(qx-kurierchi-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierchi.tfm) = %{tl_version}, tex(qx-kuriercl-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriercl.tfm) = %{tl_version}, tex(qx-kuriercli-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriercli.tfm) = %{tl_version}, tex(qx-kuriercm-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriercm.tfm) = %{tl_version}, tex(qx-kuriercmi-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriercmi.tfm) = %{tl_version}, tex(qx-kuriercr-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriercr.tfm) = %{tl_version}, tex(qx-kuriercri-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriercri.tfm) = %{tl_version}, tex(qx-kurierh-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierh.tfm) = %{tl_version}, tex(qx-kurierhi-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierhi.tfm) = %{tl_version}, tex(qx-kurierl-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierl.tfm) = %{tl_version}, tex(qx-kurierli-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierli.tfm) = %{tl_version}, tex(qx-kurierm-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierm.tfm) = %{tl_version}, tex(qx-kuriermi-sc.tfm) = %{tl_version}
Provides:       tex(qx-kuriermi.tfm) = %{tl_version}, tex(qx-kurierr-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierr.tfm) = %{tl_version}, tex(qx-kurierri-sc.tfm) = %{tl_version}
Provides:       tex(qx-kurierri.tfm) = %{tl_version}, tex(rm-kurierb-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierb.tfm) = %{tl_version}, tex(rm-kurierbi-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierbi.tfm) = %{tl_version}, tex(rm-kuriercb-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriercb.tfm) = %{tl_version}, tex(rm-kuriercbi-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriercbi.tfm) = %{tl_version}, tex(rm-kurierch-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierch.tfm) = %{tl_version}, tex(rm-kurierchi-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierchi.tfm) = %{tl_version}, tex(rm-kuriercl-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriercl.tfm) = %{tl_version}, tex(rm-kuriercli-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriercli.tfm) = %{tl_version}, tex(rm-kuriercm-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriercm.tfm) = %{tl_version}, tex(rm-kuriercmi-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriercmi.tfm) = %{tl_version}, tex(rm-kuriercr-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriercr.tfm) = %{tl_version}, tex(rm-kuriercri-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriercri.tfm) = %{tl_version}, tex(rm-kurierh-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierh.tfm) = %{tl_version}, tex(rm-kurierhi-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierhi.tfm) = %{tl_version}, tex(rm-kurierl-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierl.tfm) = %{tl_version}, tex(rm-kurierli-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierli.tfm) = %{tl_version}, tex(rm-kurierm-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierm.tfm) = %{tl_version}, tex(rm-kuriermi-sc.tfm) = %{tl_version}
Provides:       tex(rm-kuriermi.tfm) = %{tl_version}, tex(rm-kurierr-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierr.tfm) = %{tl_version}, tex(rm-kurierri-sc.tfm) = %{tl_version}
Provides:       tex(rm-kurierri.tfm) = %{tl_version}, tex(sy-kurierbz.tfm) = %{tl_version}
Provides:       tex(sy-kuriercbz.tfm) = %{tl_version}, tex(sy-kurierchz.tfm) = %{tl_version}
Provides:       tex(sy-kurierclz.tfm) = %{tl_version}, tex(sy-kuriercmz.tfm) = %{tl_version}
Provides:       tex(sy-kuriercrz.tfm) = %{tl_version}, tex(sy-kurierhz.tfm) = %{tl_version}
Provides:       tex(sy-kurierlz.tfm) = %{tl_version}, tex(sy-kuriermz.tfm) = %{tl_version}
Provides:       tex(sy-kurierrz.tfm) = %{tl_version}, tex(t2a-kurierb.tfm) = %{tl_version}
Provides:       tex(t2a-kurierbi.tfm) = %{tl_version}, tex(t2a-kuriercb.tfm) = %{tl_version}
Provides:       tex(t2a-kuriercbi.tfm) = %{tl_version}, tex(t2a-kurierch.tfm) = %{tl_version}
Provides:       tex(t2a-kurierchi.tfm) = %{tl_version}, tex(t2a-kuriercl.tfm) = %{tl_version}
Provides:       tex(t2a-kuriercli.tfm) = %{tl_version}, tex(t2a-kuriercm.tfm) = %{tl_version}
Provides:       tex(t2a-kuriercmi.tfm) = %{tl_version}, tex(t2a-kuriercr.tfm) = %{tl_version}
Provides:       tex(t2a-kuriercri.tfm) = %{tl_version}, tex(t2a-kurierh.tfm) = %{tl_version}
Provides:       tex(t2a-kurierhi.tfm) = %{tl_version}, tex(t2a-kurierl.tfm) = %{tl_version}
Provides:       tex(t2a-kurierli.tfm) = %{tl_version}, tex(t2a-kurierm.tfm) = %{tl_version}
Provides:       tex(t2a-kuriermi.tfm) = %{tl_version}, tex(t2a-kurierr.tfm) = %{tl_version}
Provides:       tex(t2a-kurierri.tfm) = %{tl_version}, tex(t2b-kurierb.tfm) = %{tl_version}
Provides:       tex(t2b-kurierbi.tfm) = %{tl_version}, tex(t2b-kuriercb.tfm) = %{tl_version}
Provides:       tex(t2b-kuriercbi.tfm) = %{tl_version}, tex(t2b-kurierch.tfm) = %{tl_version}
Provides:       tex(t2b-kurierchi.tfm) = %{tl_version}, tex(t2b-kuriercl.tfm) = %{tl_version}
Provides:       tex(t2b-kuriercli.tfm) = %{tl_version}, tex(t2b-kuriercm.tfm) = %{tl_version}
Provides:       tex(t2b-kuriercmi.tfm) = %{tl_version}, tex(t2b-kuriercr.tfm) = %{tl_version}
Provides:       tex(t2b-kuriercri.tfm) = %{tl_version}, tex(t2b-kurierh.tfm) = %{tl_version}
Provides:       tex(t2b-kurierhi.tfm) = %{tl_version}, tex(t2b-kurierl.tfm) = %{tl_version}
Provides:       tex(t2b-kurierli.tfm) = %{tl_version}, tex(t2b-kurierm.tfm) = %{tl_version}
Provides:       tex(t2b-kuriermi.tfm) = %{tl_version}, tex(t2b-kurierr.tfm) = %{tl_version}
Provides:       tex(t2b-kurierri.tfm) = %{tl_version}, tex(t2c-kurierb.tfm) = %{tl_version}
Provides:       tex(t2c-kurierbi.tfm) = %{tl_version}, tex(t2c-kuriercb.tfm) = %{tl_version}
Provides:       tex(t2c-kuriercbi.tfm) = %{tl_version}, tex(t2c-kurierch.tfm) = %{tl_version}
Provides:       tex(t2c-kurierchi.tfm) = %{tl_version}, tex(t2c-kuriercl.tfm) = %{tl_version}
Provides:       tex(t2c-kuriercli.tfm) = %{tl_version}, tex(t2c-kuriercm.tfm) = %{tl_version}
Provides:       tex(t2c-kuriercmi.tfm) = %{tl_version}, tex(t2c-kuriercr.tfm) = %{tl_version}
Provides:       tex(t2c-kuriercri.tfm) = %{tl_version}, tex(t2c-kurierh.tfm) = %{tl_version}
Provides:       tex(t2c-kurierhi.tfm) = %{tl_version}, tex(t2c-kurierl.tfm) = %{tl_version}
Provides:       tex(t2c-kurierli.tfm) = %{tl_version}, tex(t2c-kurierm.tfm) = %{tl_version}
Provides:       tex(t2c-kuriermi.tfm) = %{tl_version}, tex(t2c-kurierr.tfm) = %{tl_version}
Provides:       tex(t2c-kurierri.tfm) = %{tl_version}, tex(t5-kurierb-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierb.tfm) = %{tl_version}, tex(t5-kurierbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierbi.tfm) = %{tl_version}, tex(t5-kuriercb-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriercb.tfm) = %{tl_version}, tex(t5-kuriercbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriercbi.tfm) = %{tl_version}, tex(t5-kurierch-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierch.tfm) = %{tl_version}, tex(t5-kurierchi-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierchi.tfm) = %{tl_version}, tex(t5-kuriercl-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriercl.tfm) = %{tl_version}, tex(t5-kuriercli-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriercli.tfm) = %{tl_version}, tex(t5-kuriercm-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriercm.tfm) = %{tl_version}, tex(t5-kuriercmi-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriercmi.tfm) = %{tl_version}, tex(t5-kuriercr-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriercr.tfm) = %{tl_version}, tex(t5-kuriercri-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriercri.tfm) = %{tl_version}, tex(t5-kurierh-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierh.tfm) = %{tl_version}, tex(t5-kurierhi-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierhi.tfm) = %{tl_version}, tex(t5-kurierl-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierl.tfm) = %{tl_version}, tex(t5-kurierli-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierli.tfm) = %{tl_version}, tex(t5-kurierm-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierm.tfm) = %{tl_version}, tex(t5-kuriermi-sc.tfm) = %{tl_version}
Provides:       tex(t5-kuriermi.tfm) = %{tl_version}, tex(t5-kurierr-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierr.tfm) = %{tl_version}, tex(t5-kurierri-sc.tfm) = %{tl_version}
Provides:       tex(t5-kurierri.tfm) = %{tl_version}, tex(texnansi-kurierb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierb.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierbi.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercb.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercbi.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierch-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierch.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierchi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierchi.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercl-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercl.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercli-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercli.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercm-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercm.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercmi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercmi.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercr.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriercri.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierh-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierh.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierhi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierhi.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierl-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierl.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierli-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierli.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierm-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierm.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriermi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kuriermi.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierr.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-kurierri.tfm) = %{tl_version}
Provides:       tex(ts1-kurierb.tfm) = %{tl_version}, tex(ts1-kurierbi.tfm) = %{tl_version}
Provides:       tex(ts1-kuriercb.tfm) = %{tl_version}, tex(ts1-kuriercbi.tfm) = %{tl_version}
Provides:       tex(ts1-kurierch.tfm) = %{tl_version}, tex(ts1-kurierchi.tfm) = %{tl_version}
Provides:       tex(ts1-kuriercl.tfm) = %{tl_version}, tex(ts1-kuriercli.tfm) = %{tl_version}
Provides:       tex(ts1-kuriercm.tfm) = %{tl_version}, tex(ts1-kuriercmi.tfm) = %{tl_version}
Provides:       tex(ts1-kuriercr.tfm) = %{tl_version}, tex(ts1-kuriercri.tfm) = %{tl_version}
Provides:       tex(ts1-kurierh.tfm) = %{tl_version}, tex(ts1-kurierhi.tfm) = %{tl_version}
Provides:       tex(ts1-kurierl.tfm) = %{tl_version}, tex(ts1-kurierli.tfm) = %{tl_version}
Provides:       tex(ts1-kurierm.tfm) = %{tl_version}, tex(ts1-kuriermi.tfm) = %{tl_version}
Provides:       tex(ts1-kurierr.tfm) = %{tl_version}, tex(ts1-kurierri.tfm) = %{tl_version}
Provides:       tex(wncy-kurierb.tfm) = %{tl_version}, tex(wncy-kurierbi.tfm) = %{tl_version}
Provides:       tex(wncy-kuriercb.tfm) = %{tl_version}, tex(wncy-kuriercbi.tfm) = %{tl_version}
Provides:       tex(wncy-kurierch.tfm) = %{tl_version}, tex(wncy-kurierchi.tfm) = %{tl_version}
Provides:       tex(wncy-kuriercl.tfm) = %{tl_version}, tex(wncy-kuriercli.tfm) = %{tl_version}
Provides:       tex(wncy-kuriercm.tfm) = %{tl_version}, tex(wncy-kuriercmi.tfm) = %{tl_version}
Provides:       tex(wncy-kuriercr.tfm) = %{tl_version}, tex(wncy-kuriercri.tfm) = %{tl_version}
Provides:       tex(wncy-kurierh.tfm) = %{tl_version}, tex(wncy-kurierhi.tfm) = %{tl_version}
Provides:       tex(wncy-kurierl.tfm) = %{tl_version}, tex(wncy-kurierli.tfm) = %{tl_version}
Provides:       tex(wncy-kurierm.tfm) = %{tl_version}, tex(wncy-kuriermi.tfm) = %{tl_version}
Provides:       tex(wncy-kurierr.tfm) = %{tl_version}, tex(wncy-kurierri.tfm) = %{tl_version}
Provides:       tex(kurierb.pfb) = %{tl_version}, tex(kurierbi.pfb) = %{tl_version}
Provides:       tex(kuriercb.pfb) = %{tl_version}, tex(kuriercbi.pfb) = %{tl_version}
Provides:       tex(kurierch.pfb) = %{tl_version}, tex(kurierchi.pfb) = %{tl_version}
Provides:       tex(kuriercl.pfb) = %{tl_version}, tex(kuriercli.pfb) = %{tl_version}
Provides:       tex(kuriercm.pfb) = %{tl_version}, tex(kuriercmi.pfb) = %{tl_version}
Provides:       tex(kuriercr.pfb) = %{tl_version}, tex(kuriercri.pfb) = %{tl_version}
Provides:       tex(kurierh.pfb) = %{tl_version}, tex(kurierhi.pfb) = %{tl_version}
Provides:       tex(kurierl.pfb) = %{tl_version}, tex(kurierli.pfb) = %{tl_version}
Provides:       tex(kurierm.pfb) = %{tl_version}, tex(kuriermi.pfb) = %{tl_version}
Provides:       tex(kurierr.pfb) = %{tl_version}, tex(kurierri.pfb) = %{tl_version}
Provides:       tex(il2kurier.fd) = %{tl_version}, tex(il2kurierc.fd) = %{tl_version}
Provides:       tex(il2kurierl.fd) = %{tl_version}, tex(il2kurierlc.fd) = %{tl_version}
Provides:       tex(kurier.sty) = %{tl_version}, tex(l7xkurier.fd) = %{tl_version}
Provides:       tex(l7xkurierc.fd) = %{tl_version}, tex(l7xkurierl.fd) = %{tl_version}
Provides:       tex(l7xkurierlc.fd) = %{tl_version}, tex(ly1kurier.fd) = %{tl_version}
Provides:       tex(ly1kurierc.fd) = %{tl_version}, tex(ly1kurierl.fd) = %{tl_version}
Provides:       tex(ly1kurierlc.fd) = %{tl_version}, tex(omlkurier.fd) = %{tl_version}
Provides:       tex(omlkurierc.fd) = %{tl_version}, tex(omlkurierl.fd) = %{tl_version}
Provides:       tex(omlkurierlc.fd) = %{tl_version}, tex(omskurier.fd) = %{tl_version}
Provides:       tex(omskurierc.fd) = %{tl_version}, tex(omskurierl.fd) = %{tl_version}
Provides:       tex(omskurierlc.fd) = %{tl_version}, tex(omxkurier.fd) = %{tl_version}
Provides:       tex(omxkurierc.fd) = %{tl_version}, tex(omxkurierl.fd) = %{tl_version}
Provides:       tex(omxkurierlc.fd) = %{tl_version}, tex(ot1kurier.fd) = %{tl_version}
Provides:       tex(ot1kurierc.fd) = %{tl_version}, tex(ot1kuriercm.fd) = %{tl_version}
Provides:       tex(ot1kurierl.fd) = %{tl_version}, tex(ot1kurierlc.fd) = %{tl_version}
Provides:       tex(ot1kurierlcm.fd) = %{tl_version}, tex(ot1kurierlm.fd) = %{tl_version}
Provides:       tex(ot1kurierm.fd) = %{tl_version}, tex(ot2kurier.fd) = %{tl_version}
Provides:       tex(ot2kurierc.fd) = %{tl_version}, tex(ot2kurierl.fd) = %{tl_version}
Provides:       tex(ot2kurierlc.fd) = %{tl_version}, tex(ot4kurier.fd) = %{tl_version}
Provides:       tex(ot4kurierc.fd) = %{tl_version}, tex(ot4kurierl.fd) = %{tl_version}
Provides:       tex(ot4kurierlc.fd) = %{tl_version}, tex(qxkurier.fd) = %{tl_version}
Provides:       tex(qxkurierc.fd) = %{tl_version}, tex(qxkurierl.fd) = %{tl_version}
Provides:       tex(qxkurierlc.fd) = %{tl_version}, tex(t1kurier.fd) = %{tl_version}
Provides:       tex(t1kurierc.fd) = %{tl_version}, tex(t1kurierl.fd) = %{tl_version}
Provides:       tex(t1kurierlc.fd) = %{tl_version}, tex(t2akurier.fd) = %{tl_version}
Provides:       tex(t2akurierc.fd) = %{tl_version}, tex(t2akurierl.fd) = %{tl_version}
Provides:       tex(t2akurierlc.fd) = %{tl_version}, tex(t2bkurier.fd) = %{tl_version}
Provides:       tex(t2bkurierc.fd) = %{tl_version}, tex(t2bkurierl.fd) = %{tl_version}
Provides:       tex(t2bkurierlc.fd) = %{tl_version}, tex(t2ckurier.fd) = %{tl_version}
Provides:       tex(t2ckurierc.fd) = %{tl_version}, tex(t2ckurierl.fd) = %{tl_version}
Provides:       tex(t2ckurierlc.fd) = %{tl_version}, tex(t5kurier.fd) = %{tl_version}
Provides:       tex(t5kurierc.fd) = %{tl_version}, tex(t5kurierl.fd) = %{tl_version}
Provides:       tex(t5kurierlc.fd) = %{tl_version}, tex(ts1kurier.fd) = %{tl_version}
Provides:       tex(ts1kurierc.fd) = %{tl_version}, tex(ts1kurierl.fd) = %{tl_version}
Provides:       tex(ts1kurierlc.fd) = %{tl_version}, tex(kurier-math.tex) = %{tl_version}

%description -n texlive-kurier
Kurier is a two-element sans-serif typeface. It was designed
for a diploma in typeface design at the Warsaw Academy of Fine
Arts under the supervision of Roman Tomaszewski. This
distribution contains a significantly extended set of
characters covering the following modern alphabets: latin
(including Vietnamese), Cyrillic and Greek as well as a number
of additional symbols (including mathematical symbols). The
fonts are prepared in Type 1 and OpenType formats. For use with
TeX the following encoding files have been prepared: T1 (ec),
T2 (abc), and OT2--Cyrillic, T5 (Vietnamese), OT4, QX, texansi
and--nonstandard (IL2 for the Czech fonts), as well as
supporting macros and files defining fonts for LaTeX.

%package -n texlive-kurier-doc
Summary:        Documentation for kurier
Version:        svn19612.0.995b

Provides:       tex-kurier-doc
AutoReqProv:    No

%description -n texlive-kurier-doc
Documentation for kurier

%package -n texlive-kastrup
Provides:       tex-kastrup = %{tl_version}
License:        Copyright only
Summary:        Convert numbers into binary, octal and hexadecimal
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(binhex.tex) = %{tl_version}

%description -n texlive-kastrup
Provides expandable macros for both fixed-width and minimum-
width numbers to bases 2, 4, 8 and 16.

%package -n texlive-kastrup-doc
Summary:        Documentation for kastrup
Version:        svn15878.0

Provides:       tex-kastrup-doc
AutoReqProv:    No

%description -n texlive-kastrup-doc
Documentation for kastrup

%package -n texlive-jura
Provides:       tex-jura = %{tl_version}
License:        GPL+
Summary:        A document class for German legal texts
Version:        svn15878.4.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(alphanum.sty) = %{tl_version}, tex(jura.cls) = %{tl_version}

%description -n texlive-jura
Implements the standard layout for German term papers in law
(one-and-half linespacing, 7 cm margins, etc.). Includes
alphanum that permits alphanumeric section numbering (e.g., A.
Introduction; III. International Law).

%package -n texlive-jura-doc
Summary:        Documentation for jura
Version:        svn15878.4.3

Provides:       tex-jura-doc
AutoReqProv:    No

%description -n texlive-jura-doc
Documentation for jura

%package -n texlive-juraabbrev
Provides:       tex-juraabbrev = %{tl_version}
License:        GPL+
Summary:        Abbreviations for typesetting (German) juridical documents
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(juraabbrev.sty) = %{tl_version}

%description -n texlive-juraabbrev
This package should be helpful for people working on (German)
law. It helps you to handle abbreviations and creates a list of
those (pre-defined) abbreviations that have actually been used
in the document

%package -n texlive-juraabbrev-doc
Summary:        Documentation for juraabbrev
Version:        svn15878.0

Provides:       tex-juraabbrev-doc
AutoReqProv:    No

%description -n texlive-juraabbrev-doc
Documentation for juraabbrev

%package -n texlive-juramisc
Provides:       tex-juramisc = %{tl_version}
License:        LPPL
Summary:        Typesetting German juridical documents
Version:        svn15878.0.91

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty), tex(calc.sty), tex(ifthen.sty), tex(remreset.sty)
Requires:       tex(fancyhdr.sty), tex(multicol.sty), tex(ragged2e.sty), tex(array.sty)
Requires:       tex(pifont.sty), tex(fancybox.sty), tex(color.sty)
Provides:       tex(jbgoe.clo) = %{tl_version}, tex(jbstgallen.clo) = %{tl_version}
Provides:       tex(jbtrier.clo) = %{tl_version}, tex(jurabase.sty) = %{tl_version}
Provides:       tex(jurabook.cls) = %{tl_version}, tex(juraovw.cls) = %{tl_version}
Provides:       tex(juraurtl.cls) = %{tl_version}

%description -n texlive-juramisc
A collection of classes for typesetting court sentences, legal
opinions, books and dissertations for German lawyers. A
jurabook class is also provided, which may not yet be complete.

%package -n texlive-juramisc-doc
Summary:        Documentation for juramisc
Version:        svn15878.0.91

Provides:       tex-juramisc-doc
AutoReqProv:    No

%description -n texlive-juramisc-doc
Documentation for juramisc

%package -n texlive-jurarsp
Provides:       tex-jurarsp = %{tl_version}
License:        GPL+
Summary:        Citations of judgements and official documents in (German) juridical documents
Version:        svn15878.0.52

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(keyval.sty), tex(xspace.sty), tex(calc.sty)
Provides:       tex(jurarsp.cfg) = %{tl_version}, tex(jurarsp.sty) = %{tl_version}

%description -n texlive-jurarsp
This package should be helpful for people working on (German)
law. It (ab)uses BibTeX for citations of judgements and
official documents. For this purpose, a special BibTeX-style is
provided.

%package -n texlive-jurarsp-doc
Summary:        Documentation for jurarsp
Version:        svn15878.0.52

Provides:       tex-jurarsp-doc
AutoReqProv:    No

%description -n texlive-jurarsp-doc
Documentation for jurarsp

%package -n texlive-knuth-doc
Summary:        Documentation for knuth
Version:        svn32899.0

Provides:       tex-knuth-doc
AutoReqProv:    No

%description -n texlive-knuth-doc
Documentation for knuth

%package -n texlive-kerkis
Provides:       tex-kerkis = %{tl_version}
License:        LPPL
Summary:        Kerkis (Greek) font family
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(txfonts.sty)
Provides:       tex(gkerkis.enc) = %{tl_version}, tex(gkerkisc.enc) = %{tl_version}
Provides:       tex(gpkerkis.enc) = %{tl_version}, tex(gpkerkisc.enc) = %{tl_version}
Provides:       tex(kerkis.enc) = %{tl_version}, tex(kerkisc.enc) = %{tl_version}
Provides:       tex(kerkisec.enc) = %{tl_version}, tex(kerkisecsc.enc) = %{tl_version}
Provides:       tex(kmath.enc) = %{tl_version}, tex(kmex.enc) = %{tl_version}
Provides:       tex(kmsym.enc) = %{tl_version}, tex(kerkis.map) = %{tl_version}
Provides:       tex(ek8a.tfm) = %{tl_version}, tex(ek8r.tfm) = %{tl_version}
Provides:       tex(ekb8a.tfm) = %{tl_version}, tex(ekb8r.tfm) = %{tl_version}
Provides:       tex(ekbi8a.tfm) = %{tl_version}, tex(ekbi8r.tfm) = %{tl_version}
Provides:       tex(ekbo8a.tfm) = %{tl_version}, tex(ekbo8r.tfm) = %{tl_version}
Provides:       tex(ekbsc8a.tfm) = %{tl_version}, tex(ekbsc8r.tfm) = %{tl_version}
Provides:       tex(ekbsco8a.tfm) = %{tl_version}, tex(ekbsco8r.tfm) = %{tl_version}
Provides:       tex(ekbui8a.tfm) = %{tl_version}, tex(ekbui8r.tfm) = %{tl_version}
Provides:       tex(ekcal8a.tfm) = %{tl_version}, tex(ekcal8r.tfm) = %{tl_version}
Provides:       tex(eki8a.tfm) = %{tl_version}, tex(eki8r.tfm) = %{tl_version}
Provides:       tex(eko8a.tfm) = %{tl_version}, tex(eko8r.tfm) = %{tl_version}
Provides:       tex(eksb8a.tfm) = %{tl_version}, tex(eksb8r.tfm) = %{tl_version}
Provides:       tex(eksbi8a.tfm) = %{tl_version}, tex(eksbi8r.tfm) = %{tl_version}
Provides:       tex(eksbo8a.tfm) = %{tl_version}, tex(eksbo8r.tfm) = %{tl_version}
Provides:       tex(eksbui8a.tfm) = %{tl_version}, tex(eksbui8r.tfm) = %{tl_version}
Provides:       tex(eksc8a.tfm) = %{tl_version}, tex(eksc8r.tfm) = %{tl_version}
Provides:       tex(eksco8a.tfm) = %{tl_version}, tex(eksco8r.tfm) = %{tl_version}
Provides:       tex(eksf8a.tfm) = %{tl_version}, tex(eksf8t.tfm) = %{tl_version}
Provides:       tex(eksfb8a.tfm) = %{tl_version}, tex(eksfb8t.tfm) = %{tl_version}
Provides:       tex(eksfbi8a.tfm) = %{tl_version}, tex(eksfbi8t.tfm) = %{tl_version}
Provides:       tex(eksfi8a.tfm) = %{tl_version}, tex(eksfi8t.tfm) = %{tl_version}
Provides:       tex(eksfsc8a.tfm) = %{tl_version}, tex(eksfsc8t.tfm) = %{tl_version}
Provides:       tex(ekui8a.tfm) = %{tl_version}, tex(ekui8r.tfm) = %{tl_version}
Provides:       tex(gk7a.tfm) = %{tl_version}, tex(gk7t.tfm) = %{tl_version}
Provides:       tex(gkb7a.tfm) = %{tl_version}, tex(gkb7t.tfm) = %{tl_version}
Provides:       tex(gkbi7a.tfm) = %{tl_version}, tex(gkbi7t.tfm) = %{tl_version}
Provides:       tex(gkbo7a.tfm) = %{tl_version}, tex(gkbo7t.tfm) = %{tl_version}
Provides:       tex(gkbsc8a.tfm) = %{tl_version}, tex(gkbsc8r.tfm) = %{tl_version}
Provides:       tex(gkbsco8a.tfm) = %{tl_version}, tex(gkbsco8r.tfm) = %{tl_version}
Provides:       tex(gkbui7a.tfm) = %{tl_version}, tex(gkbui7t.tfm) = %{tl_version}
Provides:       tex(gkcal7a.tfm) = %{tl_version}, tex(gkcal7t.tfm) = %{tl_version}
Provides:       tex(gki7a.tfm) = %{tl_version}, tex(gki7t.tfm) = %{tl_version}
Provides:       tex(gko7a.tfm) = %{tl_version}, tex(gko7t.tfm) = %{tl_version}
Provides:       tex(gksb7a.tfm) = %{tl_version}, tex(gksb7t.tfm) = %{tl_version}
Provides:       tex(gksbi7a.tfm) = %{tl_version}, tex(gksbi7t.tfm) = %{tl_version}
Provides:       tex(gksbo7a.tfm) = %{tl_version}, tex(gksbo7t.tfm) = %{tl_version}
Provides:       tex(gksbui7a.tfm) = %{tl_version}, tex(gksbui7t.tfm) = %{tl_version}
Provides:       tex(gksc7a.tfm) = %{tl_version}, tex(gksc7t.tfm) = %{tl_version}
Provides:       tex(gksco7a.tfm) = %{tl_version}, tex(gksco7t.tfm) = %{tl_version}
Provides:       tex(gksf7a.tfm) = %{tl_version}, tex(gksf7t.tfm) = %{tl_version}
Provides:       tex(gksfb7a.tfm) = %{tl_version}, tex(gksfb7t.tfm) = %{tl_version}
Provides:       tex(gksfbi7a.tfm) = %{tl_version}, tex(gksfbi7t.tfm) = %{tl_version}
Provides:       tex(gksfi7a.tfm) = %{tl_version}, tex(gksfi7t.tfm) = %{tl_version}
Provides:       tex(gksfsc7a.tfm) = %{tl_version}, tex(gksfsc7t.tfm) = %{tl_version}
Provides:       tex(gkui7a.tfm) = %{tl_version}, tex(gkui7t.tfm) = %{tl_version}
Provides:       tex(k8a.tfm) = %{tl_version}, tex(k8r.tfm) = %{tl_version}
Provides:       tex(kb8a.tfm) = %{tl_version}, tex(kb8r.tfm) = %{tl_version}
Provides:       tex(kbi8a.tfm) = %{tl_version}, tex(kbi8r.tfm) = %{tl_version}
Provides:       tex(kbo8a.tfm) = %{tl_version}, tex(kbo8r.tfm) = %{tl_version}
Provides:       tex(kbsc8a.tfm) = %{tl_version}, tex(kbsc8r.tfm) = %{tl_version}
Provides:       tex(kbsco8a.tfm) = %{tl_version}, tex(kbsco8r.tfm) = %{tl_version}
Provides:       tex(kbui8a.tfm) = %{tl_version}, tex(kbui8r.tfm) = %{tl_version}
Provides:       tex(kcal8a.tfm) = %{tl_version}, tex(kcal8r.tfm) = %{tl_version}
Provides:       tex(ki8a.tfm) = %{tl_version}, tex(ki8r.tfm) = %{tl_version}
Provides:       tex(kmath8a.tfm) = %{tl_version}, tex(kmath8r.tfm) = %{tl_version}
Provides:       tex(ko8a.tfm) = %{tl_version}, tex(ko8r.tfm) = %{tl_version}
Provides:       tex(ksb8a.tfm) = %{tl_version}, tex(ksb8r.tfm) = %{tl_version}
Provides:       tex(ksbi8a.tfm) = %{tl_version}, tex(ksbi8r.tfm) = %{tl_version}
Provides:       tex(ksbo8a.tfm) = %{tl_version}, tex(ksbo8r.tfm) = %{tl_version}
Provides:       tex(ksbui8a.tfm) = %{tl_version}, tex(ksbui8r.tfm) = %{tl_version}
Provides:       tex(ksc8a.tfm) = %{tl_version}, tex(ksc8r.tfm) = %{tl_version}
Provides:       tex(ksco8a.tfm) = %{tl_version}, tex(ksco8r.tfm) = %{tl_version}
Provides:       tex(ksf8a.tfm) = %{tl_version}, tex(ksf8t.tfm) = %{tl_version}
Provides:       tex(ksfb8a.tfm) = %{tl_version}, tex(ksfb8t.tfm) = %{tl_version}
Provides:       tex(ksfbi8a.tfm) = %{tl_version}, tex(ksfbi8t.tfm) = %{tl_version}
Provides:       tex(ksfi8a.tfm) = %{tl_version}, tex(ksfi8t.tfm) = %{tl_version}
Provides:       tex(ksfsc8a.tfm) = %{tl_version}, tex(ksfsc8t.tfm) = %{tl_version}
Provides:       tex(ktsy8a.tfm) = %{tl_version}, tex(ktsy8r.tfm) = %{tl_version}
Provides:       tex(kui8a.tfm) = %{tl_version}, tex(kui8r.tfm) = %{tl_version}
Provides:       tex(Kerkis-Bold.pfb) = %{tl_version}, tex(Kerkis-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Kerkis-BoldSmallCaps.pfb) = %{tl_version}
Provides:       tex(Kerkis-Calligraphic.pfb) = %{tl_version}
Provides:       tex(Kerkis-Italic.pfb) = %{tl_version}, tex(Kerkis-SemiBold-Italic.pfb) = %{tl_version}
Provides:       tex(Kerkis-SemiBold.pfb) = %{tl_version}
Provides:       tex(Kerkis-SmallCaps.pfb) = %{tl_version}
Provides:       tex(Kerkis.pfb) = %{tl_version}, tex(KerkisSans-Bold.pfb) = %{tl_version}
Provides:       tex(KerkisSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(KerkisSans-Italic.pfb) = %{tl_version}
Provides:       tex(KerkisSans-SmallCaps.pfb) = %{tl_version}
Provides:       tex(KerkisSans.pfb) = %{tl_version}, tex(ktsy.pfb) = %{tl_version}
Provides:       tex(ek8a.vf) = %{tl_version}, tex(ekb8a.vf) = %{tl_version}
Provides:       tex(ekbi8a.vf) = %{tl_version}, tex(ekbo8a.vf) = %{tl_version}
Provides:       tex(ekbsc8a.vf) = %{tl_version}, tex(ekbsco8a.vf) = %{tl_version}
Provides:       tex(ekbui8a.vf) = %{tl_version}, tex(ekcal8a.vf) = %{tl_version}
Provides:       tex(eki8a.vf) = %{tl_version}, tex(eko8a.vf) = %{tl_version}
Provides:       tex(eksb8a.vf) = %{tl_version}, tex(eksbi8a.vf) = %{tl_version}
Provides:       tex(eksbo8a.vf) = %{tl_version}, tex(eksbui8a.vf) = %{tl_version}
Provides:       tex(eksc8a.vf) = %{tl_version}, tex(eksco8a.vf) = %{tl_version}
Provides:       tex(eksf8t.vf) = %{tl_version}, tex(eksfb8t.vf) = %{tl_version}
Provides:       tex(eksfbi8t.vf) = %{tl_version}, tex(eksfi8t.vf) = %{tl_version}
Provides:       tex(eksfsc8t.vf) = %{tl_version}, tex(ekui8a.vf) = %{tl_version}
Provides:       tex(gk7t.vf) = %{tl_version}, tex(gkb7t.vf) = %{tl_version}
Provides:       tex(gkbi7t.vf) = %{tl_version}, tex(gkbo7t.vf) = %{tl_version}
Provides:       tex(gkbsc8a.vf) = %{tl_version}, tex(gkbsco8a.vf) = %{tl_version}
Provides:       tex(gkbui7t.vf) = %{tl_version}, tex(gkcal7t.vf) = %{tl_version}
Provides:       tex(gki7t.vf) = %{tl_version}, tex(gko7t.vf) = %{tl_version}
Provides:       tex(gksb7t.vf) = %{tl_version}, tex(gksbi7t.vf) = %{tl_version}
Provides:       tex(gksbo7t.vf) = %{tl_version}, tex(gksbui7t.vf) = %{tl_version}
Provides:       tex(gksc7t.vf) = %{tl_version}, tex(gksco7t.vf) = %{tl_version}
Provides:       tex(gksf7t.vf) = %{tl_version}, tex(gksfb7t.vf) = %{tl_version}
Provides:       tex(gksfbi7t.vf) = %{tl_version}, tex(gksfi7t.vf) = %{tl_version}
Provides:       tex(gksfsc7t.vf) = %{tl_version}, tex(gkui7t.vf) = %{tl_version}
Provides:       tex(k8a.vf) = %{tl_version}, tex(kb8a.vf) = %{tl_version}
Provides:       tex(kbi8a.vf) = %{tl_version}, tex(kbo8a.vf) = %{tl_version}
Provides:       tex(kbsc8a.vf) = %{tl_version}, tex(kbsco8a.vf) = %{tl_version}
Provides:       tex(kbui8a.vf) = %{tl_version}, tex(kcal8a.vf) = %{tl_version}
Provides:       tex(ki8a.vf) = %{tl_version}, tex(kmath8a.vf) = %{tl_version}
Provides:       tex(ko8a.vf) = %{tl_version}, tex(ksb8a.vf) = %{tl_version}
Provides:       tex(ksbi8a.vf) = %{tl_version}, tex(ksbo8a.vf) = %{tl_version}
Provides:       tex(ksbui8a.vf) = %{tl_version}, tex(ksc8a.vf) = %{tl_version}
Provides:       tex(ksco8a.vf) = %{tl_version}, tex(ksf8t.vf) = %{tl_version}
Provides:       tex(ksfb8t.vf) = %{tl_version}, tex(ksfbi8t.vf) = %{tl_version}
Provides:       tex(ksfi8t.vf) = %{tl_version}, tex(ksfsc8t.vf) = %{tl_version}
Provides:       tex(ktsy8a.vf) = %{tl_version}, tex(kui8a.vf) = %{tl_version}
Provides:       tex(kerkis.sty) = %{tl_version}, tex(kmath.sty) = %{tl_version}
Provides:       tex(lgrkfn.fd) = %{tl_version}, tex(lgrmak.fd) = %{tl_version}
Provides:       tex(lgrmaksf.fd) = %{tl_version}, tex(omlmak.fd) = %{tl_version}
Provides:       tex(omsmak.fd) = %{tl_version}, tex(ot1kfn.fd) = %{tl_version}
Provides:       tex(ot1mak.fd) = %{tl_version}, tex(ot1maksf.fd) = %{tl_version}
Provides:       tex(t1mak.fd) = %{tl_version}, tex(t1maksf.fd) = %{tl_version}
Obsoletes:      tex-kerkis < %{tl_version}

%description -n texlive-kerkis
Sans-serif Greek fonts to match the URW Bookman set (which are
distributed with Kerkis). The Kerkis font set has some support
for mathematics as well as other glyphs missing from the base
URW Bookman fonts. Macros are provided to use the fonts in OT1,
T1 (only NG/ng glyphs missing) and LGR encodings, as well as in
mathematics; small caps and old-style number glyphs are also
available. The philosophy, and the design process, of the
Kerkis fonts is discussed in a paper in TUGboat 23(3/4), 2002.

%package -n texlive-kerkis-doc
Summary:        Documentation for kerkis
Version:        svn15878.0

Provides:       tex-kerkis-doc
AutoReqProv:    No

%description -n texlive-kerkis-doc
Documentation for kerkis

%package -n texlive-itnumpar
Provides:       tex-itnumpar = %{tl_version}
License:        LPPL
Summary:        Spell numbers in words (Italian)
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(itnumpar.sty) = %{tl_version}

%description -n texlive-itnumpar
Sometimes we need to say "Capitolo primo" or "Capitolo uno"
instead of "Capitolo 1", that is, spelling the number in words
instead of the usual digit form. This package provides support
for spelling out numbers in Italian words, both in cardinal and
in ordinal form.

%package -n texlive-itnumpar-doc
Summary:        Documentation for itnumpar
Version:        svn15878.1.0

Provides:       tex-itnumpar-doc
AutoReqProv:    No

%description -n texlive-itnumpar-doc
Documentation for itnumpar

%package -n texlive-japanese-otf
Provides:       tex-japanese-otf = %{tl_version}
License:        BSD
Summary:        Advanced font selection for platex and its friends
Version:        svn46598
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(otf.sty)
Provides:       tex(otf-cktx.map) = %{tl_version}, tex(brsgexpgothb-h.tfm) = %{tl_version}
Provides:       tex(brsgexpgothb-v.tfm) = %{tl_version}, tex(brsgexpgothbn-h.tfm) = %{tl_version}
Provides:       tex(brsgexpgothbn-v.tfm) = %{tl_version}
Provides:       tex(brsgexpgotheb-h.tfm) = %{tl_version}
Provides:       tex(brsgexpgotheb-v.tfm) = %{tl_version}
Provides:       tex(brsgexpgothebn-h.tfm) = %{tl_version}
Provides:       tex(brsgexpgothebn-v.tfm) = %{tl_version}
Provides:       tex(brsgexpgothr-h.tfm) = %{tl_version}, tex(brsgexpgothr-v.tfm) = %{tl_version}
Provides:       tex(brsgexpgothrn-h.tfm) = %{tl_version}
Provides:       tex(brsgexpgothrn-v.tfm) = %{tl_version}
Provides:       tex(brsgexpmgothr-h.tfm) = %{tl_version}
Provides:       tex(brsgexpmgothr-v.tfm) = %{tl_version}
Provides:       tex(brsgexpmgothrn-h.tfm) = %{tl_version}
Provides:       tex(brsgexpmgothrn-v.tfm) = %{tl_version}
Provides:       tex(brsgexpminb-h.tfm) = %{tl_version}, tex(brsgexpminb-v.tfm) = %{tl_version}
Provides:       tex(brsgexpminbn-h.tfm) = %{tl_version}, tex(brsgexpminbn-v.tfm) = %{tl_version}
Provides:       tex(brsgexpminl-h.tfm) = %{tl_version}, tex(brsgexpminl-v.tfm) = %{tl_version}
Provides:       tex(brsgexpminln-h.tfm) = %{tl_version}, tex(brsgexpminln-v.tfm) = %{tl_version}
Provides:       tex(brsgexpminr-h.tfm) = %{tl_version}, tex(brsgexpminr-v.tfm) = %{tl_version}
Provides:       tex(brsgexpminrn-h.tfm) = %{tl_version}, tex(brsgexpminrn-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlgothb-h.tfm) = %{tl_version}, tex(brsgnmlgothb-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlgothbn-h.tfm) = %{tl_version}
Provides:       tex(brsgnmlgothbn-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlgotheb-h.tfm) = %{tl_version}
Provides:       tex(brsgnmlgotheb-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlgothebn-h.tfm) = %{tl_version}
Provides:       tex(brsgnmlgothebn-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlgothr-h.tfm) = %{tl_version}, tex(brsgnmlgothr-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlgothrn-h.tfm) = %{tl_version}
Provides:       tex(brsgnmlgothrn-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlmgothr-h.tfm) = %{tl_version}
Provides:       tex(brsgnmlmgothr-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlmgothrn-h.tfm) = %{tl_version}
Provides:       tex(brsgnmlmgothrn-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlminb-h.tfm) = %{tl_version}, tex(brsgnmlminb-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlminbn-h.tfm) = %{tl_version}, tex(brsgnmlminbn-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlminl-h.tfm) = %{tl_version}, tex(brsgnmlminl-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlminln-h.tfm) = %{tl_version}, tex(brsgnmlminln-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlminr-h.tfm) = %{tl_version}, tex(brsgnmlminr-v.tfm) = %{tl_version}
Provides:       tex(brsgnmlminrn-h.tfm) = %{tl_version}, tex(brsgnmlminrn-v.tfm) = %{tl_version}
Provides:       tex(cidcgr0-h.tfm) = %{tl_version}, tex(cidcgr0-v.tfm) = %{tl_version}
Provides:       tex(cidcgr1-h.tfm) = %{tl_version}, tex(cidcgr1-v.tfm) = %{tl_version}
Provides:       tex(cidcgr2-h.tfm) = %{tl_version}, tex(cidcgr2-v.tfm) = %{tl_version}
Provides:       tex(cidcgr3-h.tfm) = %{tl_version}, tex(cidcgr3-v.tfm) = %{tl_version}
Provides:       tex(cidcgr4-h.tfm) = %{tl_version}, tex(cidcgr4-v.tfm) = %{tl_version}
Provides:       tex(cidcgr5-h.tfm) = %{tl_version}, tex(cidcgr5-v.tfm) = %{tl_version}
Provides:       tex(cidcgr6-h.tfm) = %{tl_version}, tex(cidcgr6-v.tfm) = %{tl_version}
Provides:       tex(cidcgr7-h.tfm) = %{tl_version}, tex(cidcgr7-v.tfm) = %{tl_version}
Provides:       tex(cidcmr0-h.tfm) = %{tl_version}, tex(cidcmr0-v.tfm) = %{tl_version}
Provides:       tex(cidcmr1-h.tfm) = %{tl_version}, tex(cidcmr1-v.tfm) = %{tl_version}
Provides:       tex(cidcmr2-h.tfm) = %{tl_version}, tex(cidcmr2-v.tfm) = %{tl_version}
Provides:       tex(cidcmr3-h.tfm) = %{tl_version}, tex(cidcmr3-v.tfm) = %{tl_version}
Provides:       tex(cidcmr4-h.tfm) = %{tl_version}, tex(cidcmr4-v.tfm) = %{tl_version}
Provides:       tex(cidcmr5-h.tfm) = %{tl_version}, tex(cidcmr5-v.tfm) = %{tl_version}
Provides:       tex(cidcmr6-h.tfm) = %{tl_version}, tex(cidcmr6-v.tfm) = %{tl_version}
Provides:       tex(cidcmr7-h.tfm) = %{tl_version}, tex(cidcmr7-v.tfm) = %{tl_version}
Provides:       tex(cidjgb0-h.tfm) = %{tl_version}, tex(cidjgb0-v.tfm) = %{tl_version}
Provides:       tex(cidjgb1-h.tfm) = %{tl_version}, tex(cidjgb1-v.tfm) = %{tl_version}
Provides:       tex(cidjgb2-h.tfm) = %{tl_version}, tex(cidjgb2-v.tfm) = %{tl_version}
Provides:       tex(cidjgb3-h.tfm) = %{tl_version}, tex(cidjgb3-v.tfm) = %{tl_version}
Provides:       tex(cidjgb4-h.tfm) = %{tl_version}, tex(cidjgb4-v.tfm) = %{tl_version}
Provides:       tex(cidjgb5-h.tfm) = %{tl_version}, tex(cidjgb5-v.tfm) = %{tl_version}
Provides:       tex(cidjge0-h.tfm) = %{tl_version}, tex(cidjge0-v.tfm) = %{tl_version}
Provides:       tex(cidjge1-h.tfm) = %{tl_version}, tex(cidjge1-v.tfm) = %{tl_version}
Provides:       tex(cidjge2-h.tfm) = %{tl_version}, tex(cidjge2-v.tfm) = %{tl_version}
Provides:       tex(cidjge3-h.tfm) = %{tl_version}, tex(cidjge3-v.tfm) = %{tl_version}
Provides:       tex(cidjge4-h.tfm) = %{tl_version}, tex(cidjge4-v.tfm) = %{tl_version}
Provides:       tex(cidjge5-h.tfm) = %{tl_version}, tex(cidjge5-v.tfm) = %{tl_version}
Provides:       tex(cidjgr0-h.tfm) = %{tl_version}, tex(cidjgr0-v.tfm) = %{tl_version}
Provides:       tex(cidjgr1-h.tfm) = %{tl_version}, tex(cidjgr1-v.tfm) = %{tl_version}
Provides:       tex(cidjgr2-h.tfm) = %{tl_version}, tex(cidjgr2-v.tfm) = %{tl_version}
Provides:       tex(cidjgr3-h.tfm) = %{tl_version}, tex(cidjgr3-v.tfm) = %{tl_version}
Provides:       tex(cidjgr4-h.tfm) = %{tl_version}, tex(cidjgr4-v.tfm) = %{tl_version}
Provides:       tex(cidjgr5-h.tfm) = %{tl_version}, tex(cidjgr5-v.tfm) = %{tl_version}
Provides:       tex(cidjmb0-h.tfm) = %{tl_version}, tex(cidjmb0-v.tfm) = %{tl_version}
Provides:       tex(cidjmb1-h.tfm) = %{tl_version}, tex(cidjmb1-v.tfm) = %{tl_version}
Provides:       tex(cidjmb2-h.tfm) = %{tl_version}, tex(cidjmb2-v.tfm) = %{tl_version}
Provides:       tex(cidjmb3-h.tfm) = %{tl_version}, tex(cidjmb3-v.tfm) = %{tl_version}
Provides:       tex(cidjmb4-h.tfm) = %{tl_version}, tex(cidjmb4-v.tfm) = %{tl_version}
Provides:       tex(cidjmb5-h.tfm) = %{tl_version}, tex(cidjmb5-v.tfm) = %{tl_version}
Provides:       tex(cidjmgr0-h.tfm) = %{tl_version}, tex(cidjmgr0-v.tfm) = %{tl_version}
Provides:       tex(cidjmgr1-h.tfm) = %{tl_version}, tex(cidjmgr1-v.tfm) = %{tl_version}
Provides:       tex(cidjmgr2-h.tfm) = %{tl_version}, tex(cidjmgr2-v.tfm) = %{tl_version}
Provides:       tex(cidjmgr3-h.tfm) = %{tl_version}, tex(cidjmgr3-v.tfm) = %{tl_version}
Provides:       tex(cidjmgr4-h.tfm) = %{tl_version}, tex(cidjmgr4-v.tfm) = %{tl_version}
Provides:       tex(cidjmgr5-h.tfm) = %{tl_version}, tex(cidjmgr5-v.tfm) = %{tl_version}
Provides:       tex(cidjml0-h.tfm) = %{tl_version}, tex(cidjml0-v.tfm) = %{tl_version}
Provides:       tex(cidjml1-h.tfm) = %{tl_version}, tex(cidjml1-v.tfm) = %{tl_version}
Provides:       tex(cidjml2-h.tfm) = %{tl_version}, tex(cidjml2-v.tfm) = %{tl_version}
Provides:       tex(cidjml3-h.tfm) = %{tl_version}, tex(cidjml3-v.tfm) = %{tl_version}
Provides:       tex(cidjml4-h.tfm) = %{tl_version}, tex(cidjml4-v.tfm) = %{tl_version}
Provides:       tex(cidjml5-h.tfm) = %{tl_version}, tex(cidjml5-v.tfm) = %{tl_version}
Provides:       tex(cidjmr0-h.tfm) = %{tl_version}, tex(cidjmr0-v.tfm) = %{tl_version}
Provides:       tex(cidjmr1-h.tfm) = %{tl_version}, tex(cidjmr1-v.tfm) = %{tl_version}
Provides:       tex(cidjmr2-h.tfm) = %{tl_version}, tex(cidjmr2-v.tfm) = %{tl_version}
Provides:       tex(cidjmr3-h.tfm) = %{tl_version}, tex(cidjmr3-v.tfm) = %{tl_version}
Provides:       tex(cidjmr4-h.tfm) = %{tl_version}, tex(cidjmr4-v.tfm) = %{tl_version}
Provides:       tex(cidjmr5-h.tfm) = %{tl_version}, tex(cidjmr5-v.tfm) = %{tl_version}
Provides:       tex(cidkgr0-h.tfm) = %{tl_version}, tex(cidkgr0-v.tfm) = %{tl_version}
Provides:       tex(cidkgr1-h.tfm) = %{tl_version}, tex(cidkgr1-v.tfm) = %{tl_version}
Provides:       tex(cidkgr2-h.tfm) = %{tl_version}, tex(cidkgr2-v.tfm) = %{tl_version}
Provides:       tex(cidkgr3-h.tfm) = %{tl_version}, tex(cidkgr3-v.tfm) = %{tl_version}
Provides:       tex(cidkgr4-h.tfm) = %{tl_version}, tex(cidkgr4-v.tfm) = %{tl_version}
Provides:       tex(cidkmr0-h.tfm) = %{tl_version}, tex(cidkmr0-v.tfm) = %{tl_version}
Provides:       tex(cidkmr1-h.tfm) = %{tl_version}, tex(cidkmr1-v.tfm) = %{tl_version}
Provides:       tex(cidkmr2-h.tfm) = %{tl_version}, tex(cidkmr2-v.tfm) = %{tl_version}
Provides:       tex(cidkmr3-h.tfm) = %{tl_version}, tex(cidkmr3-v.tfm) = %{tl_version}
Provides:       tex(cidkmr4-h.tfm) = %{tl_version}, tex(cidkmr4-v.tfm) = %{tl_version}
Provides:       tex(cidtgr0-h.tfm) = %{tl_version}, tex(cidtgr0-v.tfm) = %{tl_version}
Provides:       tex(cidtgr1-h.tfm) = %{tl_version}, tex(cidtgr1-v.tfm) = %{tl_version}
Provides:       tex(cidtgr2-h.tfm) = %{tl_version}, tex(cidtgr2-v.tfm) = %{tl_version}
Provides:       tex(cidtgr3-h.tfm) = %{tl_version}, tex(cidtgr3-v.tfm) = %{tl_version}
Provides:       tex(cidtgr4-h.tfm) = %{tl_version}, tex(cidtgr4-v.tfm) = %{tl_version}
Provides:       tex(cidtmr0-h.tfm) = %{tl_version}, tex(cidtmr0-v.tfm) = %{tl_version}
Provides:       tex(cidtmr1-h.tfm) = %{tl_version}, tex(cidtmr1-v.tfm) = %{tl_version}
Provides:       tex(cidtmr2-h.tfm) = %{tl_version}, tex(cidtmr2-v.tfm) = %{tl_version}
Provides:       tex(cidtmr3-h.tfm) = %{tl_version}, tex(cidtmr3-v.tfm) = %{tl_version}
Provides:       tex(cidtmr4-h.tfm) = %{tl_version}, tex(cidtmr4-v.tfm) = %{tl_version}
Provides:       tex(expgothb-h.tfm) = %{tl_version}, tex(expgothb-v.tfm) = %{tl_version}
Provides:       tex(expgothbn-h.tfm) = %{tl_version}, tex(expgothbn-v.tfm) = %{tl_version}
Provides:       tex(expgotheb-h.tfm) = %{tl_version}, tex(expgotheb-v.tfm) = %{tl_version}
Provides:       tex(expgothebn-h.tfm) = %{tl_version}, tex(expgothebn-v.tfm) = %{tl_version}
Provides:       tex(expgothr-h.tfm) = %{tl_version}, tex(expgothr-v.tfm) = %{tl_version}
Provides:       tex(expgothrn-h.tfm) = %{tl_version}, tex(expgothrn-v.tfm) = %{tl_version}
Provides:       tex(expmgothr-h.tfm) = %{tl_version}, tex(expmgothr-v.tfm) = %{tl_version}
Provides:       tex(expmgothrn-h.tfm) = %{tl_version}, tex(expmgothrn-v.tfm) = %{tl_version}
Provides:       tex(expminb-h.tfm) = %{tl_version}, tex(expminb-v.tfm) = %{tl_version}
Provides:       tex(expminbn-h.tfm) = %{tl_version}, tex(expminbn-v.tfm) = %{tl_version}
Provides:       tex(expminl-h.tfm) = %{tl_version}, tex(expminl-v.tfm) = %{tl_version}
Provides:       tex(expminln-h.tfm) = %{tl_version}, tex(expminln-v.tfm) = %{tl_version}
Provides:       tex(expminr-h.tfm) = %{tl_version}, tex(expminr-v.tfm) = %{tl_version}
Provides:       tex(expminrn-h.tfm) = %{tl_version}, tex(expminrn-v.tfm) = %{tl_version}
Provides:       tex(hgothb-h.tfm) = %{tl_version}, tex(hgothb-v.tfm) = %{tl_version}
Provides:       tex(hgothbn-h.tfm) = %{tl_version}, tex(hgothbn-v.tfm) = %{tl_version}
Provides:       tex(hgotheb-h.tfm) = %{tl_version}, tex(hgotheb-v.tfm) = %{tl_version}
Provides:       tex(hgothebn-h.tfm) = %{tl_version}, tex(hgothebn-v.tfm) = %{tl_version}
Provides:       tex(hgothr-h.tfm) = %{tl_version}, tex(hgothr-v.tfm) = %{tl_version}
Provides:       tex(hgothrn-h.tfm) = %{tl_version}, tex(hgothrn-v.tfm) = %{tl_version}
Provides:       tex(hirakaku-w3-h.tfm) = %{tl_version}, tex(hirakaku-w3-v.tfm) = %{tl_version}
Provides:       tex(hirakaku-w6-h.tfm) = %{tl_version}, tex(hirakaku-w6-v.tfm) = %{tl_version}
Provides:       tex(hiramaru-w4-h.tfm) = %{tl_version}, tex(hiramaru-w4-v.tfm) = %{tl_version}
Provides:       tex(hiramin-w3-h.tfm) = %{tl_version}, tex(hiramin-w3-v.tfm) = %{tl_version}
Provides:       tex(hiramin-w6-h.tfm) = %{tl_version}, tex(hiramin-w6-v.tfm) = %{tl_version}
Provides:       tex(hmgothr-h.tfm) = %{tl_version}, tex(hmgothr-v.tfm) = %{tl_version}
Provides:       tex(hmgothrn-h.tfm) = %{tl_version}, tex(hmgothrn-v.tfm) = %{tl_version}
Provides:       tex(hminb-h.tfm) = %{tl_version}, tex(hminb-v.tfm) = %{tl_version}
Provides:       tex(hminbn-h.tfm) = %{tl_version}, tex(hminbn-v.tfm) = %{tl_version}
Provides:       tex(hminl-h.tfm) = %{tl_version}, tex(hminl-v.tfm) = %{tl_version}
Provides:       tex(hminln-h.tfm) = %{tl_version}, tex(hminln-v.tfm) = %{tl_version}
Provides:       tex(hminr-h.tfm) = %{tl_version}, tex(hminr-v.tfm) = %{tl_version}
Provides:       tex(hminrn-h.tfm) = %{tl_version}, tex(hminrn-v.tfm) = %{tl_version}
Provides:       tex(nmlgothb-h.tfm) = %{tl_version}, tex(nmlgothb-v.tfm) = %{tl_version}
Provides:       tex(nmlgothbn-h.tfm) = %{tl_version}, tex(nmlgothbn-v.tfm) = %{tl_version}
Provides:       tex(nmlgotheb-h.tfm) = %{tl_version}, tex(nmlgotheb-v.tfm) = %{tl_version}
Provides:       tex(nmlgothebn-h.tfm) = %{tl_version}, tex(nmlgothebn-v.tfm) = %{tl_version}
Provides:       tex(nmlgothr-h.tfm) = %{tl_version}, tex(nmlgothr-v.tfm) = %{tl_version}
Provides:       tex(nmlgothrn-h.tfm) = %{tl_version}, tex(nmlgothrn-v.tfm) = %{tl_version}
Provides:       tex(nmlmgothr-h.tfm) = %{tl_version}, tex(nmlmgothr-v.tfm) = %{tl_version}
Provides:       tex(nmlmgothrn-h.tfm) = %{tl_version}, tex(nmlmgothrn-v.tfm) = %{tl_version}
Provides:       tex(nmlminb-h.tfm) = %{tl_version}, tex(nmlminb-v.tfm) = %{tl_version}
Provides:       tex(nmlminbn-h.tfm) = %{tl_version}, tex(nmlminbn-v.tfm) = %{tl_version}
Provides:       tex(nmlminl-h.tfm) = %{tl_version}, tex(nmlminl-v.tfm) = %{tl_version}
Provides:       tex(nmlminln-h.tfm) = %{tl_version}, tex(nmlminln-v.tfm) = %{tl_version}
Provides:       tex(nmlminr-h.tfm) = %{tl_version}, tex(nmlminr-v.tfm) = %{tl_version}
Provides:       tex(nmlminrn-h.tfm) = %{tl_version}, tex(nmlminrn-v.tfm) = %{tl_version}
Provides:       tex(otf-ccgr-h.tfm) = %{tl_version}, tex(otf-ccgr-v.tfm) = %{tl_version}
Provides:       tex(otf-ccmr-h.tfm) = %{tl_version}, tex(otf-ccmr-v.tfm) = %{tl_version}
Provides:       tex(otf-cjgb-h.tfm) = %{tl_version}, tex(otf-cjgb-v.tfm) = %{tl_version}
Provides:       tex(otf-cjge-h.tfm) = %{tl_version}, tex(otf-cjge-v.tfm) = %{tl_version}
Provides:       tex(otf-cjgr-h.tfm) = %{tl_version}, tex(otf-cjgr-v.tfm) = %{tl_version}
Provides:       tex(otf-cjmb-h.tfm) = %{tl_version}, tex(otf-cjmb-v.tfm) = %{tl_version}
Provides:       tex(otf-cjmgr-h.tfm) = %{tl_version}, tex(otf-cjmgr-v.tfm) = %{tl_version}
Provides:       tex(otf-cjml-h.tfm) = %{tl_version}, tex(otf-cjml-v.tfm) = %{tl_version}
Provides:       tex(otf-cjmr-h.tfm) = %{tl_version}, tex(otf-cjmr-v.tfm) = %{tl_version}
Provides:       tex(otf-ckgr-h.tfm) = %{tl_version}, tex(otf-ckgr-v.tfm) = %{tl_version}
Provides:       tex(otf-ckmr-h.tfm) = %{tl_version}, tex(otf-ckmr-v.tfm) = %{tl_version}
Provides:       tex(otf-ctgr-h.tfm) = %{tl_version}, tex(otf-ctgr-v.tfm) = %{tl_version}
Provides:       tex(otf-ctmr-h.tfm) = %{tl_version}, tex(otf-ctmr-v.tfm) = %{tl_version}
Provides:       tex(otf-ucgr-h.tfm) = %{tl_version}, tex(otf-ucgr-v.tfm) = %{tl_version}
Provides:       tex(otf-ucmr-h.tfm) = %{tl_version}, tex(otf-ucmr-v.tfm) = %{tl_version}
Provides:       tex(otf-ujgb-h.tfm) = %{tl_version}, tex(otf-ujgb-v.tfm) = %{tl_version}
Provides:       tex(otf-ujgbn-h.tfm) = %{tl_version}, tex(otf-ujgbn-v.tfm) = %{tl_version}
Provides:       tex(otf-ujge-h.tfm) = %{tl_version}, tex(otf-ujge-v.tfm) = %{tl_version}
Provides:       tex(otf-ujgen-h.tfm) = %{tl_version}, tex(otf-ujgen-v.tfm) = %{tl_version}
Provides:       tex(otf-ujgr-h.tfm) = %{tl_version}, tex(otf-ujgr-v.tfm) = %{tl_version}
Provides:       tex(otf-ujgrn-h.tfm) = %{tl_version}, tex(otf-ujgrn-v.tfm) = %{tl_version}
Provides:       tex(otf-ujmb-h.tfm) = %{tl_version}, tex(otf-ujmb-v.tfm) = %{tl_version}
Provides:       tex(otf-ujmbn-h.tfm) = %{tl_version}, tex(otf-ujmbn-v.tfm) = %{tl_version}
Provides:       tex(otf-ujmgr-h.tfm) = %{tl_version}, tex(otf-ujmgr-v.tfm) = %{tl_version}
Provides:       tex(otf-ujmgrn-h.tfm) = %{tl_version}, tex(otf-ujmgrn-v.tfm) = %{tl_version}
Provides:       tex(otf-ujml-h.tfm) = %{tl_version}, tex(otf-ujml-v.tfm) = %{tl_version}
Provides:       tex(otf-ujmln-h.tfm) = %{tl_version}, tex(otf-ujmln-v.tfm) = %{tl_version}
Provides:       tex(otf-ujmr-h.tfm) = %{tl_version}, tex(otf-ujmr-v.tfm) = %{tl_version}
Provides:       tex(otf-ujmrn-h.tfm) = %{tl_version}, tex(otf-ujmrn-v.tfm) = %{tl_version}
Provides:       tex(otf-ukgr-h.tfm) = %{tl_version}, tex(otf-ukgr-v.tfm) = %{tl_version}
Provides:       tex(otf-ukmr-h.tfm) = %{tl_version}, tex(otf-ukmr-v.tfm) = %{tl_version}
Provides:       tex(otf-utgr-h.tfm) = %{tl_version}, tex(otf-utgr-v.tfm) = %{tl_version}
Provides:       tex(otf-utmr-h.tfm) = %{tl_version}, tex(otf-utmr-v.tfm) = %{tl_version}
Provides:       tex(phirakakuw3-h.tfm) = %{tl_version}, tex(phirakakuw3-v.tfm) = %{tl_version}
Provides:       tex(phirakakuw6-h.tfm) = %{tl_version}, tex(phirakakuw6-v.tfm) = %{tl_version}
Provides:       tex(phiramaruw4-h.tfm) = %{tl_version}, tex(phiramaruw4-v.tfm) = %{tl_version}
Provides:       tex(phiraminw3-h.tfm) = %{tl_version}, tex(phiraminw3-v.tfm) = %{tl_version}
Provides:       tex(phiraminw6-h.tfm) = %{tl_version}, tex(phiraminw6-v.tfm) = %{tl_version}
Provides:       tex(rubygothb-h.tfm) = %{tl_version}, tex(rubygothb-v.tfm) = %{tl_version}
Provides:       tex(rubygotheb-h.tfm) = %{tl_version}, tex(rubygotheb-v.tfm) = %{tl_version}
Provides:       tex(rubygothr-h.tfm) = %{tl_version}, tex(rubygothr-v.tfm) = %{tl_version}
Provides:       tex(rubymgothr-h.tfm) = %{tl_version}, tex(rubymgothr-v.tfm) = %{tl_version}
Provides:       tex(rubyminb-h.tfm) = %{tl_version}, tex(rubyminb-v.tfm) = %{tl_version}
Provides:       tex(rubyminl-h.tfm) = %{tl_version}, tex(rubyminl-v.tfm) = %{tl_version}
Provides:       tex(rubyminr-h.tfm) = %{tl_version}, tex(rubyminr-v.tfm) = %{tl_version}
Provides:       tex(utfcgr0-h.tfm) = %{tl_version}, tex(utfcgr0-v.tfm) = %{tl_version}
Provides:       tex(utfcgr1-h.tfm) = %{tl_version}, tex(utfcgr1-v.tfm) = %{tl_version}
Provides:       tex(utfcgr2-h.tfm) = %{tl_version}, tex(utfcgr2-v.tfm) = %{tl_version}
Provides:       tex(utfcgr3-h.tfm) = %{tl_version}, tex(utfcgr3-v.tfm) = %{tl_version}
Provides:       tex(utfcgr4-h.tfm) = %{tl_version}, tex(utfcgr4-v.tfm) = %{tl_version}
Provides:       tex(utfcgr5-h.tfm) = %{tl_version}, tex(utfcgr5-v.tfm) = %{tl_version}
Provides:       tex(utfcgr6-h.tfm) = %{tl_version}, tex(utfcgr6-v.tfm) = %{tl_version}
Provides:       tex(utfcgr7-h.tfm) = %{tl_version}, tex(utfcgr7-v.tfm) = %{tl_version}
Provides:       tex(utfcgr8-h.tfm) = %{tl_version}, tex(utfcgr8-v.tfm) = %{tl_version}
Provides:       tex(utfcgr9-h.tfm) = %{tl_version}, tex(utfcgr9-v.tfm) = %{tl_version}
Provides:       tex(utfcgra-h.tfm) = %{tl_version}, tex(utfcgra-v.tfm) = %{tl_version}
Provides:       tex(utfcgrb-h.tfm) = %{tl_version}, tex(utfcgrb-v.tfm) = %{tl_version}
Provides:       tex(utfcgrc-h.tfm) = %{tl_version}, tex(utfcgrc-v.tfm) = %{tl_version}
Provides:       tex(utfcgrd-h.tfm) = %{tl_version}, tex(utfcgrd-v.tfm) = %{tl_version}
Provides:       tex(utfcgre-h.tfm) = %{tl_version}, tex(utfcgre-v.tfm) = %{tl_version}
Provides:       tex(utfcgrf-h.tfm) = %{tl_version}, tex(utfcgrf-v.tfm) = %{tl_version}
Provides:       tex(utfcmr0-h.tfm) = %{tl_version}, tex(utfcmr0-v.tfm) = %{tl_version}
Provides:       tex(utfcmr1-h.tfm) = %{tl_version}, tex(utfcmr1-v.tfm) = %{tl_version}
Provides:       tex(utfcmr2-h.tfm) = %{tl_version}, tex(utfcmr2-v.tfm) = %{tl_version}
Provides:       tex(utfcmr3-h.tfm) = %{tl_version}, tex(utfcmr3-v.tfm) = %{tl_version}
Provides:       tex(utfcmr4-h.tfm) = %{tl_version}, tex(utfcmr4-v.tfm) = %{tl_version}
Provides:       tex(utfcmr5-h.tfm) = %{tl_version}, tex(utfcmr5-v.tfm) = %{tl_version}
Provides:       tex(utfcmr6-h.tfm) = %{tl_version}, tex(utfcmr6-v.tfm) = %{tl_version}
Provides:       tex(utfcmr7-h.tfm) = %{tl_version}, tex(utfcmr7-v.tfm) = %{tl_version}
Provides:       tex(utfcmr8-h.tfm) = %{tl_version}, tex(utfcmr8-v.tfm) = %{tl_version}
Provides:       tex(utfcmr9-h.tfm) = %{tl_version}, tex(utfcmr9-v.tfm) = %{tl_version}
Provides:       tex(utfcmra-h.tfm) = %{tl_version}, tex(utfcmra-v.tfm) = %{tl_version}
Provides:       tex(utfcmrb-h.tfm) = %{tl_version}, tex(utfcmrb-v.tfm) = %{tl_version}
Provides:       tex(utfcmrc-h.tfm) = %{tl_version}, tex(utfcmrc-v.tfm) = %{tl_version}
Provides:       tex(utfcmrd-h.tfm) = %{tl_version}, tex(utfcmrd-v.tfm) = %{tl_version}
Provides:       tex(utfcmre-h.tfm) = %{tl_version}, tex(utfcmre-v.tfm) = %{tl_version}
Provides:       tex(utfcmrf-h.tfm) = %{tl_version}, tex(utfcmrf-v.tfm) = %{tl_version}
Provides:       tex(utfgr0-h.tfm) = %{tl_version}, tex(utfgr0-v.tfm) = %{tl_version}
Provides:       tex(utfgr1-h.tfm) = %{tl_version}, tex(utfgr1-v.tfm) = %{tl_version}
Provides:       tex(utfgr2-h.tfm) = %{tl_version}, tex(utfgr2-v.tfm) = %{tl_version}
Provides:       tex(utfgr3-h.tfm) = %{tl_version}, tex(utfgr3-v.tfm) = %{tl_version}
Provides:       tex(utfgr4-h.tfm) = %{tl_version}, tex(utfgr4-v.tfm) = %{tl_version}
Provides:       tex(utfgr5-h.tfm) = %{tl_version}, tex(utfgr5-v.tfm) = %{tl_version}
Provides:       tex(utfgr6-h.tfm) = %{tl_version}, tex(utfgr6-v.tfm) = %{tl_version}
Provides:       tex(utfgr7-h.tfm) = %{tl_version}, tex(utfgr7-v.tfm) = %{tl_version}
Provides:       tex(utfgr8-h.tfm) = %{tl_version}, tex(utfgr8-v.tfm) = %{tl_version}
Provides:       tex(utfgr9-h.tfm) = %{tl_version}, tex(utfgr9-v.tfm) = %{tl_version}
Provides:       tex(utfgra-h.tfm) = %{tl_version}, tex(utfgra-v.tfm) = %{tl_version}
Provides:       tex(utfgrb-h.tfm) = %{tl_version}, tex(utfgrb-v.tfm) = %{tl_version}
Provides:       tex(utfgrc-h.tfm) = %{tl_version}, tex(utfgrc-v.tfm) = %{tl_version}
Provides:       tex(utfgrd-h.tfm) = %{tl_version}, tex(utfgrd-v.tfm) = %{tl_version}
Provides:       tex(utfgre-h.tfm) = %{tl_version}, tex(utfgre-v.tfm) = %{tl_version}
Provides:       tex(utfgrf-h.tfm) = %{tl_version}, tex(utfgrf-v.tfm) = %{tl_version}
Provides:       tex(utfjgb0-h.tfm) = %{tl_version}, tex(utfjgb0-v.tfm) = %{tl_version}
Provides:       tex(utfjgb1-h.tfm) = %{tl_version}, tex(utfjgb1-v.tfm) = %{tl_version}
Provides:       tex(utfjgb2-h.tfm) = %{tl_version}, tex(utfjgb2-v.tfm) = %{tl_version}
Provides:       tex(utfjgb3-h.tfm) = %{tl_version}, tex(utfjgb3-v.tfm) = %{tl_version}
Provides:       tex(utfjgb4-h.tfm) = %{tl_version}, tex(utfjgb4-v.tfm) = %{tl_version}
Provides:       tex(utfjgb5-h.tfm) = %{tl_version}, tex(utfjgb5-v.tfm) = %{tl_version}
Provides:       tex(utfjgb6-h.tfm) = %{tl_version}, tex(utfjgb6-v.tfm) = %{tl_version}
Provides:       tex(utfjgb7-h.tfm) = %{tl_version}, tex(utfjgb7-v.tfm) = %{tl_version}
Provides:       tex(utfjgb8-h.tfm) = %{tl_version}, tex(utfjgb8-v.tfm) = %{tl_version}
Provides:       tex(utfjgb9-h.tfm) = %{tl_version}, tex(utfjgb9-v.tfm) = %{tl_version}
Provides:       tex(utfjgba-h.tfm) = %{tl_version}, tex(utfjgba-v.tfm) = %{tl_version}
Provides:       tex(utfjgbb-h.tfm) = %{tl_version}, tex(utfjgbb-v.tfm) = %{tl_version}
Provides:       tex(utfjgbc-h.tfm) = %{tl_version}, tex(utfjgbc-v.tfm) = %{tl_version}
Provides:       tex(utfjgbd-h.tfm) = %{tl_version}, tex(utfjgbd-v.tfm) = %{tl_version}
Provides:       tex(utfjgbe-h.tfm) = %{tl_version}, tex(utfjgbe-v.tfm) = %{tl_version}
Provides:       tex(utfjgbf-h.tfm) = %{tl_version}, tex(utfjgbf-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn0-h.tfm) = %{tl_version}, tex(utfjgbn0-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn1-h.tfm) = %{tl_version}, tex(utfjgbn1-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn2-h.tfm) = %{tl_version}, tex(utfjgbn2-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn3-h.tfm) = %{tl_version}, tex(utfjgbn3-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn4-h.tfm) = %{tl_version}, tex(utfjgbn4-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn5-h.tfm) = %{tl_version}, tex(utfjgbn5-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn6-h.tfm) = %{tl_version}, tex(utfjgbn6-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn7-h.tfm) = %{tl_version}, tex(utfjgbn7-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn8-h.tfm) = %{tl_version}, tex(utfjgbn8-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn9-h.tfm) = %{tl_version}, tex(utfjgbn9-v.tfm) = %{tl_version}
Provides:       tex(utfjgbna-h.tfm) = %{tl_version}, tex(utfjgbna-v.tfm) = %{tl_version}
Provides:       tex(utfjgbnb-h.tfm) = %{tl_version}, tex(utfjgbnb-v.tfm) = %{tl_version}
Provides:       tex(utfjgbnc-h.tfm) = %{tl_version}, tex(utfjgbnc-v.tfm) = %{tl_version}
Provides:       tex(utfjgbnd-h.tfm) = %{tl_version}, tex(utfjgbnd-v.tfm) = %{tl_version}
Provides:       tex(utfjgbne-h.tfm) = %{tl_version}, tex(utfjgbne-v.tfm) = %{tl_version}
Provides:       tex(utfjgbnf-h.tfm) = %{tl_version}, tex(utfjgbnf-v.tfm) = %{tl_version}
Provides:       tex(utfjge0-h.tfm) = %{tl_version}, tex(utfjge0-v.tfm) = %{tl_version}
Provides:       tex(utfjge1-h.tfm) = %{tl_version}, tex(utfjge1-v.tfm) = %{tl_version}
Provides:       tex(utfjge2-h.tfm) = %{tl_version}, tex(utfjge2-v.tfm) = %{tl_version}
Provides:       tex(utfjge3-h.tfm) = %{tl_version}, tex(utfjge3-v.tfm) = %{tl_version}
Provides:       tex(utfjge4-h.tfm) = %{tl_version}, tex(utfjge4-v.tfm) = %{tl_version}
Provides:       tex(utfjge5-h.tfm) = %{tl_version}, tex(utfjge5-v.tfm) = %{tl_version}
Provides:       tex(utfjge6-h.tfm) = %{tl_version}, tex(utfjge6-v.tfm) = %{tl_version}
Provides:       tex(utfjge7-h.tfm) = %{tl_version}, tex(utfjge7-v.tfm) = %{tl_version}
Provides:       tex(utfjge8-h.tfm) = %{tl_version}, tex(utfjge8-v.tfm) = %{tl_version}
Provides:       tex(utfjge9-h.tfm) = %{tl_version}, tex(utfjge9-v.tfm) = %{tl_version}
Provides:       tex(utfjgea-h.tfm) = %{tl_version}, tex(utfjgea-v.tfm) = %{tl_version}
Provides:       tex(utfjgeb-h.tfm) = %{tl_version}, tex(utfjgeb-v.tfm) = %{tl_version}
Provides:       tex(utfjgec-h.tfm) = %{tl_version}, tex(utfjgec-v.tfm) = %{tl_version}
Provides:       tex(utfjged-h.tfm) = %{tl_version}, tex(utfjged-v.tfm) = %{tl_version}
Provides:       tex(utfjgee-h.tfm) = %{tl_version}, tex(utfjgee-v.tfm) = %{tl_version}
Provides:       tex(utfjgef-h.tfm) = %{tl_version}, tex(utfjgef-v.tfm) = %{tl_version}
Provides:       tex(utfjgen0-h.tfm) = %{tl_version}, tex(utfjgen0-v.tfm) = %{tl_version}
Provides:       tex(utfjgen1-h.tfm) = %{tl_version}, tex(utfjgen1-v.tfm) = %{tl_version}
Provides:       tex(utfjgen2-h.tfm) = %{tl_version}, tex(utfjgen2-v.tfm) = %{tl_version}
Provides:       tex(utfjgen3-h.tfm) = %{tl_version}, tex(utfjgen3-v.tfm) = %{tl_version}
Provides:       tex(utfjgen4-h.tfm) = %{tl_version}, tex(utfjgen4-v.tfm) = %{tl_version}
Provides:       tex(utfjgen5-h.tfm) = %{tl_version}, tex(utfjgen5-v.tfm) = %{tl_version}
Provides:       tex(utfjgen6-h.tfm) = %{tl_version}, tex(utfjgen6-v.tfm) = %{tl_version}
Provides:       tex(utfjgen7-h.tfm) = %{tl_version}, tex(utfjgen7-v.tfm) = %{tl_version}
Provides:       tex(utfjgen8-h.tfm) = %{tl_version}, tex(utfjgen8-v.tfm) = %{tl_version}
Provides:       tex(utfjgen9-h.tfm) = %{tl_version}, tex(utfjgen9-v.tfm) = %{tl_version}
Provides:       tex(utfjgena-h.tfm) = %{tl_version}, tex(utfjgena-v.tfm) = %{tl_version}
Provides:       tex(utfjgenb-h.tfm) = %{tl_version}, tex(utfjgenb-v.tfm) = %{tl_version}
Provides:       tex(utfjgenc-h.tfm) = %{tl_version}, tex(utfjgenc-v.tfm) = %{tl_version}
Provides:       tex(utfjgend-h.tfm) = %{tl_version}, tex(utfjgend-v.tfm) = %{tl_version}
Provides:       tex(utfjgene-h.tfm) = %{tl_version}, tex(utfjgene-v.tfm) = %{tl_version}
Provides:       tex(utfjgenf-h.tfm) = %{tl_version}, tex(utfjgenf-v.tfm) = %{tl_version}
Provides:       tex(utfjgr0-h.tfm) = %{tl_version}, tex(utfjgr0-v.tfm) = %{tl_version}
Provides:       tex(utfjgr1-h.tfm) = %{tl_version}, tex(utfjgr1-v.tfm) = %{tl_version}
Provides:       tex(utfjgr2-h.tfm) = %{tl_version}, tex(utfjgr2-v.tfm) = %{tl_version}
Provides:       tex(utfjgr3-h.tfm) = %{tl_version}, tex(utfjgr3-v.tfm) = %{tl_version}
Provides:       tex(utfjgr4-h.tfm) = %{tl_version}, tex(utfjgr4-v.tfm) = %{tl_version}
Provides:       tex(utfjgr5-h.tfm) = %{tl_version}, tex(utfjgr5-v.tfm) = %{tl_version}
Provides:       tex(utfjgr6-h.tfm) = %{tl_version}, tex(utfjgr6-v.tfm) = %{tl_version}
Provides:       tex(utfjgr7-h.tfm) = %{tl_version}, tex(utfjgr7-v.tfm) = %{tl_version}
Provides:       tex(utfjgr8-h.tfm) = %{tl_version}, tex(utfjgr8-v.tfm) = %{tl_version}
Provides:       tex(utfjgr9-h.tfm) = %{tl_version}, tex(utfjgr9-v.tfm) = %{tl_version}
Provides:       tex(utfjgra-h.tfm) = %{tl_version}, tex(utfjgra-v.tfm) = %{tl_version}
Provides:       tex(utfjgrb-h.tfm) = %{tl_version}, tex(utfjgrb-v.tfm) = %{tl_version}
Provides:       tex(utfjgrc-h.tfm) = %{tl_version}, tex(utfjgrc-v.tfm) = %{tl_version}
Provides:       tex(utfjgrd-h.tfm) = %{tl_version}, tex(utfjgrd-v.tfm) = %{tl_version}
Provides:       tex(utfjgre-h.tfm) = %{tl_version}, tex(utfjgre-v.tfm) = %{tl_version}
Provides:       tex(utfjgrf-h.tfm) = %{tl_version}, tex(utfjgrf-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn0-h.tfm) = %{tl_version}, tex(utfjgrn0-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn1-h.tfm) = %{tl_version}, tex(utfjgrn1-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn2-h.tfm) = %{tl_version}, tex(utfjgrn2-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn3-h.tfm) = %{tl_version}, tex(utfjgrn3-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn4-h.tfm) = %{tl_version}, tex(utfjgrn4-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn5-h.tfm) = %{tl_version}, tex(utfjgrn5-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn6-h.tfm) = %{tl_version}, tex(utfjgrn6-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn7-h.tfm) = %{tl_version}, tex(utfjgrn7-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn8-h.tfm) = %{tl_version}, tex(utfjgrn8-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn9-h.tfm) = %{tl_version}, tex(utfjgrn9-v.tfm) = %{tl_version}
Provides:       tex(utfjgrna-h.tfm) = %{tl_version}, tex(utfjgrna-v.tfm) = %{tl_version}
Provides:       tex(utfjgrnb-h.tfm) = %{tl_version}, tex(utfjgrnb-v.tfm) = %{tl_version}
Provides:       tex(utfjgrnc-h.tfm) = %{tl_version}, tex(utfjgrnc-v.tfm) = %{tl_version}
Provides:       tex(utfjgrnd-h.tfm) = %{tl_version}, tex(utfjgrnd-v.tfm) = %{tl_version}
Provides:       tex(utfjgrne-h.tfm) = %{tl_version}, tex(utfjgrne-v.tfm) = %{tl_version}
Provides:       tex(utfjgrnf-h.tfm) = %{tl_version}, tex(utfjgrnf-v.tfm) = %{tl_version}
Provides:       tex(utfjmb0-h.tfm) = %{tl_version}, tex(utfjmb0-v.tfm) = %{tl_version}
Provides:       tex(utfjmb1-h.tfm) = %{tl_version}, tex(utfjmb1-v.tfm) = %{tl_version}
Provides:       tex(utfjmb2-h.tfm) = %{tl_version}, tex(utfjmb2-v.tfm) = %{tl_version}
Provides:       tex(utfjmb3-h.tfm) = %{tl_version}, tex(utfjmb3-v.tfm) = %{tl_version}
Provides:       tex(utfjmb4-h.tfm) = %{tl_version}, tex(utfjmb4-v.tfm) = %{tl_version}
Provides:       tex(utfjmb5-h.tfm) = %{tl_version}, tex(utfjmb5-v.tfm) = %{tl_version}
Provides:       tex(utfjmb6-h.tfm) = %{tl_version}, tex(utfjmb6-v.tfm) = %{tl_version}
Provides:       tex(utfjmb7-h.tfm) = %{tl_version}, tex(utfjmb7-v.tfm) = %{tl_version}
Provides:       tex(utfjmb8-h.tfm) = %{tl_version}, tex(utfjmb8-v.tfm) = %{tl_version}
Provides:       tex(utfjmb9-h.tfm) = %{tl_version}, tex(utfjmb9-v.tfm) = %{tl_version}
Provides:       tex(utfjmba-h.tfm) = %{tl_version}, tex(utfjmba-v.tfm) = %{tl_version}
Provides:       tex(utfjmbb-h.tfm) = %{tl_version}, tex(utfjmbb-v.tfm) = %{tl_version}
Provides:       tex(utfjmbc-h.tfm) = %{tl_version}, tex(utfjmbc-v.tfm) = %{tl_version}
Provides:       tex(utfjmbd-h.tfm) = %{tl_version}, tex(utfjmbd-v.tfm) = %{tl_version}
Provides:       tex(utfjmbe-h.tfm) = %{tl_version}, tex(utfjmbe-v.tfm) = %{tl_version}
Provides:       tex(utfjmbf-h.tfm) = %{tl_version}, tex(utfjmbf-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn0-h.tfm) = %{tl_version}, tex(utfjmbn0-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn1-h.tfm) = %{tl_version}, tex(utfjmbn1-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn2-h.tfm) = %{tl_version}, tex(utfjmbn2-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn3-h.tfm) = %{tl_version}, tex(utfjmbn3-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn4-h.tfm) = %{tl_version}, tex(utfjmbn4-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn5-h.tfm) = %{tl_version}, tex(utfjmbn5-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn6-h.tfm) = %{tl_version}, tex(utfjmbn6-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn7-h.tfm) = %{tl_version}, tex(utfjmbn7-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn8-h.tfm) = %{tl_version}, tex(utfjmbn8-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn9-h.tfm) = %{tl_version}, tex(utfjmbn9-v.tfm) = %{tl_version}
Provides:       tex(utfjmbna-h.tfm) = %{tl_version}, tex(utfjmbna-v.tfm) = %{tl_version}
Provides:       tex(utfjmbnb-h.tfm) = %{tl_version}, tex(utfjmbnb-v.tfm) = %{tl_version}
Provides:       tex(utfjmbnc-h.tfm) = %{tl_version}, tex(utfjmbnc-v.tfm) = %{tl_version}
Provides:       tex(utfjmbnd-h.tfm) = %{tl_version}, tex(utfjmbnd-v.tfm) = %{tl_version}
Provides:       tex(utfjmbne-h.tfm) = %{tl_version}, tex(utfjmbne-v.tfm) = %{tl_version}
Provides:       tex(utfjmbnf-h.tfm) = %{tl_version}, tex(utfjmbnf-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr0-h.tfm) = %{tl_version}, tex(utfjmgr0-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr1-h.tfm) = %{tl_version}, tex(utfjmgr1-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr2-h.tfm) = %{tl_version}, tex(utfjmgr2-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr3-h.tfm) = %{tl_version}, tex(utfjmgr3-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr4-h.tfm) = %{tl_version}, tex(utfjmgr4-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr5-h.tfm) = %{tl_version}, tex(utfjmgr5-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr6-h.tfm) = %{tl_version}, tex(utfjmgr6-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr7-h.tfm) = %{tl_version}, tex(utfjmgr7-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr8-h.tfm) = %{tl_version}, tex(utfjmgr8-v.tfm) = %{tl_version}
Provides:       tex(utfjmgr9-h.tfm) = %{tl_version}, tex(utfjmgr9-v.tfm) = %{tl_version}
Provides:       tex(utfjmgra-h.tfm) = %{tl_version}, tex(utfjmgra-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrb-h.tfm) = %{tl_version}, tex(utfjmgrb-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrc-h.tfm) = %{tl_version}, tex(utfjmgrc-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrd-h.tfm) = %{tl_version}, tex(utfjmgrd-v.tfm) = %{tl_version}
Provides:       tex(utfjmgre-h.tfm) = %{tl_version}, tex(utfjmgre-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrf-h.tfm) = %{tl_version}, tex(utfjmgrf-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn0-h.tfm) = %{tl_version}, tex(utfjmgrn0-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn1-h.tfm) = %{tl_version}, tex(utfjmgrn1-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn2-h.tfm) = %{tl_version}, tex(utfjmgrn2-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn3-h.tfm) = %{tl_version}, tex(utfjmgrn3-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn4-h.tfm) = %{tl_version}, tex(utfjmgrn4-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn5-h.tfm) = %{tl_version}, tex(utfjmgrn5-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn6-h.tfm) = %{tl_version}, tex(utfjmgrn6-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn7-h.tfm) = %{tl_version}, tex(utfjmgrn7-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn8-h.tfm) = %{tl_version}, tex(utfjmgrn8-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn9-h.tfm) = %{tl_version}, tex(utfjmgrn9-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrna-h.tfm) = %{tl_version}, tex(utfjmgrna-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrnb-h.tfm) = %{tl_version}, tex(utfjmgrnb-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrnc-h.tfm) = %{tl_version}, tex(utfjmgrnc-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrnd-h.tfm) = %{tl_version}, tex(utfjmgrnd-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrne-h.tfm) = %{tl_version}, tex(utfjmgrne-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrnf-h.tfm) = %{tl_version}, tex(utfjmgrnf-v.tfm) = %{tl_version}
Provides:       tex(utfjml0-h.tfm) = %{tl_version}, tex(utfjml0-v.tfm) = %{tl_version}
Provides:       tex(utfjml1-h.tfm) = %{tl_version}, tex(utfjml1-v.tfm) = %{tl_version}
Provides:       tex(utfjml2-h.tfm) = %{tl_version}, tex(utfjml2-v.tfm) = %{tl_version}
Provides:       tex(utfjml3-h.tfm) = %{tl_version}, tex(utfjml3-v.tfm) = %{tl_version}
Provides:       tex(utfjml4-h.tfm) = %{tl_version}, tex(utfjml4-v.tfm) = %{tl_version}
Provides:       tex(utfjml5-h.tfm) = %{tl_version}, tex(utfjml5-v.tfm) = %{tl_version}
Provides:       tex(utfjml6-h.tfm) = %{tl_version}, tex(utfjml6-v.tfm) = %{tl_version}
Provides:       tex(utfjml7-h.tfm) = %{tl_version}, tex(utfjml7-v.tfm) = %{tl_version}
Provides:       tex(utfjml8-h.tfm) = %{tl_version}, tex(utfjml8-v.tfm) = %{tl_version}
Provides:       tex(utfjml9-h.tfm) = %{tl_version}, tex(utfjml9-v.tfm) = %{tl_version}
Provides:       tex(utfjmla-h.tfm) = %{tl_version}, tex(utfjmla-v.tfm) = %{tl_version}
Provides:       tex(utfjmlb-h.tfm) = %{tl_version}, tex(utfjmlb-v.tfm) = %{tl_version}
Provides:       tex(utfjmlc-h.tfm) = %{tl_version}, tex(utfjmlc-v.tfm) = %{tl_version}
Provides:       tex(utfjmld-h.tfm) = %{tl_version}, tex(utfjmld-v.tfm) = %{tl_version}
Provides:       tex(utfjmle-h.tfm) = %{tl_version}, tex(utfjmle-v.tfm) = %{tl_version}
Provides:       tex(utfjmlf-h.tfm) = %{tl_version}, tex(utfjmlf-v.tfm) = %{tl_version}
Provides:       tex(utfjmln0-h.tfm) = %{tl_version}, tex(utfjmln0-v.tfm) = %{tl_version}
Provides:       tex(utfjmln1-h.tfm) = %{tl_version}, tex(utfjmln1-v.tfm) = %{tl_version}
Provides:       tex(utfjmln2-h.tfm) = %{tl_version}, tex(utfjmln2-v.tfm) = %{tl_version}
Provides:       tex(utfjmln3-h.tfm) = %{tl_version}, tex(utfjmln3-v.tfm) = %{tl_version}
Provides:       tex(utfjmln4-h.tfm) = %{tl_version}, tex(utfjmln4-v.tfm) = %{tl_version}
Provides:       tex(utfjmln5-h.tfm) = %{tl_version}, tex(utfjmln5-v.tfm) = %{tl_version}
Provides:       tex(utfjmln6-h.tfm) = %{tl_version}, tex(utfjmln6-v.tfm) = %{tl_version}
Provides:       tex(utfjmln7-h.tfm) = %{tl_version}, tex(utfjmln7-v.tfm) = %{tl_version}
Provides:       tex(utfjmln8-h.tfm) = %{tl_version}, tex(utfjmln8-v.tfm) = %{tl_version}
Provides:       tex(utfjmln9-h.tfm) = %{tl_version}, tex(utfjmln9-v.tfm) = %{tl_version}
Provides:       tex(utfjmlna-h.tfm) = %{tl_version}, tex(utfjmlna-v.tfm) = %{tl_version}
Provides:       tex(utfjmlnb-h.tfm) = %{tl_version}, tex(utfjmlnb-v.tfm) = %{tl_version}
Provides:       tex(utfjmlnc-h.tfm) = %{tl_version}, tex(utfjmlnc-v.tfm) = %{tl_version}
Provides:       tex(utfjmlnd-h.tfm) = %{tl_version}, tex(utfjmlnd-v.tfm) = %{tl_version}
Provides:       tex(utfjmlne-h.tfm) = %{tl_version}, tex(utfjmlne-v.tfm) = %{tl_version}
Provides:       tex(utfjmlnf-h.tfm) = %{tl_version}, tex(utfjmlnf-v.tfm) = %{tl_version}
Provides:       tex(utfjmr0-h.tfm) = %{tl_version}, tex(utfjmr0-v.tfm) = %{tl_version}
Provides:       tex(utfjmr1-h.tfm) = %{tl_version}, tex(utfjmr1-v.tfm) = %{tl_version}
Provides:       tex(utfjmr2-h.tfm) = %{tl_version}, tex(utfjmr2-v.tfm) = %{tl_version}
Provides:       tex(utfjmr3-h.tfm) = %{tl_version}, tex(utfjmr3-v.tfm) = %{tl_version}
Provides:       tex(utfjmr4-h.tfm) = %{tl_version}, tex(utfjmr4-v.tfm) = %{tl_version}
Provides:       tex(utfjmr5-h.tfm) = %{tl_version}, tex(utfjmr5-v.tfm) = %{tl_version}
Provides:       tex(utfjmr6-h.tfm) = %{tl_version}, tex(utfjmr6-v.tfm) = %{tl_version}
Provides:       tex(utfjmr7-h.tfm) = %{tl_version}, tex(utfjmr7-v.tfm) = %{tl_version}
Provides:       tex(utfjmr8-h.tfm) = %{tl_version}, tex(utfjmr8-v.tfm) = %{tl_version}
Provides:       tex(utfjmr9-h.tfm) = %{tl_version}, tex(utfjmr9-v.tfm) = %{tl_version}
Provides:       tex(utfjmra-h.tfm) = %{tl_version}, tex(utfjmra-v.tfm) = %{tl_version}
Provides:       tex(utfjmrb-h.tfm) = %{tl_version}, tex(utfjmrb-v.tfm) = %{tl_version}
Provides:       tex(utfjmrc-h.tfm) = %{tl_version}, tex(utfjmrc-v.tfm) = %{tl_version}
Provides:       tex(utfjmrd-h.tfm) = %{tl_version}, tex(utfjmrd-v.tfm) = %{tl_version}
Provides:       tex(utfjmre-h.tfm) = %{tl_version}, tex(utfjmre-v.tfm) = %{tl_version}
Provides:       tex(utfjmrf-h.tfm) = %{tl_version}, tex(utfjmrf-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn0-h.tfm) = %{tl_version}, tex(utfjmrn0-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn1-h.tfm) = %{tl_version}, tex(utfjmrn1-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn2-h.tfm) = %{tl_version}, tex(utfjmrn2-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn3-h.tfm) = %{tl_version}, tex(utfjmrn3-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn4-h.tfm) = %{tl_version}, tex(utfjmrn4-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn5-h.tfm) = %{tl_version}, tex(utfjmrn5-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn6-h.tfm) = %{tl_version}, tex(utfjmrn6-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn7-h.tfm) = %{tl_version}, tex(utfjmrn7-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn8-h.tfm) = %{tl_version}, tex(utfjmrn8-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn9-h.tfm) = %{tl_version}, tex(utfjmrn9-v.tfm) = %{tl_version}
Provides:       tex(utfjmrna-h.tfm) = %{tl_version}, tex(utfjmrna-v.tfm) = %{tl_version}
Provides:       tex(utfjmrnb-h.tfm) = %{tl_version}, tex(utfjmrnb-v.tfm) = %{tl_version}
Provides:       tex(utfjmrnc-h.tfm) = %{tl_version}, tex(utfjmrnc-v.tfm) = %{tl_version}
Provides:       tex(utfjmrnd-h.tfm) = %{tl_version}, tex(utfjmrnd-v.tfm) = %{tl_version}
Provides:       tex(utfjmrne-h.tfm) = %{tl_version}, tex(utfjmrne-v.tfm) = %{tl_version}
Provides:       tex(utfjmrnf-h.tfm) = %{tl_version}, tex(utfjmrnf-v.tfm) = %{tl_version}
Provides:       tex(utfkgr0-h.tfm) = %{tl_version}, tex(utfkgr0-v.tfm) = %{tl_version}
Provides:       tex(utfkgr1-h.tfm) = %{tl_version}, tex(utfkgr1-v.tfm) = %{tl_version}
Provides:       tex(utfkgr2-h.tfm) = %{tl_version}, tex(utfkgr2-v.tfm) = %{tl_version}
Provides:       tex(utfkgr3-h.tfm) = %{tl_version}, tex(utfkgr3-v.tfm) = %{tl_version}
Provides:       tex(utfkgr4-h.tfm) = %{tl_version}, tex(utfkgr4-v.tfm) = %{tl_version}
Provides:       tex(utfkgr5-h.tfm) = %{tl_version}, tex(utfkgr5-v.tfm) = %{tl_version}
Provides:       tex(utfkgr6-h.tfm) = %{tl_version}, tex(utfkgr6-v.tfm) = %{tl_version}
Provides:       tex(utfkgr7-h.tfm) = %{tl_version}, tex(utfkgr7-v.tfm) = %{tl_version}
Provides:       tex(utfkgr8-h.tfm) = %{tl_version}, tex(utfkgr8-v.tfm) = %{tl_version}
Provides:       tex(utfkgr9-h.tfm) = %{tl_version}, tex(utfkgr9-v.tfm) = %{tl_version}
Provides:       tex(utfkgra-h.tfm) = %{tl_version}, tex(utfkgra-v.tfm) = %{tl_version}
Provides:       tex(utfkgrb-h.tfm) = %{tl_version}, tex(utfkgrb-v.tfm) = %{tl_version}
Provides:       tex(utfkgrc-h.tfm) = %{tl_version}, tex(utfkgrc-v.tfm) = %{tl_version}
Provides:       tex(utfkgrd-h.tfm) = %{tl_version}, tex(utfkgrd-v.tfm) = %{tl_version}
Provides:       tex(utfkgre-h.tfm) = %{tl_version}, tex(utfkgre-v.tfm) = %{tl_version}
Provides:       tex(utfkgrf-h.tfm) = %{tl_version}, tex(utfkgrf-v.tfm) = %{tl_version}
Provides:       tex(utfkmr0-h.tfm) = %{tl_version}, tex(utfkmr0-v.tfm) = %{tl_version}
Provides:       tex(utfkmr1-h.tfm) = %{tl_version}, tex(utfkmr1-v.tfm) = %{tl_version}
Provides:       tex(utfkmr2-h.tfm) = %{tl_version}, tex(utfkmr2-v.tfm) = %{tl_version}
Provides:       tex(utfkmr3-h.tfm) = %{tl_version}, tex(utfkmr3-v.tfm) = %{tl_version}
Provides:       tex(utfkmr4-h.tfm) = %{tl_version}, tex(utfkmr4-v.tfm) = %{tl_version}
Provides:       tex(utfkmr5-h.tfm) = %{tl_version}, tex(utfkmr5-v.tfm) = %{tl_version}
Provides:       tex(utfkmr6-h.tfm) = %{tl_version}, tex(utfkmr6-v.tfm) = %{tl_version}
Provides:       tex(utfkmr7-h.tfm) = %{tl_version}, tex(utfkmr7-v.tfm) = %{tl_version}
Provides:       tex(utfkmr8-h.tfm) = %{tl_version}, tex(utfkmr8-v.tfm) = %{tl_version}
Provides:       tex(utfkmr9-h.tfm) = %{tl_version}, tex(utfkmr9-v.tfm) = %{tl_version}
Provides:       tex(utfkmra-h.tfm) = %{tl_version}, tex(utfkmra-v.tfm) = %{tl_version}
Provides:       tex(utfkmrb-h.tfm) = %{tl_version}, tex(utfkmrb-v.tfm) = %{tl_version}
Provides:       tex(utfkmrc-h.tfm) = %{tl_version}, tex(utfkmrc-v.tfm) = %{tl_version}
Provides:       tex(utfkmrd-h.tfm) = %{tl_version}, tex(utfkmrd-v.tfm) = %{tl_version}
Provides:       tex(utfkmre-h.tfm) = %{tl_version}, tex(utfkmre-v.tfm) = %{tl_version}
Provides:       tex(utfkmrf-h.tfm) = %{tl_version}, tex(utfkmrf-v.tfm) = %{tl_version}
Provides:       tex(utfmr0-h.tfm) = %{tl_version}, tex(utfmr0-v.tfm) = %{tl_version}
Provides:       tex(utfmr1-h.tfm) = %{tl_version}, tex(utfmr1-v.tfm) = %{tl_version}
Provides:       tex(utfmr2-h.tfm) = %{tl_version}, tex(utfmr2-v.tfm) = %{tl_version}
Provides:       tex(utfmr3-h.tfm) = %{tl_version}, tex(utfmr3-v.tfm) = %{tl_version}
Provides:       tex(utfmr4-h.tfm) = %{tl_version}, tex(utfmr4-v.tfm) = %{tl_version}
Provides:       tex(utfmr5-h.tfm) = %{tl_version}, tex(utfmr5-v.tfm) = %{tl_version}
Provides:       tex(utfmr6-h.tfm) = %{tl_version}, tex(utfmr6-v.tfm) = %{tl_version}
Provides:       tex(utfmr7-h.tfm) = %{tl_version}, tex(utfmr7-v.tfm) = %{tl_version}
Provides:       tex(utfmr8-h.tfm) = %{tl_version}, tex(utfmr8-v.tfm) = %{tl_version}
Provides:       tex(utfmr9-h.tfm) = %{tl_version}, tex(utfmr9-v.tfm) = %{tl_version}
Provides:       tex(utfmra-h.tfm) = %{tl_version}, tex(utfmra-v.tfm) = %{tl_version}
Provides:       tex(utfmrb-h.tfm) = %{tl_version}, tex(utfmrb-v.tfm) = %{tl_version}
Provides:       tex(utfmrc-h.tfm) = %{tl_version}, tex(utfmrc-v.tfm) = %{tl_version}
Provides:       tex(utfmrd-h.tfm) = %{tl_version}, tex(utfmrd-v.tfm) = %{tl_version}
Provides:       tex(utfmre-h.tfm) = %{tl_version}, tex(utfmre-v.tfm) = %{tl_version}
Provides:       tex(utfmrf-h.tfm) = %{tl_version}, tex(utfmrf-v.tfm) = %{tl_version}
Provides:       tex(utftgr0-h.tfm) = %{tl_version}, tex(utftgr0-v.tfm) = %{tl_version}
Provides:       tex(utftgr1-h.tfm) = %{tl_version}, tex(utftgr1-v.tfm) = %{tl_version}
Provides:       tex(utftgr2-h.tfm) = %{tl_version}, tex(utftgr2-v.tfm) = %{tl_version}
Provides:       tex(utftgr3-h.tfm) = %{tl_version}, tex(utftgr3-v.tfm) = %{tl_version}
Provides:       tex(utftgr4-h.tfm) = %{tl_version}, tex(utftgr4-v.tfm) = %{tl_version}
Provides:       tex(utftgr5-h.tfm) = %{tl_version}, tex(utftgr5-v.tfm) = %{tl_version}
Provides:       tex(utftgr6-h.tfm) = %{tl_version}, tex(utftgr6-v.tfm) = %{tl_version}
Provides:       tex(utftgr7-h.tfm) = %{tl_version}, tex(utftgr7-v.tfm) = %{tl_version}
Provides:       tex(utftgr8-h.tfm) = %{tl_version}, tex(utftgr8-v.tfm) = %{tl_version}
Provides:       tex(utftgr9-h.tfm) = %{tl_version}, tex(utftgr9-v.tfm) = %{tl_version}
Provides:       tex(utftgra-h.tfm) = %{tl_version}, tex(utftgra-v.tfm) = %{tl_version}
Provides:       tex(utftgrb-h.tfm) = %{tl_version}, tex(utftgrb-v.tfm) = %{tl_version}
Provides:       tex(utftgrc-h.tfm) = %{tl_version}, tex(utftgrc-v.tfm) = %{tl_version}
Provides:       tex(utftgrd-h.tfm) = %{tl_version}, tex(utftgrd-v.tfm) = %{tl_version}
Provides:       tex(utftgre-h.tfm) = %{tl_version}, tex(utftgre-v.tfm) = %{tl_version}
Provides:       tex(utftgrf-h.tfm) = %{tl_version}, tex(utftgrf-v.tfm) = %{tl_version}
Provides:       tex(utftmr0-h.tfm) = %{tl_version}, tex(utftmr0-v.tfm) = %{tl_version}
Provides:       tex(utftmr1-h.tfm) = %{tl_version}, tex(utftmr1-v.tfm) = %{tl_version}
Provides:       tex(utftmr2-h.tfm) = %{tl_version}, tex(utftmr2-v.tfm) = %{tl_version}
Provides:       tex(utftmr3-h.tfm) = %{tl_version}, tex(utftmr3-v.tfm) = %{tl_version}
Provides:       tex(utftmr4-h.tfm) = %{tl_version}, tex(utftmr4-v.tfm) = %{tl_version}
Provides:       tex(utftmr5-h.tfm) = %{tl_version}, tex(utftmr5-v.tfm) = %{tl_version}
Provides:       tex(utftmr6-h.tfm) = %{tl_version}, tex(utftmr6-v.tfm) = %{tl_version}
Provides:       tex(utftmr7-h.tfm) = %{tl_version}, tex(utftmr7-v.tfm) = %{tl_version}
Provides:       tex(utftmr8-h.tfm) = %{tl_version}, tex(utftmr8-v.tfm) = %{tl_version}
Provides:       tex(utftmr9-h.tfm) = %{tl_version}, tex(utftmr9-v.tfm) = %{tl_version}
Provides:       tex(utftmra-h.tfm) = %{tl_version}, tex(utftmra-v.tfm) = %{tl_version}
Provides:       tex(utftmrb-h.tfm) = %{tl_version}, tex(utftmrb-v.tfm) = %{tl_version}
Provides:       tex(utftmrc-h.tfm) = %{tl_version}, tex(utftmrc-v.tfm) = %{tl_version}
Provides:       tex(utftmrd-h.tfm) = %{tl_version}, tex(utftmrd-v.tfm) = %{tl_version}
Provides:       tex(utftmre-h.tfm) = %{tl_version}, tex(utftmre-v.tfm) = %{tl_version}
Provides:       tex(utftmrf-h.tfm) = %{tl_version}, tex(utftmrf-v.tfm) = %{tl_version}
Provides:       tex(brsgexpgothb-h.vf) = %{tl_version}, tex(brsgexpgothb-v.vf) = %{tl_version}
Provides:       tex(brsgexpgothbn-h.vf) = %{tl_version}, tex(brsgexpgothbn-v.vf) = %{tl_version}
Provides:       tex(brsgexpgotheb-h.vf) = %{tl_version}, tex(brsgexpgotheb-v.vf) = %{tl_version}
Provides:       tex(brsgexpgothebn-h.vf) = %{tl_version}
Provides:       tex(brsgexpgothebn-v.vf) = %{tl_version}
Provides:       tex(brsgexpgothr-h.vf) = %{tl_version}, tex(brsgexpgothr-v.vf) = %{tl_version}
Provides:       tex(brsgexpgothrn-h.vf) = %{tl_version}, tex(brsgexpgothrn-v.vf) = %{tl_version}
Provides:       tex(brsgexpmgothr-h.vf) = %{tl_version}, tex(brsgexpmgothr-v.vf) = %{tl_version}
Provides:       tex(brsgexpmgothrn-h.vf) = %{tl_version}
Provides:       tex(brsgexpmgothrn-v.vf) = %{tl_version}
Provides:       tex(brsgexpminb-h.vf) = %{tl_version}, tex(brsgexpminb-v.vf) = %{tl_version}
Provides:       tex(brsgexpminbn-h.vf) = %{tl_version}, tex(brsgexpminbn-v.vf) = %{tl_version}
Provides:       tex(brsgexpminl-h.vf) = %{tl_version}, tex(brsgexpminl-v.vf) = %{tl_version}
Provides:       tex(brsgexpminln-h.vf) = %{tl_version}, tex(brsgexpminln-v.vf) = %{tl_version}
Provides:       tex(brsgexpminr-h.vf) = %{tl_version}, tex(brsgexpminr-v.vf) = %{tl_version}
Provides:       tex(brsgexpminrn-h.vf) = %{tl_version}, tex(brsgexpminrn-v.vf) = %{tl_version}
Provides:       tex(brsgnmlgothb-h.vf) = %{tl_version}, tex(brsgnmlgothb-v.vf) = %{tl_version}
Provides:       tex(brsgnmlgothbn-h.vf) = %{tl_version}, tex(brsgnmlgothbn-v.vf) = %{tl_version}
Provides:       tex(brsgnmlgotheb-h.vf) = %{tl_version}, tex(brsgnmlgotheb-v.vf) = %{tl_version}
Provides:       tex(brsgnmlgothebn-h.vf) = %{tl_version}
Provides:       tex(brsgnmlgothebn-v.vf) = %{tl_version}
Provides:       tex(brsgnmlgothr-h.vf) = %{tl_version}, tex(brsgnmlgothr-v.vf) = %{tl_version}
Provides:       tex(brsgnmlgothrn-h.vf) = %{tl_version}, tex(brsgnmlgothrn-v.vf) = %{tl_version}
Provides:       tex(brsgnmlmgothr-h.vf) = %{tl_version}, tex(brsgnmlmgothr-v.vf) = %{tl_version}
Provides:       tex(brsgnmlmgothrn-h.vf) = %{tl_version}
Provides:       tex(brsgnmlmgothrn-v.vf) = %{tl_version}
Provides:       tex(brsgnmlminb-h.vf) = %{tl_version}, tex(brsgnmlminb-v.vf) = %{tl_version}
Provides:       tex(brsgnmlminbn-h.vf) = %{tl_version}, tex(brsgnmlminbn-v.vf) = %{tl_version}
Provides:       tex(brsgnmlminl-h.vf) = %{tl_version}, tex(brsgnmlminl-v.vf) = %{tl_version}
Provides:       tex(brsgnmlminln-h.vf) = %{tl_version}, tex(brsgnmlminln-v.vf) = %{tl_version}
Provides:       tex(brsgnmlminr-h.vf) = %{tl_version}, tex(brsgnmlminr-v.vf) = %{tl_version}
Provides:       tex(brsgnmlminrn-h.vf) = %{tl_version}, tex(brsgnmlminrn-v.vf) = %{tl_version}
Provides:       tex(cidcgr0-h.vf) = %{tl_version}, tex(cidcgr0-v.vf) = %{tl_version}
Provides:       tex(cidcgr1-h.vf) = %{tl_version}, tex(cidcgr1-v.vf) = %{tl_version}
Provides:       tex(cidcgr2-h.vf) = %{tl_version}, tex(cidcgr2-v.vf) = %{tl_version}
Provides:       tex(cidcgr3-h.vf) = %{tl_version}, tex(cidcgr3-v.vf) = %{tl_version}
Provides:       tex(cidcgr4-h.vf) = %{tl_version}, tex(cidcgr4-v.vf) = %{tl_version}
Provides:       tex(cidcgr5-h.vf) = %{tl_version}, tex(cidcgr5-v.vf) = %{tl_version}
Provides:       tex(cidcgr6-h.vf) = %{tl_version}, tex(cidcgr6-v.vf) = %{tl_version}
Provides:       tex(cidcgr7-h.vf) = %{tl_version}, tex(cidcgr7-v.vf) = %{tl_version}
Provides:       tex(cidcmr0-h.vf) = %{tl_version}, tex(cidcmr0-v.vf) = %{tl_version}
Provides:       tex(cidcmr1-h.vf) = %{tl_version}, tex(cidcmr1-v.vf) = %{tl_version}
Provides:       tex(cidcmr2-h.vf) = %{tl_version}, tex(cidcmr2-v.vf) = %{tl_version}
Provides:       tex(cidcmr3-h.vf) = %{tl_version}, tex(cidcmr3-v.vf) = %{tl_version}
Provides:       tex(cidcmr4-h.vf) = %{tl_version}, tex(cidcmr4-v.vf) = %{tl_version}
Provides:       tex(cidcmr5-h.vf) = %{tl_version}, tex(cidcmr5-v.vf) = %{tl_version}
Provides:       tex(cidcmr6-h.vf) = %{tl_version}, tex(cidcmr6-v.vf) = %{tl_version}
Provides:       tex(cidcmr7-h.vf) = %{tl_version}, tex(cidcmr7-v.vf) = %{tl_version}
Provides:       tex(cidjgb0-h.vf) = %{tl_version}, tex(cidjgb0-v.vf) = %{tl_version}
Provides:       tex(cidjgb1-h.vf) = %{tl_version}, tex(cidjgb1-v.vf) = %{tl_version}
Provides:       tex(cidjgb2-h.vf) = %{tl_version}, tex(cidjgb2-v.vf) = %{tl_version}
Provides:       tex(cidjgb3-h.vf) = %{tl_version}, tex(cidjgb3-v.vf) = %{tl_version}
Provides:       tex(cidjgb4-h.vf) = %{tl_version}, tex(cidjgb4-v.vf) = %{tl_version}
Provides:       tex(cidjgb5-h.vf) = %{tl_version}, tex(cidjgb5-v.vf) = %{tl_version}
Provides:       tex(cidjge0-h.vf) = %{tl_version}, tex(cidjge0-v.vf) = %{tl_version}
Provides:       tex(cidjge1-h.vf) = %{tl_version}, tex(cidjge1-v.vf) = %{tl_version}
Provides:       tex(cidjge2-h.vf) = %{tl_version}, tex(cidjge2-v.vf) = %{tl_version}
Provides:       tex(cidjge3-h.vf) = %{tl_version}, tex(cidjge3-v.vf) = %{tl_version}
Provides:       tex(cidjge4-h.vf) = %{tl_version}, tex(cidjge4-v.vf) = %{tl_version}
Provides:       tex(cidjge5-h.vf) = %{tl_version}, tex(cidjge5-v.vf) = %{tl_version}
Provides:       tex(cidjgr0-h.vf) = %{tl_version}, tex(cidjgr0-v.vf) = %{tl_version}
Provides:       tex(cidjgr1-h.vf) = %{tl_version}, tex(cidjgr1-v.vf) = %{tl_version}
Provides:       tex(cidjgr2-h.vf) = %{tl_version}, tex(cidjgr2-v.vf) = %{tl_version}
Provides:       tex(cidjgr3-h.vf) = %{tl_version}, tex(cidjgr3-v.vf) = %{tl_version}
Provides:       tex(cidjgr4-h.vf) = %{tl_version}, tex(cidjgr4-v.vf) = %{tl_version}
Provides:       tex(cidjgr5-h.vf) = %{tl_version}, tex(cidjgr5-v.vf) = %{tl_version}
Provides:       tex(cidjmb0-h.vf) = %{tl_version}, tex(cidjmb0-v.vf) = %{tl_version}
Provides:       tex(cidjmb1-h.vf) = %{tl_version}, tex(cidjmb1-v.vf) = %{tl_version}
Provides:       tex(cidjmb2-h.vf) = %{tl_version}, tex(cidjmb2-v.vf) = %{tl_version}
Provides:       tex(cidjmb3-h.vf) = %{tl_version}, tex(cidjmb3-v.vf) = %{tl_version}
Provides:       tex(cidjmb4-h.vf) = %{tl_version}, tex(cidjmb4-v.vf) = %{tl_version}
Provides:       tex(cidjmb5-h.vf) = %{tl_version}, tex(cidjmb5-v.vf) = %{tl_version}
Provides:       tex(cidjmgr0-h.vf) = %{tl_version}, tex(cidjmgr0-v.vf) = %{tl_version}
Provides:       tex(cidjmgr1-h.vf) = %{tl_version}, tex(cidjmgr1-v.vf) = %{tl_version}
Provides:       tex(cidjmgr2-h.vf) = %{tl_version}, tex(cidjmgr2-v.vf) = %{tl_version}
Provides:       tex(cidjmgr3-h.vf) = %{tl_version}, tex(cidjmgr3-v.vf) = %{tl_version}
Provides:       tex(cidjmgr4-h.vf) = %{tl_version}, tex(cidjmgr4-v.vf) = %{tl_version}
Provides:       tex(cidjmgr5-h.vf) = %{tl_version}, tex(cidjmgr5-v.vf) = %{tl_version}
Provides:       tex(cidjml0-h.vf) = %{tl_version}, tex(cidjml0-v.vf) = %{tl_version}
Provides:       tex(cidjml1-h.vf) = %{tl_version}, tex(cidjml1-v.vf) = %{tl_version}
Provides:       tex(cidjml2-h.vf) = %{tl_version}, tex(cidjml2-v.vf) = %{tl_version}
Provides:       tex(cidjml3-h.vf) = %{tl_version}, tex(cidjml3-v.vf) = %{tl_version}
Provides:       tex(cidjml4-h.vf) = %{tl_version}, tex(cidjml4-v.vf) = %{tl_version}
Provides:       tex(cidjml5-h.vf) = %{tl_version}, tex(cidjml5-v.vf) = %{tl_version}
Provides:       tex(cidjmr0-h.vf) = %{tl_version}, tex(cidjmr0-v.vf) = %{tl_version}
Provides:       tex(cidjmr1-h.vf) = %{tl_version}, tex(cidjmr1-v.vf) = %{tl_version}
Provides:       tex(cidjmr2-h.vf) = %{tl_version}, tex(cidjmr2-v.vf) = %{tl_version}
Provides:       tex(cidjmr3-h.vf) = %{tl_version}, tex(cidjmr3-v.vf) = %{tl_version}
Provides:       tex(cidjmr4-h.vf) = %{tl_version}, tex(cidjmr4-v.vf) = %{tl_version}
Provides:       tex(cidjmr5-h.vf) = %{tl_version}, tex(cidjmr5-v.vf) = %{tl_version}
Provides:       tex(cidkgr0-h.vf) = %{tl_version}, tex(cidkgr0-v.vf) = %{tl_version}
Provides:       tex(cidkgr1-h.vf) = %{tl_version}, tex(cidkgr1-v.vf) = %{tl_version}
Provides:       tex(cidkgr2-h.vf) = %{tl_version}, tex(cidkgr2-v.vf) = %{tl_version}
Provides:       tex(cidkgr3-h.vf) = %{tl_version}, tex(cidkgr3-v.vf) = %{tl_version}
Provides:       tex(cidkgr4-h.vf) = %{tl_version}, tex(cidkgr4-v.vf) = %{tl_version}
Provides:       tex(cidkmr0-h.vf) = %{tl_version}, tex(cidkmr0-v.vf) = %{tl_version}
Provides:       tex(cidkmr1-h.vf) = %{tl_version}, tex(cidkmr1-v.vf) = %{tl_version}
Provides:       tex(cidkmr2-h.vf) = %{tl_version}, tex(cidkmr2-v.vf) = %{tl_version}
Provides:       tex(cidkmr3-h.vf) = %{tl_version}, tex(cidkmr3-v.vf) = %{tl_version}
Provides:       tex(cidkmr4-h.vf) = %{tl_version}, tex(cidkmr4-v.vf) = %{tl_version}
Provides:       tex(cidtgr0-h.vf) = %{tl_version}, tex(cidtgr0-v.vf) = %{tl_version}
Provides:       tex(cidtgr1-h.vf) = %{tl_version}, tex(cidtgr1-v.vf) = %{tl_version}
Provides:       tex(cidtgr2-h.vf) = %{tl_version}, tex(cidtgr2-v.vf) = %{tl_version}
Provides:       tex(cidtgr3-h.vf) = %{tl_version}, tex(cidtgr3-v.vf) = %{tl_version}
Provides:       tex(cidtgr4-h.vf) = %{tl_version}, tex(cidtgr4-v.vf) = %{tl_version}
Provides:       tex(cidtmr0-h.vf) = %{tl_version}, tex(cidtmr0-v.vf) = %{tl_version}
Provides:       tex(cidtmr1-h.vf) = %{tl_version}, tex(cidtmr1-v.vf) = %{tl_version}
Provides:       tex(cidtmr2-h.vf) = %{tl_version}, tex(cidtmr2-v.vf) = %{tl_version}
Provides:       tex(cidtmr3-h.vf) = %{tl_version}, tex(cidtmr3-v.vf) = %{tl_version}
Provides:       tex(cidtmr4-h.vf) = %{tl_version}, tex(cidtmr4-v.vf) = %{tl_version}
Provides:       tex(expgothb-h.vf) = %{tl_version}, tex(expgothb-v.vf) = %{tl_version}
Provides:       tex(expgothbn-h.vf) = %{tl_version}, tex(expgothbn-v.vf) = %{tl_version}
Provides:       tex(expgotheb-h.vf) = %{tl_version}, tex(expgotheb-v.vf) = %{tl_version}
Provides:       tex(expgothebn-h.vf) = %{tl_version}, tex(expgothebn-v.vf) = %{tl_version}
Provides:       tex(expgothr-h.vf) = %{tl_version}, tex(expgothr-v.vf) = %{tl_version}
Provides:       tex(expgothrn-h.vf) = %{tl_version}, tex(expgothrn-v.vf) = %{tl_version}
Provides:       tex(expmgothr-h.vf) = %{tl_version}, tex(expmgothr-v.vf) = %{tl_version}
Provides:       tex(expmgothrn-h.vf) = %{tl_version}, tex(expmgothrn-v.vf) = %{tl_version}
Provides:       tex(expminb-h.vf) = %{tl_version}, tex(expminb-v.vf) = %{tl_version}
Provides:       tex(expminbn-h.vf) = %{tl_version}, tex(expminbn-v.vf) = %{tl_version}
Provides:       tex(expminl-h.vf) = %{tl_version}, tex(expminl-v.vf) = %{tl_version}
Provides:       tex(expminln-h.vf) = %{tl_version}, tex(expminln-v.vf) = %{tl_version}
Provides:       tex(expminr-h.vf) = %{tl_version}, tex(expminr-v.vf) = %{tl_version}
Provides:       tex(expminrn-h.vf) = %{tl_version}, tex(expminrn-v.vf) = %{tl_version}
Provides:       tex(nmlgothb-h.vf) = %{tl_version}, tex(nmlgothb-v.vf) = %{tl_version}
Provides:       tex(nmlgothbn-h.vf) = %{tl_version}, tex(nmlgothbn-v.vf) = %{tl_version}
Provides:       tex(nmlgotheb-h.vf) = %{tl_version}, tex(nmlgotheb-v.vf) = %{tl_version}
Provides:       tex(nmlgothebn-h.vf) = %{tl_version}, tex(nmlgothebn-v.vf) = %{tl_version}
Provides:       tex(nmlgothr-h.vf) = %{tl_version}, tex(nmlgothr-v.vf) = %{tl_version}
Provides:       tex(nmlgothrn-h.vf) = %{tl_version}, tex(nmlgothrn-v.vf) = %{tl_version}
Provides:       tex(nmlmgothr-h.vf) = %{tl_version}, tex(nmlmgothr-v.vf) = %{tl_version}
Provides:       tex(nmlmgothrn-h.vf) = %{tl_version}, tex(nmlmgothrn-v.vf) = %{tl_version}
Provides:       tex(nmlminb-h.vf) = %{tl_version}, tex(nmlminb-v.vf) = %{tl_version}
Provides:       tex(nmlminbn-h.vf) = %{tl_version}, tex(nmlminbn-v.vf) = %{tl_version}
Provides:       tex(nmlminl-h.vf) = %{tl_version}, tex(nmlminl-v.vf) = %{tl_version}
Provides:       tex(nmlminln-h.vf) = %{tl_version}, tex(nmlminln-v.vf) = %{tl_version}
Provides:       tex(nmlminr-h.vf) = %{tl_version}, tex(nmlminr-v.vf) = %{tl_version}
Provides:       tex(nmlminrn-h.vf) = %{tl_version}, tex(nmlminrn-v.vf) = %{tl_version}
Provides:       tex(phirakakuw3-h.vf) = %{tl_version}, tex(phirakakuw3-v.vf) = %{tl_version}
Provides:       tex(phirakakuw6-h.vf) = %{tl_version}, tex(phirakakuw6-v.vf) = %{tl_version}
Provides:       tex(phiramaruw4-h.vf) = %{tl_version}, tex(phiramaruw4-v.vf) = %{tl_version}
Provides:       tex(phiraminw3-h.vf) = %{tl_version}, tex(phiraminw3-v.vf) = %{tl_version}
Provides:       tex(phiraminw6-h.vf) = %{tl_version}, tex(phiraminw6-v.vf) = %{tl_version}
Provides:       tex(rubygothb-h.vf) = %{tl_version}, tex(rubygothb-v.vf) = %{tl_version}
Provides:       tex(rubygotheb-h.vf) = %{tl_version}, tex(rubygotheb-v.vf) = %{tl_version}
Provides:       tex(rubygothr-h.vf) = %{tl_version}, tex(rubygothr-v.vf) = %{tl_version}
Provides:       tex(rubymgothr-h.vf) = %{tl_version}, tex(rubymgothr-v.vf) = %{tl_version}
Provides:       tex(rubyminb-h.vf) = %{tl_version}, tex(rubyminb-v.vf) = %{tl_version}
Provides:       tex(rubyminl-h.vf) = %{tl_version}, tex(rubyminl-v.vf) = %{tl_version}
Provides:       tex(rubyminr-h.vf) = %{tl_version}, tex(rubyminr-v.vf) = %{tl_version}
Provides:       tex(utfcgr0-h.vf) = %{tl_version}, tex(utfcgr0-v.vf) = %{tl_version}
Provides:       tex(utfcgr1-h.vf) = %{tl_version}, tex(utfcgr1-v.vf) = %{tl_version}
Provides:       tex(utfcgr2-h.vf) = %{tl_version}, tex(utfcgr2-v.vf) = %{tl_version}
Provides:       tex(utfcgr3-h.vf) = %{tl_version}, tex(utfcgr3-v.vf) = %{tl_version}
Provides:       tex(utfcgr4-h.vf) = %{tl_version}, tex(utfcgr4-v.vf) = %{tl_version}
Provides:       tex(utfcgr5-h.vf) = %{tl_version}, tex(utfcgr5-v.vf) = %{tl_version}
Provides:       tex(utfcgr6-h.vf) = %{tl_version}, tex(utfcgr6-v.vf) = %{tl_version}
Provides:       tex(utfcgr7-h.vf) = %{tl_version}, tex(utfcgr7-v.vf) = %{tl_version}
Provides:       tex(utfcgr8-h.vf) = %{tl_version}, tex(utfcgr8-v.vf) = %{tl_version}
Provides:       tex(utfcgr9-h.vf) = %{tl_version}, tex(utfcgr9-v.vf) = %{tl_version}
Provides:       tex(utfcgra-h.vf) = %{tl_version}, tex(utfcgra-v.vf) = %{tl_version}
Provides:       tex(utfcgrb-h.vf) = %{tl_version}, tex(utfcgrb-v.vf) = %{tl_version}
Provides:       tex(utfcgrc-h.vf) = %{tl_version}, tex(utfcgrc-v.vf) = %{tl_version}
Provides:       tex(utfcgrd-h.vf) = %{tl_version}, tex(utfcgrd-v.vf) = %{tl_version}
Provides:       tex(utfcgre-h.vf) = %{tl_version}, tex(utfcgre-v.vf) = %{tl_version}
Provides:       tex(utfcgrf-h.vf) = %{tl_version}, tex(utfcgrf-v.vf) = %{tl_version}
Provides:       tex(utfcmr0-h.vf) = %{tl_version}, tex(utfcmr0-v.vf) = %{tl_version}
Provides:       tex(utfcmr1-h.vf) = %{tl_version}, tex(utfcmr1-v.vf) = %{tl_version}
Provides:       tex(utfcmr2-h.vf) = %{tl_version}, tex(utfcmr2-v.vf) = %{tl_version}
Provides:       tex(utfcmr3-h.vf) = %{tl_version}, tex(utfcmr3-v.vf) = %{tl_version}
Provides:       tex(utfcmr4-h.vf) = %{tl_version}, tex(utfcmr4-v.vf) = %{tl_version}
Provides:       tex(utfcmr5-h.vf) = %{tl_version}, tex(utfcmr5-v.vf) = %{tl_version}
Provides:       tex(utfcmr6-h.vf) = %{tl_version}, tex(utfcmr6-v.vf) = %{tl_version}
Provides:       tex(utfcmr7-h.vf) = %{tl_version}, tex(utfcmr7-v.vf) = %{tl_version}
Provides:       tex(utfcmr8-h.vf) = %{tl_version}, tex(utfcmr8-v.vf) = %{tl_version}
Provides:       tex(utfcmr9-h.vf) = %{tl_version}, tex(utfcmr9-v.vf) = %{tl_version}
Provides:       tex(utfcmra-h.vf) = %{tl_version}, tex(utfcmra-v.vf) = %{tl_version}
Provides:       tex(utfcmrb-h.vf) = %{tl_version}, tex(utfcmrb-v.vf) = %{tl_version}
Provides:       tex(utfcmrc-h.vf) = %{tl_version}, tex(utfcmrc-v.vf) = %{tl_version}
Provides:       tex(utfcmrd-h.vf) = %{tl_version}, tex(utfcmrd-v.vf) = %{tl_version}
Provides:       tex(utfcmre-h.vf) = %{tl_version}, tex(utfcmre-v.vf) = %{tl_version}
Provides:       tex(utfcmrf-h.vf) = %{tl_version}, tex(utfcmrf-v.vf) = %{tl_version}
Provides:       tex(utfgr0-h.vf) = %{tl_version}, tex(utfgr0-v.vf) = %{tl_version}
Provides:       tex(utfgr1-h.vf) = %{tl_version}, tex(utfgr1-v.vf) = %{tl_version}
Provides:       tex(utfgr2-h.vf) = %{tl_version}, tex(utfgr2-v.vf) = %{tl_version}
Provides:       tex(utfgr3-h.vf) = %{tl_version}, tex(utfgr3-v.vf) = %{tl_version}
Provides:       tex(utfgr4-h.vf) = %{tl_version}, tex(utfgr4-v.vf) = %{tl_version}
Provides:       tex(utfgr5-h.vf) = %{tl_version}, tex(utfgr5-v.vf) = %{tl_version}
Provides:       tex(utfgr6-h.vf) = %{tl_version}, tex(utfgr6-v.vf) = %{tl_version}
Provides:       tex(utfgr7-h.vf) = %{tl_version}, tex(utfgr7-v.vf) = %{tl_version}
Provides:       tex(utfgr8-h.vf) = %{tl_version}, tex(utfgr8-v.vf) = %{tl_version}
Provides:       tex(utfgr9-h.vf) = %{tl_version}, tex(utfgr9-v.vf) = %{tl_version}
Provides:       tex(utfgra-h.vf) = %{tl_version}, tex(utfgra-v.vf) = %{tl_version}
Provides:       tex(utfgrb-h.vf) = %{tl_version}, tex(utfgrb-v.vf) = %{tl_version}
Provides:       tex(utfgrc-h.vf) = %{tl_version}, tex(utfgrc-v.vf) = %{tl_version}
Provides:       tex(utfgrd-h.vf) = %{tl_version}, tex(utfgrd-v.vf) = %{tl_version}
Provides:       tex(utfgre-h.vf) = %{tl_version}, tex(utfgre-v.vf) = %{tl_version}
Provides:       tex(utfgrf-h.vf) = %{tl_version}, tex(utfgrf-v.vf) = %{tl_version}
Provides:       tex(utfjgb0-h.vf) = %{tl_version}, tex(utfjgb0-v.vf) = %{tl_version}
Provides:       tex(utfjgb1-h.vf) = %{tl_version}, tex(utfjgb1-v.vf) = %{tl_version}
Provides:       tex(utfjgb2-h.vf) = %{tl_version}, tex(utfjgb2-v.vf) = %{tl_version}
Provides:       tex(utfjgb3-h.vf) = %{tl_version}, tex(utfjgb3-v.vf) = %{tl_version}
Provides:       tex(utfjgb4-h.vf) = %{tl_version}, tex(utfjgb4-v.vf) = %{tl_version}
Provides:       tex(utfjgb5-h.vf) = %{tl_version}, tex(utfjgb5-v.vf) = %{tl_version}
Provides:       tex(utfjgb6-h.vf) = %{tl_version}, tex(utfjgb6-v.vf) = %{tl_version}
Provides:       tex(utfjgb7-h.vf) = %{tl_version}, tex(utfjgb7-v.vf) = %{tl_version}
Provides:       tex(utfjgb8-h.vf) = %{tl_version}, tex(utfjgb8-v.vf) = %{tl_version}
Provides:       tex(utfjgb9-h.vf) = %{tl_version}, tex(utfjgb9-v.vf) = %{tl_version}
Provides:       tex(utfjgba-h.vf) = %{tl_version}, tex(utfjgba-v.vf) = %{tl_version}
Provides:       tex(utfjgbb-h.vf) = %{tl_version}, tex(utfjgbb-v.vf) = %{tl_version}
Provides:       tex(utfjgbc-h.vf) = %{tl_version}, tex(utfjgbc-v.vf) = %{tl_version}
Provides:       tex(utfjgbd-h.vf) = %{tl_version}, tex(utfjgbd-v.vf) = %{tl_version}
Provides:       tex(utfjgbe-h.vf) = %{tl_version}, tex(utfjgbe-v.vf) = %{tl_version}
Provides:       tex(utfjgbf-h.vf) = %{tl_version}, tex(utfjgbf-v.vf) = %{tl_version}
Provides:       tex(utfjgbn0-h.vf) = %{tl_version}, tex(utfjgbn0-v.vf) = %{tl_version}
Provides:       tex(utfjgbn1-h.vf) = %{tl_version}, tex(utfjgbn1-v.vf) = %{tl_version}
Provides:       tex(utfjgbn2-h.vf) = %{tl_version}, tex(utfjgbn2-v.vf) = %{tl_version}
Provides:       tex(utfjgbn3-h.vf) = %{tl_version}, tex(utfjgbn3-v.vf) = %{tl_version}
Provides:       tex(utfjgbn4-h.vf) = %{tl_version}, tex(utfjgbn4-v.vf) = %{tl_version}
Provides:       tex(utfjgbn5-h.vf) = %{tl_version}, tex(utfjgbn5-v.vf) = %{tl_version}
Provides:       tex(utfjgbn6-h.vf) = %{tl_version}, tex(utfjgbn6-v.vf) = %{tl_version}
Provides:       tex(utfjgbn7-h.vf) = %{tl_version}, tex(utfjgbn7-v.vf) = %{tl_version}
Provides:       tex(utfjgbn8-h.vf) = %{tl_version}, tex(utfjgbn8-v.vf) = %{tl_version}
Provides:       tex(utfjgbn9-h.vf) = %{tl_version}, tex(utfjgbn9-v.vf) = %{tl_version}
Provides:       tex(utfjgbna-h.vf) = %{tl_version}, tex(utfjgbna-v.vf) = %{tl_version}
Provides:       tex(utfjgbnb-h.vf) = %{tl_version}, tex(utfjgbnb-v.vf) = %{tl_version}
Provides:       tex(utfjgbnc-h.vf) = %{tl_version}, tex(utfjgbnc-v.vf) = %{tl_version}
Provides:       tex(utfjgbnd-h.vf) = %{tl_version}, tex(utfjgbnd-v.vf) = %{tl_version}
Provides:       tex(utfjgbne-h.vf) = %{tl_version}, tex(utfjgbne-v.vf) = %{tl_version}
Provides:       tex(utfjgbnf-h.vf) = %{tl_version}, tex(utfjgbnf-v.vf) = %{tl_version}
Provides:       tex(utfjge0-h.vf) = %{tl_version}, tex(utfjge0-v.vf) = %{tl_version}
Provides:       tex(utfjge1-h.vf) = %{tl_version}, tex(utfjge1-v.vf) = %{tl_version}
Provides:       tex(utfjge2-h.vf) = %{tl_version}, tex(utfjge2-v.vf) = %{tl_version}
Provides:       tex(utfjge3-h.vf) = %{tl_version}, tex(utfjge3-v.vf) = %{tl_version}
Provides:       tex(utfjge4-h.vf) = %{tl_version}, tex(utfjge4-v.vf) = %{tl_version}
Provides:       tex(utfjge5-h.vf) = %{tl_version}, tex(utfjge5-v.vf) = %{tl_version}
Provides:       tex(utfjge6-h.vf) = %{tl_version}, tex(utfjge6-v.vf) = %{tl_version}
Provides:       tex(utfjge7-h.vf) = %{tl_version}, tex(utfjge7-v.vf) = %{tl_version}
Provides:       tex(utfjge8-h.vf) = %{tl_version}, tex(utfjge8-v.vf) = %{tl_version}
Provides:       tex(utfjge9-h.vf) = %{tl_version}, tex(utfjge9-v.vf) = %{tl_version}
Provides:       tex(utfjgea-h.vf) = %{tl_version}, tex(utfjgea-v.vf) = %{tl_version}
Provides:       tex(utfjgeb-h.vf) = %{tl_version}, tex(utfjgeb-v.vf) = %{tl_version}
Provides:       tex(utfjgec-h.vf) = %{tl_version}, tex(utfjgec-v.vf) = %{tl_version}
Provides:       tex(utfjged-h.vf) = %{tl_version}, tex(utfjged-v.vf) = %{tl_version}
Provides:       tex(utfjgee-h.vf) = %{tl_version}, tex(utfjgee-v.vf) = %{tl_version}
Provides:       tex(utfjgef-h.vf) = %{tl_version}, tex(utfjgef-v.vf) = %{tl_version}
Provides:       tex(utfjgen0-h.vf) = %{tl_version}, tex(utfjgen0-v.vf) = %{tl_version}
Provides:       tex(utfjgen1-h.vf) = %{tl_version}, tex(utfjgen1-v.vf) = %{tl_version}
Provides:       tex(utfjgen2-h.vf) = %{tl_version}, tex(utfjgen2-v.vf) = %{tl_version}
Provides:       tex(utfjgen3-h.vf) = %{tl_version}, tex(utfjgen3-v.vf) = %{tl_version}
Provides:       tex(utfjgen4-h.vf) = %{tl_version}, tex(utfjgen4-v.vf) = %{tl_version}
Provides:       tex(utfjgen5-h.vf) = %{tl_version}, tex(utfjgen5-v.vf) = %{tl_version}
Provides:       tex(utfjgen6-h.vf) = %{tl_version}, tex(utfjgen6-v.vf) = %{tl_version}
Provides:       tex(utfjgen7-h.vf) = %{tl_version}, tex(utfjgen7-v.vf) = %{tl_version}
Provides:       tex(utfjgen8-h.vf) = %{tl_version}, tex(utfjgen8-v.vf) = %{tl_version}
Provides:       tex(utfjgen9-h.vf) = %{tl_version}, tex(utfjgen9-v.vf) = %{tl_version}
Provides:       tex(utfjgena-h.vf) = %{tl_version}, tex(utfjgena-v.vf) = %{tl_version}
Provides:       tex(utfjgenb-h.vf) = %{tl_version}, tex(utfjgenb-v.vf) = %{tl_version}
Provides:       tex(utfjgenc-h.vf) = %{tl_version}, tex(utfjgenc-v.vf) = %{tl_version}
Provides:       tex(utfjgend-h.vf) = %{tl_version}, tex(utfjgend-v.vf) = %{tl_version}
Provides:       tex(utfjgene-h.vf) = %{tl_version}, tex(utfjgene-v.vf) = %{tl_version}
Provides:       tex(utfjgenf-h.vf) = %{tl_version}, tex(utfjgenf-v.vf) = %{tl_version}
Provides:       tex(utfjgr0-h.vf) = %{tl_version}, tex(utfjgr0-v.vf) = %{tl_version}
Provides:       tex(utfjgr1-h.vf) = %{tl_version}, tex(utfjgr1-v.vf) = %{tl_version}
Provides:       tex(utfjgr2-h.vf) = %{tl_version}, tex(utfjgr2-v.vf) = %{tl_version}
Provides:       tex(utfjgr3-h.vf) = %{tl_version}, tex(utfjgr3-v.vf) = %{tl_version}
Provides:       tex(utfjgr4-h.vf) = %{tl_version}, tex(utfjgr4-v.vf) = %{tl_version}
Provides:       tex(utfjgr5-h.vf) = %{tl_version}, tex(utfjgr5-v.vf) = %{tl_version}
Provides:       tex(utfjgr6-h.vf) = %{tl_version}, tex(utfjgr6-v.vf) = %{tl_version}
Provides:       tex(utfjgr7-h.vf) = %{tl_version}, tex(utfjgr7-v.vf) = %{tl_version}
Provides:       tex(utfjgr8-h.vf) = %{tl_version}, tex(utfjgr8-v.vf) = %{tl_version}
Provides:       tex(utfjgr9-h.vf) = %{tl_version}, tex(utfjgr9-v.vf) = %{tl_version}
Provides:       tex(utfjgra-h.vf) = %{tl_version}, tex(utfjgra-v.vf) = %{tl_version}
Provides:       tex(utfjgrb-h.vf) = %{tl_version}, tex(utfjgrb-v.vf) = %{tl_version}
Provides:       tex(utfjgrc-h.vf) = %{tl_version}, tex(utfjgrc-v.vf) = %{tl_version}
Provides:       tex(utfjgrd-h.vf) = %{tl_version}, tex(utfjgrd-v.vf) = %{tl_version}
Provides:       tex(utfjgre-h.vf) = %{tl_version}, tex(utfjgre-v.vf) = %{tl_version}
Provides:       tex(utfjgrf-h.vf) = %{tl_version}, tex(utfjgrf-v.vf) = %{tl_version}
Provides:       tex(utfjgrn0-h.vf) = %{tl_version}, tex(utfjgrn0-v.vf) = %{tl_version}
Provides:       tex(utfjgrn1-h.vf) = %{tl_version}, tex(utfjgrn1-v.vf) = %{tl_version}
Provides:       tex(utfjgrn2-h.vf) = %{tl_version}, tex(utfjgrn2-v.vf) = %{tl_version}
Provides:       tex(utfjgrn3-h.vf) = %{tl_version}, tex(utfjgrn3-v.vf) = %{tl_version}
Provides:       tex(utfjgrn4-h.vf) = %{tl_version}, tex(utfjgrn4-v.vf) = %{tl_version}
Provides:       tex(utfjgrn5-h.vf) = %{tl_version}, tex(utfjgrn5-v.vf) = %{tl_version}
Provides:       tex(utfjgrn6-h.vf) = %{tl_version}, tex(utfjgrn6-v.vf) = %{tl_version}
Provides:       tex(utfjgrn7-h.vf) = %{tl_version}, tex(utfjgrn7-v.vf) = %{tl_version}
Provides:       tex(utfjgrn8-h.vf) = %{tl_version}, tex(utfjgrn8-v.vf) = %{tl_version}
Provides:       tex(utfjgrn9-h.vf) = %{tl_version}, tex(utfjgrn9-v.vf) = %{tl_version}
Provides:       tex(utfjgrna-h.vf) = %{tl_version}, tex(utfjgrna-v.vf) = %{tl_version}
Provides:       tex(utfjgrnb-h.vf) = %{tl_version}, tex(utfjgrnb-v.vf) = %{tl_version}
Provides:       tex(utfjgrnc-h.vf) = %{tl_version}, tex(utfjgrnc-v.vf) = %{tl_version}
Provides:       tex(utfjgrnd-h.vf) = %{tl_version}, tex(utfjgrnd-v.vf) = %{tl_version}
Provides:       tex(utfjgrne-h.vf) = %{tl_version}, tex(utfjgrne-v.vf) = %{tl_version}
Provides:       tex(utfjgrnf-h.vf) = %{tl_version}, tex(utfjgrnf-v.vf) = %{tl_version}
Provides:       tex(utfjmb0-h.vf) = %{tl_version}, tex(utfjmb0-v.vf) = %{tl_version}
Provides:       tex(utfjmb1-h.vf) = %{tl_version}, tex(utfjmb1-v.vf) = %{tl_version}
Provides:       tex(utfjmb2-h.vf) = %{tl_version}, tex(utfjmb2-v.vf) = %{tl_version}
Provides:       tex(utfjmb3-h.vf) = %{tl_version}, tex(utfjmb3-v.vf) = %{tl_version}
Provides:       tex(utfjmb4-h.vf) = %{tl_version}, tex(utfjmb4-v.vf) = %{tl_version}
Provides:       tex(utfjmb5-h.vf) = %{tl_version}, tex(utfjmb5-v.vf) = %{tl_version}
Provides:       tex(utfjmb6-h.vf) = %{tl_version}, tex(utfjmb6-v.vf) = %{tl_version}
Provides:       tex(utfjmb7-h.vf) = %{tl_version}, tex(utfjmb7-v.vf) = %{tl_version}
Provides:       tex(utfjmb8-h.vf) = %{tl_version}, tex(utfjmb8-v.vf) = %{tl_version}
Provides:       tex(utfjmb9-h.vf) = %{tl_version}, tex(utfjmb9-v.vf) = %{tl_version}
Provides:       tex(utfjmba-h.vf) = %{tl_version}, tex(utfjmba-v.vf) = %{tl_version}
Provides:       tex(utfjmbb-h.vf) = %{tl_version}, tex(utfjmbb-v.vf) = %{tl_version}
Provides:       tex(utfjmbc-h.vf) = %{tl_version}, tex(utfjmbc-v.vf) = %{tl_version}
Provides:       tex(utfjmbd-h.vf) = %{tl_version}, tex(utfjmbd-v.vf) = %{tl_version}
Provides:       tex(utfjmbe-h.vf) = %{tl_version}, tex(utfjmbe-v.vf) = %{tl_version}
Provides:       tex(utfjmbf-h.vf) = %{tl_version}, tex(utfjmbf-v.vf) = %{tl_version}
Provides:       tex(utfjmbn0-h.vf) = %{tl_version}, tex(utfjmbn0-v.vf) = %{tl_version}
Provides:       tex(utfjmbn1-h.vf) = %{tl_version}, tex(utfjmbn1-v.vf) = %{tl_version}
Provides:       tex(utfjmbn2-h.vf) = %{tl_version}, tex(utfjmbn2-v.vf) = %{tl_version}
Provides:       tex(utfjmbn3-h.vf) = %{tl_version}, tex(utfjmbn3-v.vf) = %{tl_version}
Provides:       tex(utfjmbn4-h.vf) = %{tl_version}, tex(utfjmbn4-v.vf) = %{tl_version}
Provides:       tex(utfjmbn5-h.vf) = %{tl_version}, tex(utfjmbn5-v.vf) = %{tl_version}
Provides:       tex(utfjmbn6-h.vf) = %{tl_version}, tex(utfjmbn6-v.vf) = %{tl_version}
Provides:       tex(utfjmbn7-h.vf) = %{tl_version}, tex(utfjmbn7-v.vf) = %{tl_version}
Provides:       tex(utfjmbn8-h.vf) = %{tl_version}, tex(utfjmbn8-v.vf) = %{tl_version}
Provides:       tex(utfjmbn9-h.vf) = %{tl_version}, tex(utfjmbn9-v.vf) = %{tl_version}
Provides:       tex(utfjmbna-h.vf) = %{tl_version}, tex(utfjmbna-v.vf) = %{tl_version}
Provides:       tex(utfjmbnb-h.vf) = %{tl_version}, tex(utfjmbnb-v.vf) = %{tl_version}
Provides:       tex(utfjmbnc-h.vf) = %{tl_version}, tex(utfjmbnc-v.vf) = %{tl_version}
Provides:       tex(utfjmbnd-h.vf) = %{tl_version}, tex(utfjmbnd-v.vf) = %{tl_version}
Provides:       tex(utfjmbne-h.vf) = %{tl_version}, tex(utfjmbne-v.vf) = %{tl_version}
Provides:       tex(utfjmbnf-h.vf) = %{tl_version}, tex(utfjmbnf-v.vf) = %{tl_version}
Provides:       tex(utfjmgr0-h.vf) = %{tl_version}, tex(utfjmgr0-v.vf) = %{tl_version}
Provides:       tex(utfjmgr1-h.vf) = %{tl_version}, tex(utfjmgr1-v.vf) = %{tl_version}
Provides:       tex(utfjmgr2-h.vf) = %{tl_version}, tex(utfjmgr2-v.vf) = %{tl_version}
Provides:       tex(utfjmgr3-h.vf) = %{tl_version}, tex(utfjmgr3-v.vf) = %{tl_version}
Provides:       tex(utfjmgr4-h.vf) = %{tl_version}, tex(utfjmgr4-v.vf) = %{tl_version}
Provides:       tex(utfjmgr5-h.vf) = %{tl_version}, tex(utfjmgr5-v.vf) = %{tl_version}
Provides:       tex(utfjmgr6-h.vf) = %{tl_version}, tex(utfjmgr6-v.vf) = %{tl_version}
Provides:       tex(utfjmgr7-h.vf) = %{tl_version}, tex(utfjmgr7-v.vf) = %{tl_version}
Provides:       tex(utfjmgr8-h.vf) = %{tl_version}, tex(utfjmgr8-v.vf) = %{tl_version}
Provides:       tex(utfjmgr9-h.vf) = %{tl_version}, tex(utfjmgr9-v.vf) = %{tl_version}
Provides:       tex(utfjmgra-h.vf) = %{tl_version}, tex(utfjmgra-v.vf) = %{tl_version}
Provides:       tex(utfjmgrb-h.vf) = %{tl_version}, tex(utfjmgrb-v.vf) = %{tl_version}
Provides:       tex(utfjmgrc-h.vf) = %{tl_version}, tex(utfjmgrc-v.vf) = %{tl_version}
Provides:       tex(utfjmgrd-h.vf) = %{tl_version}, tex(utfjmgrd-v.vf) = %{tl_version}
Provides:       tex(utfjmgre-h.vf) = %{tl_version}, tex(utfjmgre-v.vf) = %{tl_version}
Provides:       tex(utfjmgrf-h.vf) = %{tl_version}, tex(utfjmgrf-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn0-h.vf) = %{tl_version}, tex(utfjmgrn0-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn1-h.vf) = %{tl_version}, tex(utfjmgrn1-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn2-h.vf) = %{tl_version}, tex(utfjmgrn2-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn3-h.vf) = %{tl_version}, tex(utfjmgrn3-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn4-h.vf) = %{tl_version}, tex(utfjmgrn4-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn5-h.vf) = %{tl_version}, tex(utfjmgrn5-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn6-h.vf) = %{tl_version}, tex(utfjmgrn6-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn7-h.vf) = %{tl_version}, tex(utfjmgrn7-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn8-h.vf) = %{tl_version}, tex(utfjmgrn8-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn9-h.vf) = %{tl_version}, tex(utfjmgrn9-v.vf) = %{tl_version}
Provides:       tex(utfjmgrna-h.vf) = %{tl_version}, tex(utfjmgrna-v.vf) = %{tl_version}
Provides:       tex(utfjmgrnb-h.vf) = %{tl_version}, tex(utfjmgrnb-v.vf) = %{tl_version}
Provides:       tex(utfjmgrnc-h.vf) = %{tl_version}, tex(utfjmgrnc-v.vf) = %{tl_version}
Provides:       tex(utfjmgrnd-h.vf) = %{tl_version}, tex(utfjmgrnd-v.vf) = %{tl_version}
Provides:       tex(utfjmgrne-h.vf) = %{tl_version}, tex(utfjmgrne-v.vf) = %{tl_version}
Provides:       tex(utfjmgrnf-h.vf) = %{tl_version}, tex(utfjmgrnf-v.vf) = %{tl_version}
Provides:       tex(utfjml0-h.vf) = %{tl_version}, tex(utfjml0-v.vf) = %{tl_version}
Provides:       tex(utfjml1-h.vf) = %{tl_version}, tex(utfjml1-v.vf) = %{tl_version}
Provides:       tex(utfjml2-h.vf) = %{tl_version}, tex(utfjml2-v.vf) = %{tl_version}
Provides:       tex(utfjml3-h.vf) = %{tl_version}, tex(utfjml3-v.vf) = %{tl_version}
Provides:       tex(utfjml4-h.vf) = %{tl_version}, tex(utfjml4-v.vf) = %{tl_version}
Provides:       tex(utfjml5-h.vf) = %{tl_version}, tex(utfjml5-v.vf) = %{tl_version}
Provides:       tex(utfjml6-h.vf) = %{tl_version}, tex(utfjml6-v.vf) = %{tl_version}
Provides:       tex(utfjml7-h.vf) = %{tl_version}, tex(utfjml7-v.vf) = %{tl_version}
Provides:       tex(utfjml8-h.vf) = %{tl_version}, tex(utfjml8-v.vf) = %{tl_version}
Provides:       tex(utfjml9-h.vf) = %{tl_version}, tex(utfjml9-v.vf) = %{tl_version}
Provides:       tex(utfjmla-h.vf) = %{tl_version}, tex(utfjmla-v.vf) = %{tl_version}
Provides:       tex(utfjmlb-h.vf) = %{tl_version}, tex(utfjmlb-v.vf) = %{tl_version}
Provides:       tex(utfjmlc-h.vf) = %{tl_version}, tex(utfjmlc-v.vf) = %{tl_version}
Provides:       tex(utfjmld-h.vf) = %{tl_version}, tex(utfjmld-v.vf) = %{tl_version}
Provides:       tex(utfjmle-h.vf) = %{tl_version}, tex(utfjmle-v.vf) = %{tl_version}
Provides:       tex(utfjmlf-h.vf) = %{tl_version}, tex(utfjmlf-v.vf) = %{tl_version}
Provides:       tex(utfjmln0-h.vf) = %{tl_version}, tex(utfjmln0-v.vf) = %{tl_version}
Provides:       tex(utfjmln1-h.vf) = %{tl_version}, tex(utfjmln1-v.vf) = %{tl_version}
Provides:       tex(utfjmln2-h.vf) = %{tl_version}, tex(utfjmln2-v.vf) = %{tl_version}
Provides:       tex(utfjmln3-h.vf) = %{tl_version}, tex(utfjmln3-v.vf) = %{tl_version}
Provides:       tex(utfjmln4-h.vf) = %{tl_version}, tex(utfjmln4-v.vf) = %{tl_version}
Provides:       tex(utfjmln5-h.vf) = %{tl_version}, tex(utfjmln5-v.vf) = %{tl_version}
Provides:       tex(utfjmln6-h.vf) = %{tl_version}, tex(utfjmln6-v.vf) = %{tl_version}
Provides:       tex(utfjmln7-h.vf) = %{tl_version}, tex(utfjmln7-v.vf) = %{tl_version}
Provides:       tex(utfjmln8-h.vf) = %{tl_version}, tex(utfjmln8-v.vf) = %{tl_version}
Provides:       tex(utfjmln9-h.vf) = %{tl_version}, tex(utfjmln9-v.vf) = %{tl_version}
Provides:       tex(utfjmlna-h.vf) = %{tl_version}, tex(utfjmlna-v.vf) = %{tl_version}
Provides:       tex(utfjmlnb-h.vf) = %{tl_version}, tex(utfjmlnb-v.vf) = %{tl_version}
Provides:       tex(utfjmlnc-h.vf) = %{tl_version}, tex(utfjmlnc-v.vf) = %{tl_version}
Provides:       tex(utfjmlnd-h.vf) = %{tl_version}, tex(utfjmlnd-v.vf) = %{tl_version}
Provides:       tex(utfjmlne-h.vf) = %{tl_version}, tex(utfjmlne-v.vf) = %{tl_version}
Provides:       tex(utfjmlnf-h.vf) = %{tl_version}, tex(utfjmlnf-v.vf) = %{tl_version}
Provides:       tex(utfjmr0-h.vf) = %{tl_version}, tex(utfjmr0-v.vf) = %{tl_version}
Provides:       tex(utfjmr1-h.vf) = %{tl_version}, tex(utfjmr1-v.vf) = %{tl_version}
Provides:       tex(utfjmr2-h.vf) = %{tl_version}, tex(utfjmr2-v.vf) = %{tl_version}
Provides:       tex(utfjmr3-h.vf) = %{tl_version}, tex(utfjmr3-v.vf) = %{tl_version}
Provides:       tex(utfjmr4-h.vf) = %{tl_version}, tex(utfjmr4-v.vf) = %{tl_version}
Provides:       tex(utfjmr5-h.vf) = %{tl_version}, tex(utfjmr5-v.vf) = %{tl_version}
Provides:       tex(utfjmr6-h.vf) = %{tl_version}, tex(utfjmr6-v.vf) = %{tl_version}
Provides:       tex(utfjmr7-h.vf) = %{tl_version}, tex(utfjmr7-v.vf) = %{tl_version}
Provides:       tex(utfjmr8-h.vf) = %{tl_version}, tex(utfjmr8-v.vf) = %{tl_version}
Provides:       tex(utfjmr9-h.vf) = %{tl_version}, tex(utfjmr9-v.vf) = %{tl_version}
Provides:       tex(utfjmra-h.vf) = %{tl_version}, tex(utfjmra-v.vf) = %{tl_version}
Provides:       tex(utfjmrb-h.vf) = %{tl_version}, tex(utfjmrb-v.vf) = %{tl_version}
Provides:       tex(utfjmrc-h.vf) = %{tl_version}, tex(utfjmrc-v.vf) = %{tl_version}
Provides:       tex(utfjmrd-h.vf) = %{tl_version}, tex(utfjmrd-v.vf) = %{tl_version}
Provides:       tex(utfjmre-h.vf) = %{tl_version}, tex(utfjmre-v.vf) = %{tl_version}
Provides:       tex(utfjmrf-h.vf) = %{tl_version}, tex(utfjmrf-v.vf) = %{tl_version}
Provides:       tex(utfjmrn0-h.vf) = %{tl_version}, tex(utfjmrn0-v.vf) = %{tl_version}
Provides:       tex(utfjmrn1-h.vf) = %{tl_version}, tex(utfjmrn1-v.vf) = %{tl_version}
Provides:       tex(utfjmrn2-h.vf) = %{tl_version}, tex(utfjmrn2-v.vf) = %{tl_version}
Provides:       tex(utfjmrn3-h.vf) = %{tl_version}, tex(utfjmrn3-v.vf) = %{tl_version}
Provides:       tex(utfjmrn4-h.vf) = %{tl_version}, tex(utfjmrn4-v.vf) = %{tl_version}
Provides:       tex(utfjmrn5-h.vf) = %{tl_version}, tex(utfjmrn5-v.vf) = %{tl_version}
Provides:       tex(utfjmrn6-h.vf) = %{tl_version}, tex(utfjmrn6-v.vf) = %{tl_version}
Provides:       tex(utfjmrn7-h.vf) = %{tl_version}, tex(utfjmrn7-v.vf) = %{tl_version}
Provides:       tex(utfjmrn8-h.vf) = %{tl_version}, tex(utfjmrn8-v.vf) = %{tl_version}
Provides:       tex(utfjmrn9-h.vf) = %{tl_version}, tex(utfjmrn9-v.vf) = %{tl_version}
Provides:       tex(utfjmrna-h.vf) = %{tl_version}, tex(utfjmrna-v.vf) = %{tl_version}
Provides:       tex(utfjmrnb-h.vf) = %{tl_version}, tex(utfjmrnb-v.vf) = %{tl_version}
Provides:       tex(utfjmrnc-h.vf) = %{tl_version}, tex(utfjmrnc-v.vf) = %{tl_version}
Provides:       tex(utfjmrnd-h.vf) = %{tl_version}, tex(utfjmrnd-v.vf) = %{tl_version}
Provides:       tex(utfjmrne-h.vf) = %{tl_version}, tex(utfjmrne-v.vf) = %{tl_version}
Provides:       tex(utfjmrnf-h.vf) = %{tl_version}, tex(utfjmrnf-v.vf) = %{tl_version}
Provides:       tex(utfkgr0-h.vf) = %{tl_version}, tex(utfkgr0-v.vf) = %{tl_version}
Provides:       tex(utfkgr1-h.vf) = %{tl_version}, tex(utfkgr1-v.vf) = %{tl_version}
Provides:       tex(utfkgr2-h.vf) = %{tl_version}, tex(utfkgr2-v.vf) = %{tl_version}
Provides:       tex(utfkgr3-h.vf) = %{tl_version}, tex(utfkgr3-v.vf) = %{tl_version}
Provides:       tex(utfkgr4-h.vf) = %{tl_version}, tex(utfkgr4-v.vf) = %{tl_version}
Provides:       tex(utfkgr5-h.vf) = %{tl_version}, tex(utfkgr5-v.vf) = %{tl_version}
Provides:       tex(utfkgr6-h.vf) = %{tl_version}, tex(utfkgr6-v.vf) = %{tl_version}
Provides:       tex(utfkgr7-h.vf) = %{tl_version}, tex(utfkgr7-v.vf) = %{tl_version}
Provides:       tex(utfkgr8-h.vf) = %{tl_version}, tex(utfkgr8-v.vf) = %{tl_version}
Provides:       tex(utfkgr9-h.vf) = %{tl_version}, tex(utfkgr9-v.vf) = %{tl_version}
Provides:       tex(utfkgra-h.vf) = %{tl_version}, tex(utfkgra-v.vf) = %{tl_version}
Provides:       tex(utfkgrb-h.vf) = %{tl_version}, tex(utfkgrb-v.vf) = %{tl_version}
Provides:       tex(utfkgrc-h.vf) = %{tl_version}, tex(utfkgrc-v.vf) = %{tl_version}
Provides:       tex(utfkgrd-h.vf) = %{tl_version}, tex(utfkgrd-v.vf) = %{tl_version}
Provides:       tex(utfkgre-h.vf) = %{tl_version}, tex(utfkgre-v.vf) = %{tl_version}
Provides:       tex(utfkgrf-h.vf) = %{tl_version}, tex(utfkgrf-v.vf) = %{tl_version}
Provides:       tex(utfkmr0-h.vf) = %{tl_version}, tex(utfkmr0-v.vf) = %{tl_version}
Provides:       tex(utfkmr1-h.vf) = %{tl_version}, tex(utfkmr1-v.vf) = %{tl_version}
Provides:       tex(utfkmr2-h.vf) = %{tl_version}, tex(utfkmr2-v.vf) = %{tl_version}
Provides:       tex(utfkmr3-h.vf) = %{tl_version}, tex(utfkmr3-v.vf) = %{tl_version}
Provides:       tex(utfkmr4-h.vf) = %{tl_version}, tex(utfkmr4-v.vf) = %{tl_version}
Provides:       tex(utfkmr5-h.vf) = %{tl_version}, tex(utfkmr5-v.vf) = %{tl_version}
Provides:       tex(utfkmr6-h.vf) = %{tl_version}, tex(utfkmr6-v.vf) = %{tl_version}
Provides:       tex(utfkmr7-h.vf) = %{tl_version}, tex(utfkmr7-v.vf) = %{tl_version}
Provides:       tex(utfkmr8-h.vf) = %{tl_version}, tex(utfkmr8-v.vf) = %{tl_version}
Provides:       tex(utfkmr9-h.vf) = %{tl_version}, tex(utfkmr9-v.vf) = %{tl_version}
Provides:       tex(utfkmra-h.vf) = %{tl_version}, tex(utfkmra-v.vf) = %{tl_version}
Provides:       tex(utfkmrb-h.vf) = %{tl_version}, tex(utfkmrb-v.vf) = %{tl_version}
Provides:       tex(utfkmrc-h.vf) = %{tl_version}, tex(utfkmrc-v.vf) = %{tl_version}
Provides:       tex(utfkmrd-h.vf) = %{tl_version}, tex(utfkmrd-v.vf) = %{tl_version}
Provides:       tex(utfkmre-h.vf) = %{tl_version}, tex(utfkmre-v.vf) = %{tl_version}
Provides:       tex(utfkmrf-h.vf) = %{tl_version}, tex(utfkmrf-v.vf) = %{tl_version}
Provides:       tex(utfmr0-h.vf) = %{tl_version}, tex(utfmr0-v.vf) = %{tl_version}
Provides:       tex(utfmr1-h.vf) = %{tl_version}, tex(utfmr1-v.vf) = %{tl_version}
Provides:       tex(utfmr2-h.vf) = %{tl_version}, tex(utfmr2-v.vf) = %{tl_version}
Provides:       tex(utfmr3-h.vf) = %{tl_version}, tex(utfmr3-v.vf) = %{tl_version}
Provides:       tex(utfmr4-h.vf) = %{tl_version}, tex(utfmr4-v.vf) = %{tl_version}
Provides:       tex(utfmr5-h.vf) = %{tl_version}, tex(utfmr5-v.vf) = %{tl_version}
Provides:       tex(utfmr6-h.vf) = %{tl_version}, tex(utfmr6-v.vf) = %{tl_version}
Provides:       tex(utfmr7-h.vf) = %{tl_version}, tex(utfmr7-v.vf) = %{tl_version}
Provides:       tex(utfmr8-h.vf) = %{tl_version}, tex(utfmr8-v.vf) = %{tl_version}
Provides:       tex(utfmr9-h.vf) = %{tl_version}, tex(utfmr9-v.vf) = %{tl_version}
Provides:       tex(utfmra-h.vf) = %{tl_version}, tex(utfmra-v.vf) = %{tl_version}
Provides:       tex(utfmrb-h.vf) = %{tl_version}, tex(utfmrb-v.vf) = %{tl_version}
Provides:       tex(utfmrc-h.vf) = %{tl_version}, tex(utfmrc-v.vf) = %{tl_version}
Provides:       tex(utfmrd-h.vf) = %{tl_version}, tex(utfmrd-v.vf) = %{tl_version}
Provides:       tex(utfmre-h.vf) = %{tl_version}, tex(utfmre-v.vf) = %{tl_version}
Provides:       tex(utfmrf-h.vf) = %{tl_version}, tex(utfmrf-v.vf) = %{tl_version}
Provides:       tex(utftgr0-h.vf) = %{tl_version}, tex(utftgr0-v.vf) = %{tl_version}
Provides:       tex(utftgr1-h.vf) = %{tl_version}, tex(utftgr1-v.vf) = %{tl_version}
Provides:       tex(utftgr2-h.vf) = %{tl_version}, tex(utftgr2-v.vf) = %{tl_version}
Provides:       tex(utftgr3-h.vf) = %{tl_version}, tex(utftgr3-v.vf) = %{tl_version}
Provides:       tex(utftgr4-h.vf) = %{tl_version}, tex(utftgr4-v.vf) = %{tl_version}
Provides:       tex(utftgr5-h.vf) = %{tl_version}, tex(utftgr5-v.vf) = %{tl_version}
Provides:       tex(utftgr6-h.vf) = %{tl_version}, tex(utftgr6-v.vf) = %{tl_version}
Provides:       tex(utftgr7-h.vf) = %{tl_version}, tex(utftgr7-v.vf) = %{tl_version}
Provides:       tex(utftgr8-h.vf) = %{tl_version}, tex(utftgr8-v.vf) = %{tl_version}
Provides:       tex(utftgr9-h.vf) = %{tl_version}, tex(utftgr9-v.vf) = %{tl_version}
Provides:       tex(utftgra-h.vf) = %{tl_version}, tex(utftgra-v.vf) = %{tl_version}
Provides:       tex(utftgrb-h.vf) = %{tl_version}, tex(utftgrb-v.vf) = %{tl_version}
Provides:       tex(utftgrc-h.vf) = %{tl_version}, tex(utftgrc-v.vf) = %{tl_version}
Provides:       tex(utftgrd-h.vf) = %{tl_version}, tex(utftgrd-v.vf) = %{tl_version}
Provides:       tex(utftgre-h.vf) = %{tl_version}, tex(utftgre-v.vf) = %{tl_version}
Provides:       tex(utftgrf-h.vf) = %{tl_version}, tex(utftgrf-v.vf) = %{tl_version}
Provides:       tex(utftmr0-h.vf) = %{tl_version}, tex(utftmr0-v.vf) = %{tl_version}
Provides:       tex(utftmr1-h.vf) = %{tl_version}, tex(utftmr1-v.vf) = %{tl_version}
Provides:       tex(utftmr2-h.vf) = %{tl_version}, tex(utftmr2-v.vf) = %{tl_version}
Provides:       tex(utftmr3-h.vf) = %{tl_version}, tex(utftmr3-v.vf) = %{tl_version}
Provides:       tex(utftmr4-h.vf) = %{tl_version}, tex(utftmr4-v.vf) = %{tl_version}
Provides:       tex(utftmr5-h.vf) = %{tl_version}, tex(utftmr5-v.vf) = %{tl_version}
Provides:       tex(utftmr6-h.vf) = %{tl_version}, tex(utftmr6-v.vf) = %{tl_version}
Provides:       tex(utftmr7-h.vf) = %{tl_version}, tex(utftmr7-v.vf) = %{tl_version}
Provides:       tex(utftmr8-h.vf) = %{tl_version}, tex(utftmr8-v.vf) = %{tl_version}
Provides:       tex(utftmr9-h.vf) = %{tl_version}, tex(utftmr9-v.vf) = %{tl_version}
Provides:       tex(utftmra-h.vf) = %{tl_version}, tex(utftmra-v.vf) = %{tl_version}
Provides:       tex(utftmrb-h.vf) = %{tl_version}, tex(utftmrb-v.vf) = %{tl_version}
Provides:       tex(utftmrc-h.vf) = %{tl_version}, tex(utftmrc-v.vf) = %{tl_version}
Provides:       tex(utftmrd-h.vf) = %{tl_version}, tex(utftmrd-v.vf) = %{tl_version}
Provides:       tex(utftmre-h.vf) = %{tl_version}, tex(utftmre-v.vf) = %{tl_version}
Provides:       tex(utftmrf-h.vf) = %{tl_version}, tex(utftmrf-v.vf) = %{tl_version}
Provides:       tex(ajmacros.sty) = %{tl_version}, tex(mlcid.sty) = %{tl_version}
Provides:       tex(redeffont.sty) = %{tl_version}

%description -n texlive-japanese-otf
The package contains pLaTeX support files and virtual fonts for
supporting a wide variety of fonts in LaTeX using the pTeX
engine.

%package -n texlive-japanese-otf-doc
Summary:        Documentation for japanese-otf
Version:        svn46598
Provides:       tex-japanese-otf-doc
AutoReqProv:    No

%description -n texlive-japanese-otf-doc
Documentation for japanese-otf

%package -n texlive-japanese-otf-uptex
Provides:       tex-japanese-otf-uptex = %{tl_version}
License:        BSD
Summary:        Support for Japanese OTF files in upLaTeX
Version:        svn47702
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex-japanese-otf
Requires:       tex(keyval.sty), tex(mlcid.sty), tex(ajmacros.sty)
Provides:       tex(upbrsgexpgothb-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothb-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothbn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothbn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgotheb-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgotheb-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothebn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothebn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothr-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothr-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothrn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothrn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpmgothr-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpmgothr-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpmgothrn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpmgothrn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminb-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminb-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminbn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminbn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminl-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminl-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminln-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminln-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminr-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminr-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminrn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgexpminrn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothb-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothb-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothbn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothbn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgotheb-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgotheb-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothebn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothebn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothr-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothr-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothrn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlgothrn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlmgothr-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlmgothr-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlmgothrn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlmgothrn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminb-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminb-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminbn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminbn-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminl-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminl-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminln-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminln-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminr-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminr-v.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminrn-h.tfm) = %{tl_version}
Provides:       tex(upbrsgnmlminrn-v.tfm) = %{tl_version}
Provides:       tex(upexpgothb-h.tfm) = %{tl_version}, tex(upexpgothb-v.tfm) = %{tl_version}
Provides:       tex(upexpgothbn-h.tfm) = %{tl_version}, tex(upexpgothbn-v.tfm) = %{tl_version}
Provides:       tex(upexpgotheb-h.tfm) = %{tl_version}, tex(upexpgotheb-v.tfm) = %{tl_version}
Provides:       tex(upexpgothebn-h.tfm) = %{tl_version}, tex(upexpgothebn-v.tfm) = %{tl_version}
Provides:       tex(upexpgothr-h.tfm) = %{tl_version}, tex(upexpgothr-v.tfm) = %{tl_version}
Provides:       tex(upexpgothrn-h.tfm) = %{tl_version}, tex(upexpgothrn-v.tfm) = %{tl_version}
Provides:       tex(upexpmgothr-h.tfm) = %{tl_version}, tex(upexpmgothr-v.tfm) = %{tl_version}
Provides:       tex(upexpmgothrn-h.tfm) = %{tl_version}, tex(upexpmgothrn-v.tfm) = %{tl_version}
Provides:       tex(upexpminb-h.tfm) = %{tl_version}, tex(upexpminb-v.tfm) = %{tl_version}
Provides:       tex(upexpminbn-h.tfm) = %{tl_version}, tex(upexpminbn-v.tfm) = %{tl_version}
Provides:       tex(upexpminl-h.tfm) = %{tl_version}, tex(upexpminl-v.tfm) = %{tl_version}
Provides:       tex(upexpminln-h.tfm) = %{tl_version}, tex(upexpminln-v.tfm) = %{tl_version}
Provides:       tex(upexpminr-h.tfm) = %{tl_version}, tex(upexpminr-v.tfm) = %{tl_version}
Provides:       tex(upexpminrn-h.tfm) = %{tl_version}, tex(upexpminrn-v.tfm) = %{tl_version}
Provides:       tex(uphgothb-h.tfm) = %{tl_version}, tex(uphgothb-v.tfm) = %{tl_version}
Provides:       tex(uphgothbn-h.tfm) = %{tl_version}, tex(uphgothbn-v.tfm) = %{tl_version}
Provides:       tex(uphgotheb-h.tfm) = %{tl_version}, tex(uphgotheb-v.tfm) = %{tl_version}
Provides:       tex(uphgothebn-h.tfm) = %{tl_version}, tex(uphgothebn-v.tfm) = %{tl_version}
Provides:       tex(uphgothr-h.tfm) = %{tl_version}, tex(uphgothr-v.tfm) = %{tl_version}
Provides:       tex(uphgothrn-h.tfm) = %{tl_version}, tex(uphgothrn-v.tfm) = %{tl_version}
Provides:       tex(uphmgothr-h.tfm) = %{tl_version}, tex(uphmgothr-v.tfm) = %{tl_version}
Provides:       tex(uphmgothrn-h.tfm) = %{tl_version}, tex(uphmgothrn-v.tfm) = %{tl_version}
Provides:       tex(uphminb-h.tfm) = %{tl_version}, tex(uphminb-v.tfm) = %{tl_version}
Provides:       tex(uphminbn-h.tfm) = %{tl_version}, tex(uphminbn-v.tfm) = %{tl_version}
Provides:       tex(uphminl-h.tfm) = %{tl_version}, tex(uphminl-v.tfm) = %{tl_version}
Provides:       tex(uphminln-h.tfm) = %{tl_version}, tex(uphminln-v.tfm) = %{tl_version}
Provides:       tex(uphminr-h.tfm) = %{tl_version}, tex(uphminr-v.tfm) = %{tl_version}
Provides:       tex(uphminrn-h.tfm) = %{tl_version}, tex(uphminrn-v.tfm) = %{tl_version}
Provides:       tex(upnmlgothb-h.tfm) = %{tl_version}, tex(upnmlgothb-v.tfm) = %{tl_version}
Provides:       tex(upnmlgothbn-h.tfm) = %{tl_version}, tex(upnmlgothbn-v.tfm) = %{tl_version}
Provides:       tex(upnmlgotheb-h.tfm) = %{tl_version}, tex(upnmlgotheb-v.tfm) = %{tl_version}
Provides:       tex(upnmlgothebn-h.tfm) = %{tl_version}, tex(upnmlgothebn-v.tfm) = %{tl_version}
Provides:       tex(upnmlgothr-h.tfm) = %{tl_version}, tex(upnmlgothr-v.tfm) = %{tl_version}
Provides:       tex(upnmlgothrn-h.tfm) = %{tl_version}, tex(upnmlgothrn-v.tfm) = %{tl_version}
Provides:       tex(upnmlmgothr-h.tfm) = %{tl_version}, tex(upnmlmgothr-v.tfm) = %{tl_version}
Provides:       tex(upnmlmgothrn-h.tfm) = %{tl_version}, tex(upnmlmgothrn-v.tfm) = %{tl_version}
Provides:       tex(upnmlminb-h.tfm) = %{tl_version}, tex(upnmlminb-v.tfm) = %{tl_version}
Provides:       tex(upnmlminbn-h.tfm) = %{tl_version}, tex(upnmlminbn-v.tfm) = %{tl_version}
Provides:       tex(upnmlminl-h.tfm) = %{tl_version}, tex(upnmlminl-v.tfm) = %{tl_version}
Provides:       tex(upnmlminln-h.tfm) = %{tl_version}, tex(upnmlminln-v.tfm) = %{tl_version}
Provides:       tex(upnmlminr-h.tfm) = %{tl_version}, tex(upnmlminr-v.tfm) = %{tl_version}
Provides:       tex(upnmlminrn-h.tfm) = %{tl_version}, tex(upnmlminrn-v.tfm) = %{tl_version}
Provides:       tex(upphirakakuw3-h.tfm) = %{tl_version}
Provides:       tex(upphirakakuw3-v.tfm) = %{tl_version}
Provides:       tex(upphirakakuw6-h.tfm) = %{tl_version}
Provides:       tex(upphirakakuw6-v.tfm) = %{tl_version}
Provides:       tex(upphiramaruw4-h.tfm) = %{tl_version}
Provides:       tex(upphiramaruw4-v.tfm) = %{tl_version}
Provides:       tex(upphiraminw3-h.tfm) = %{tl_version}, tex(upphiraminw3-v.tfm) = %{tl_version}
Provides:       tex(upphiraminw6-h.tfm) = %{tl_version}, tex(upphiraminw6-v.tfm) = %{tl_version}
Provides:       tex(uprubygothb-h.tfm) = %{tl_version}, tex(uprubygothb-v.tfm) = %{tl_version}
Provides:       tex(uprubygotheb-h.tfm) = %{tl_version}, tex(uprubygotheb-v.tfm) = %{tl_version}
Provides:       tex(uprubygothr-h.tfm) = %{tl_version}, tex(uprubygothr-v.tfm) = %{tl_version}
Provides:       tex(uprubymgothr-h.tfm) = %{tl_version}, tex(uprubymgothr-v.tfm) = %{tl_version}
Provides:       tex(uprubyminb-h.tfm) = %{tl_version}, tex(uprubyminb-v.tfm) = %{tl_version}
Provides:       tex(uprubyminl-h.tfm) = %{tl_version}, tex(uprubyminl-v.tfm) = %{tl_version}
Provides:       tex(uprubyminr-h.tfm) = %{tl_version}, tex(uprubyminr-v.tfm) = %{tl_version}
Provides:       tex(utfcgrk-h.tfm) = %{tl_version}, tex(utfcgrk-v.tfm) = %{tl_version}
Provides:       tex(utfcgrl-h.tfm) = %{tl_version}, tex(utfcgrl-v.tfm) = %{tl_version}
Provides:       tex(utfcgrm-h.tfm) = %{tl_version}, tex(utfcgrm-v.tfm) = %{tl_version}
Provides:       tex(utfcgro-h.tfm) = %{tl_version}, tex(utfcgro-v.tfm) = %{tl_version}
Provides:       tex(utfcmrk-h.tfm) = %{tl_version}, tex(utfcmrk-v.tfm) = %{tl_version}
Provides:       tex(utfcmrl-h.tfm) = %{tl_version}, tex(utfcmrl-v.tfm) = %{tl_version}
Provides:       tex(utfcmrm-h.tfm) = %{tl_version}, tex(utfcmrm-v.tfm) = %{tl_version}
Provides:       tex(utfcmro-h.tfm) = %{tl_version}, tex(utfcmro-v.tfm) = %{tl_version}
Provides:       tex(utfgrj-h.tfm) = %{tl_version}, tex(utfgrj-v.tfm) = %{tl_version}
Provides:       tex(utfgrk-h.tfm) = %{tl_version}, tex(utfgrk-v.tfm) = %{tl_version}
Provides:       tex(utfgrl-h.tfm) = %{tl_version}, tex(utfgrl-v.tfm) = %{tl_version}
Provides:       tex(utfgrm-h.tfm) = %{tl_version}, tex(utfgrm-v.tfm) = %{tl_version}
Provides:       tex(utfgrn-h.tfm) = %{tl_version}, tex(utfgrn-v.tfm) = %{tl_version}
Provides:       tex(utfgro-h.tfm) = %{tl_version}, tex(utfgro-v.tfm) = %{tl_version}
Provides:       tex(utfgrp-h.tfm) = %{tl_version}, tex(utfgrp-v.tfm) = %{tl_version}
Provides:       tex(utfgrq-h.tfm) = %{tl_version}, tex(utfgrq-v.tfm) = %{tl_version}
Provides:       tex(utfgrr-h.tfm) = %{tl_version}, tex(utfgrr-v.tfm) = %{tl_version}
Provides:       tex(utfgrs-h.tfm) = %{tl_version}, tex(utfgrs-v.tfm) = %{tl_version}
Provides:       tex(utfgrt-h.tfm) = %{tl_version}, tex(utfgrt-v.tfm) = %{tl_version}
Provides:       tex(utfgru-h.tfm) = %{tl_version}, tex(utfgru-v.tfm) = %{tl_version}
Provides:       tex(utfgrv-h.tfm) = %{tl_version}, tex(utfgrv-v.tfm) = %{tl_version}
Provides:       tex(utfgrz-h.tfm) = %{tl_version}, tex(utfgrz-v.tfm) = %{tl_version}
Provides:       tex(utfjgbj-h.tfm) = %{tl_version}, tex(utfjgbj-v.tfm) = %{tl_version}
Provides:       tex(utfjgbk-h.tfm) = %{tl_version}, tex(utfjgbk-v.tfm) = %{tl_version}
Provides:       tex(utfjgbl-h.tfm) = %{tl_version}, tex(utfjgbl-v.tfm) = %{tl_version}
Provides:       tex(utfjgbm-h.tfm) = %{tl_version}, tex(utfjgbm-v.tfm) = %{tl_version}
Provides:       tex(utfjgbn-h.tfm) = %{tl_version}, tex(utfjgbn-v.tfm) = %{tl_version}
Provides:       tex(utfjgbo-h.tfm) = %{tl_version}, tex(utfjgbo-v.tfm) = %{tl_version}
Provides:       tex(utfjgbp-h.tfm) = %{tl_version}, tex(utfjgbp-v.tfm) = %{tl_version}
Provides:       tex(utfjgbq-h.tfm) = %{tl_version}, tex(utfjgbq-v.tfm) = %{tl_version}
Provides:       tex(utfjgbr-h.tfm) = %{tl_version}, tex(utfjgbr-v.tfm) = %{tl_version}
Provides:       tex(utfjgbs-h.tfm) = %{tl_version}, tex(utfjgbs-v.tfm) = %{tl_version}
Provides:       tex(utfjgbt-h.tfm) = %{tl_version}, tex(utfjgbt-v.tfm) = %{tl_version}
Provides:       tex(utfjgbu-h.tfm) = %{tl_version}, tex(utfjgbu-v.tfm) = %{tl_version}
Provides:       tex(utfjgbv-h.tfm) = %{tl_version}, tex(utfjgbv-v.tfm) = %{tl_version}
Provides:       tex(utfjgbz-h.tfm) = %{tl_version}, tex(utfjgbz-v.tfm) = %{tl_version}
Provides:       tex(utfjgej-h.tfm) = %{tl_version}, tex(utfjgej-v.tfm) = %{tl_version}
Provides:       tex(utfjgek-h.tfm) = %{tl_version}, tex(utfjgek-v.tfm) = %{tl_version}
Provides:       tex(utfjgel-h.tfm) = %{tl_version}, tex(utfjgel-v.tfm) = %{tl_version}
Provides:       tex(utfjgem-h.tfm) = %{tl_version}, tex(utfjgem-v.tfm) = %{tl_version}
Provides:       tex(utfjgen-h.tfm) = %{tl_version}, tex(utfjgen-v.tfm) = %{tl_version}
Provides:       tex(utfjgeo-h.tfm) = %{tl_version}, tex(utfjgeo-v.tfm) = %{tl_version}
Provides:       tex(utfjgep-h.tfm) = %{tl_version}, tex(utfjgep-v.tfm) = %{tl_version}
Provides:       tex(utfjgeq-h.tfm) = %{tl_version}, tex(utfjgeq-v.tfm) = %{tl_version}
Provides:       tex(utfjger-h.tfm) = %{tl_version}, tex(utfjger-v.tfm) = %{tl_version}
Provides:       tex(utfjges-h.tfm) = %{tl_version}, tex(utfjges-v.tfm) = %{tl_version}
Provides:       tex(utfjget-h.tfm) = %{tl_version}, tex(utfjget-v.tfm) = %{tl_version}
Provides:       tex(utfjgeu-h.tfm) = %{tl_version}, tex(utfjgeu-v.tfm) = %{tl_version}
Provides:       tex(utfjgev-h.tfm) = %{tl_version}, tex(utfjgev-v.tfm) = %{tl_version}
Provides:       tex(utfjgez-h.tfm) = %{tl_version}, tex(utfjgez-v.tfm) = %{tl_version}
Provides:       tex(utfjgrj-h.tfm) = %{tl_version}, tex(utfjgrj-v.tfm) = %{tl_version}
Provides:       tex(utfjgrk-h.tfm) = %{tl_version}, tex(utfjgrk-v.tfm) = %{tl_version}
Provides:       tex(utfjgrl-h.tfm) = %{tl_version}, tex(utfjgrl-v.tfm) = %{tl_version}
Provides:       tex(utfjgrm-h.tfm) = %{tl_version}, tex(utfjgrm-v.tfm) = %{tl_version}
Provides:       tex(utfjgrn-h.tfm) = %{tl_version}, tex(utfjgrn-v.tfm) = %{tl_version}
Provides:       tex(utfjgro-h.tfm) = %{tl_version}, tex(utfjgro-v.tfm) = %{tl_version}
Provides:       tex(utfjgrp-h.tfm) = %{tl_version}, tex(utfjgrp-v.tfm) = %{tl_version}
Provides:       tex(utfjgrq-h.tfm) = %{tl_version}, tex(utfjgrq-v.tfm) = %{tl_version}
Provides:       tex(utfjgrr-h.tfm) = %{tl_version}, tex(utfjgrr-v.tfm) = %{tl_version}
Provides:       tex(utfjgrs-h.tfm) = %{tl_version}, tex(utfjgrs-v.tfm) = %{tl_version}
Provides:       tex(utfjgrt-h.tfm) = %{tl_version}, tex(utfjgrt-v.tfm) = %{tl_version}
Provides:       tex(utfjgru-h.tfm) = %{tl_version}, tex(utfjgru-v.tfm) = %{tl_version}
Provides:       tex(utfjgrv-h.tfm) = %{tl_version}, tex(utfjgrv-v.tfm) = %{tl_version}
Provides:       tex(utfjgrz-h.tfm) = %{tl_version}, tex(utfjgrz-v.tfm) = %{tl_version}
Provides:       tex(utfjmbj-h.tfm) = %{tl_version}, tex(utfjmbj-v.tfm) = %{tl_version}
Provides:       tex(utfjmbk-h.tfm) = %{tl_version}, tex(utfjmbk-v.tfm) = %{tl_version}
Provides:       tex(utfjmbl-h.tfm) = %{tl_version}, tex(utfjmbl-v.tfm) = %{tl_version}
Provides:       tex(utfjmbm-h.tfm) = %{tl_version}, tex(utfjmbm-v.tfm) = %{tl_version}
Provides:       tex(utfjmbn-h.tfm) = %{tl_version}, tex(utfjmbn-v.tfm) = %{tl_version}
Provides:       tex(utfjmbo-h.tfm) = %{tl_version}, tex(utfjmbo-v.tfm) = %{tl_version}
Provides:       tex(utfjmbp-h.tfm) = %{tl_version}, tex(utfjmbp-v.tfm) = %{tl_version}
Provides:       tex(utfjmbq-h.tfm) = %{tl_version}, tex(utfjmbq-v.tfm) = %{tl_version}
Provides:       tex(utfjmbr-h.tfm) = %{tl_version}, tex(utfjmbr-v.tfm) = %{tl_version}
Provides:       tex(utfjmbs-h.tfm) = %{tl_version}, tex(utfjmbs-v.tfm) = %{tl_version}
Provides:       tex(utfjmbt-h.tfm) = %{tl_version}, tex(utfjmbt-v.tfm) = %{tl_version}
Provides:       tex(utfjmbu-h.tfm) = %{tl_version}, tex(utfjmbu-v.tfm) = %{tl_version}
Provides:       tex(utfjmbv-h.tfm) = %{tl_version}, tex(utfjmbv-v.tfm) = %{tl_version}
Provides:       tex(utfjmbz-h.tfm) = %{tl_version}, tex(utfjmbz-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrj-h.tfm) = %{tl_version}, tex(utfjmgrj-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrk-h.tfm) = %{tl_version}, tex(utfjmgrk-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrl-h.tfm) = %{tl_version}, tex(utfjmgrl-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrm-h.tfm) = %{tl_version}, tex(utfjmgrm-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrn-h.tfm) = %{tl_version}, tex(utfjmgrn-v.tfm) = %{tl_version}
Provides:       tex(utfjmgro-h.tfm) = %{tl_version}, tex(utfjmgro-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrp-h.tfm) = %{tl_version}, tex(utfjmgrp-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrq-h.tfm) = %{tl_version}, tex(utfjmgrq-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrr-h.tfm) = %{tl_version}, tex(utfjmgrr-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrs-h.tfm) = %{tl_version}, tex(utfjmgrs-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrt-h.tfm) = %{tl_version}, tex(utfjmgrt-v.tfm) = %{tl_version}
Provides:       tex(utfjmgru-h.tfm) = %{tl_version}, tex(utfjmgru-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrv-h.tfm) = %{tl_version}, tex(utfjmgrv-v.tfm) = %{tl_version}
Provides:       tex(utfjmgrz-h.tfm) = %{tl_version}, tex(utfjmgrz-v.tfm) = %{tl_version}
Provides:       tex(utfjmlj-h.tfm) = %{tl_version}, tex(utfjmlj-v.tfm) = %{tl_version}
Provides:       tex(utfjmlk-h.tfm) = %{tl_version}, tex(utfjmlk-v.tfm) = %{tl_version}
Provides:       tex(utfjmll-h.tfm) = %{tl_version}, tex(utfjmll-v.tfm) = %{tl_version}
Provides:       tex(utfjmlm-h.tfm) = %{tl_version}, tex(utfjmlm-v.tfm) = %{tl_version}
Provides:       tex(utfjmln-h.tfm) = %{tl_version}, tex(utfjmln-v.tfm) = %{tl_version}
Provides:       tex(utfjmlo-h.tfm) = %{tl_version}, tex(utfjmlo-v.tfm) = %{tl_version}
Provides:       tex(utfjmlp-h.tfm) = %{tl_version}, tex(utfjmlp-v.tfm) = %{tl_version}
Provides:       tex(utfjmlq-h.tfm) = %{tl_version}, tex(utfjmlq-v.tfm) = %{tl_version}
Provides:       tex(utfjmlr-h.tfm) = %{tl_version}, tex(utfjmlr-v.tfm) = %{tl_version}
Provides:       tex(utfjmls-h.tfm) = %{tl_version}, tex(utfjmls-v.tfm) = %{tl_version}
Provides:       tex(utfjmlt-h.tfm) = %{tl_version}, tex(utfjmlt-v.tfm) = %{tl_version}
Provides:       tex(utfjmlu-h.tfm) = %{tl_version}, tex(utfjmlu-v.tfm) = %{tl_version}
Provides:       tex(utfjmlv-h.tfm) = %{tl_version}, tex(utfjmlv-v.tfm) = %{tl_version}
Provides:       tex(utfjmlz-h.tfm) = %{tl_version}, tex(utfjmlz-v.tfm) = %{tl_version}
Provides:       tex(utfjmrj-h.tfm) = %{tl_version}, tex(utfjmrj-v.tfm) = %{tl_version}
Provides:       tex(utfjmrk-h.tfm) = %{tl_version}, tex(utfjmrk-v.tfm) = %{tl_version}
Provides:       tex(utfjmrl-h.tfm) = %{tl_version}, tex(utfjmrl-v.tfm) = %{tl_version}
Provides:       tex(utfjmrm-h.tfm) = %{tl_version}, tex(utfjmrm-v.tfm) = %{tl_version}
Provides:       tex(utfjmrn-h.tfm) = %{tl_version}, tex(utfjmrn-v.tfm) = %{tl_version}
Provides:       tex(utfjmro-h.tfm) = %{tl_version}, tex(utfjmro-v.tfm) = %{tl_version}
Provides:       tex(utfjmrp-h.tfm) = %{tl_version}, tex(utfjmrp-v.tfm) = %{tl_version}
Provides:       tex(utfjmrq-h.tfm) = %{tl_version}, tex(utfjmrq-v.tfm) = %{tl_version}
Provides:       tex(utfjmrr-h.tfm) = %{tl_version}, tex(utfjmrr-v.tfm) = %{tl_version}
Provides:       tex(utfjmrs-h.tfm) = %{tl_version}, tex(utfjmrs-v.tfm) = %{tl_version}
Provides:       tex(utfjmrt-h.tfm) = %{tl_version}, tex(utfjmrt-v.tfm) = %{tl_version}
Provides:       tex(utfjmru-h.tfm) = %{tl_version}, tex(utfjmru-v.tfm) = %{tl_version}
Provides:       tex(utfjmrv-h.tfm) = %{tl_version}, tex(utfjmrv-v.tfm) = %{tl_version}
Provides:       tex(utfjmrz-h.tfm) = %{tl_version}, tex(utfjmrz-v.tfm) = %{tl_version}
Provides:       tex(utfmrj-h.tfm) = %{tl_version}, tex(utfmrj-v.tfm) = %{tl_version}
Provides:       tex(utfmrk-h.tfm) = %{tl_version}, tex(utfmrk-v.tfm) = %{tl_version}
Provides:       tex(utfmrl-h.tfm) = %{tl_version}, tex(utfmrl-v.tfm) = %{tl_version}
Provides:       tex(utfmrm-h.tfm) = %{tl_version}, tex(utfmrm-v.tfm) = %{tl_version}
Provides:       tex(utfmrn-h.tfm) = %{tl_version}, tex(utfmrn-v.tfm) = %{tl_version}
Provides:       tex(utfmro-h.tfm) = %{tl_version}, tex(utfmro-v.tfm) = %{tl_version}
Provides:       tex(utfmrp-h.tfm) = %{tl_version}, tex(utfmrp-v.tfm) = %{tl_version}
Provides:       tex(utfmrq-h.tfm) = %{tl_version}, tex(utfmrq-v.tfm) = %{tl_version}
Provides:       tex(utfmrr-h.tfm) = %{tl_version}, tex(utfmrr-v.tfm) = %{tl_version}
Provides:       tex(utfmrs-h.tfm) = %{tl_version}, tex(utfmrs-v.tfm) = %{tl_version}
Provides:       tex(utfmrt-h.tfm) = %{tl_version}, tex(utfmrt-v.tfm) = %{tl_version}
Provides:       tex(utfmru-h.tfm) = %{tl_version}, tex(utfmru-v.tfm) = %{tl_version}
Provides:       tex(utfmrv-h.tfm) = %{tl_version}, tex(utfmrv-v.tfm) = %{tl_version}
Provides:       tex(utfmrz-h.tfm) = %{tl_version}, tex(utfmrz-v.tfm) = %{tl_version}
Provides:       tex(utftgrk-h.tfm) = %{tl_version}, tex(utftgrk-v.tfm) = %{tl_version}
Provides:       tex(utftgrl-h.tfm) = %{tl_version}, tex(utftgrl-v.tfm) = %{tl_version}
Provides:       tex(utftgrm-h.tfm) = %{tl_version}, tex(utftgrm-v.tfm) = %{tl_version}
Provides:       tex(utftgrn-h.tfm) = %{tl_version}, tex(utftgrn-v.tfm) = %{tl_version}
Provides:       tex(utftgro-h.tfm) = %{tl_version}, tex(utftgro-v.tfm) = %{tl_version}
Provides:       tex(utftgrp-h.tfm) = %{tl_version}, tex(utftgrp-v.tfm) = %{tl_version}
Provides:       tex(utftgrq-h.tfm) = %{tl_version}, tex(utftgrq-v.tfm) = %{tl_version}
Provides:       tex(utftgrr-h.tfm) = %{tl_version}, tex(utftgrr-v.tfm) = %{tl_version}
Provides:       tex(utftgrs-h.tfm) = %{tl_version}, tex(utftgrs-v.tfm) = %{tl_version}
Provides:       tex(utftgrt-h.tfm) = %{tl_version}, tex(utftgrt-v.tfm) = %{tl_version}
Provides:       tex(utftgru-h.tfm) = %{tl_version}, tex(utftgru-v.tfm) = %{tl_version}
Provides:       tex(utftgrz-h.tfm) = %{tl_version}, tex(utftgrz-v.tfm) = %{tl_version}
Provides:       tex(utftmrk-h.tfm) = %{tl_version}, tex(utftmrk-v.tfm) = %{tl_version}
Provides:       tex(utftmrl-h.tfm) = %{tl_version}, tex(utftmrl-v.tfm) = %{tl_version}
Provides:       tex(utftmrm-h.tfm) = %{tl_version}, tex(utftmrm-v.tfm) = %{tl_version}
Provides:       tex(utftmrn-h.tfm) = %{tl_version}, tex(utftmrn-v.tfm) = %{tl_version}
Provides:       tex(utftmro-h.tfm) = %{tl_version}, tex(utftmro-v.tfm) = %{tl_version}
Provides:       tex(utftmrp-h.tfm) = %{tl_version}, tex(utftmrp-v.tfm) = %{tl_version}
Provides:       tex(utftmrq-h.tfm) = %{tl_version}, tex(utftmrq-v.tfm) = %{tl_version}
Provides:       tex(utftmrr-h.tfm) = %{tl_version}, tex(utftmrr-v.tfm) = %{tl_version}
Provides:       tex(utftmrs-h.tfm) = %{tl_version}, tex(utftmrs-v.tfm) = %{tl_version}
Provides:       tex(utftmrt-h.tfm) = %{tl_version}, tex(utftmrt-v.tfm) = %{tl_version}
Provides:       tex(utftmru-h.tfm) = %{tl_version}, tex(utftmru-v.tfm) = %{tl_version}
Provides:       tex(utftmrz-h.tfm) = %{tl_version}, tex(utftmrz-v.tfm) = %{tl_version}
Provides:       tex(upbrsgexpgothb-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothb-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothbn-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothbn-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpgotheb-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpgotheb-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothebn-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothebn-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothr-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothr-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothrn-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpgothrn-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpmgothr-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpmgothr-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpmgothrn-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpmgothrn-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpminb-h.vf) = %{tl_version}, tex(upbrsgexpminb-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpminbn-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpminbn-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpminl-h.vf) = %{tl_version}, tex(upbrsgexpminl-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpminln-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpminln-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpminr-h.vf) = %{tl_version}, tex(upbrsgexpminr-v.vf) = %{tl_version}
Provides:       tex(upbrsgexpminrn-h.vf) = %{tl_version}
Provides:       tex(upbrsgexpminrn-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothb-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothb-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothbn-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothbn-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgotheb-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgotheb-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothebn-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothebn-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothr-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothr-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothrn-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlgothrn-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlmgothr-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlmgothr-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlmgothrn-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlmgothrn-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminb-h.vf) = %{tl_version}, tex(upbrsgnmlminb-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminbn-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminbn-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminl-h.vf) = %{tl_version}, tex(upbrsgnmlminl-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminln-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminln-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminr-h.vf) = %{tl_version}, tex(upbrsgnmlminr-v.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminrn-h.vf) = %{tl_version}
Provides:       tex(upbrsgnmlminrn-v.vf) = %{tl_version}
Provides:       tex(upexpgothb-h.vf) = %{tl_version}, tex(upexpgothb-v.vf) = %{tl_version}
Provides:       tex(upexpgothbn-h.vf) = %{tl_version}, tex(upexpgothbn-v.vf) = %{tl_version}
Provides:       tex(upexpgotheb-h.vf) = %{tl_version}, tex(upexpgotheb-v.vf) = %{tl_version}
Provides:       tex(upexpgothebn-h.vf) = %{tl_version}, tex(upexpgothebn-v.vf) = %{tl_version}
Provides:       tex(upexpgothr-h.vf) = %{tl_version}, tex(upexpgothr-v.vf) = %{tl_version}
Provides:       tex(upexpgothrn-h.vf) = %{tl_version}, tex(upexpgothrn-v.vf) = %{tl_version}
Provides:       tex(upexpmgothr-h.vf) = %{tl_version}, tex(upexpmgothr-v.vf) = %{tl_version}
Provides:       tex(upexpmgothrn-h.vf) = %{tl_version}, tex(upexpmgothrn-v.vf) = %{tl_version}
Provides:       tex(upexpminb-h.vf) = %{tl_version}, tex(upexpminb-v.vf) = %{tl_version}
Provides:       tex(upexpminbn-h.vf) = %{tl_version}, tex(upexpminbn-v.vf) = %{tl_version}
Provides:       tex(upexpminl-h.vf) = %{tl_version}, tex(upexpminl-v.vf) = %{tl_version}
Provides:       tex(upexpminln-h.vf) = %{tl_version}, tex(upexpminln-v.vf) = %{tl_version}
Provides:       tex(upexpminr-h.vf) = %{tl_version}, tex(upexpminr-v.vf) = %{tl_version}
Provides:       tex(upexpminrn-h.vf) = %{tl_version}, tex(upexpminrn-v.vf) = %{tl_version}
Provides:       tex(upnmlgothb-h.vf) = %{tl_version}, tex(upnmlgothb-v.vf) = %{tl_version}
Provides:       tex(upnmlgothbn-h.vf) = %{tl_version}, tex(upnmlgothbn-v.vf) = %{tl_version}
Provides:       tex(upnmlgotheb-h.vf) = %{tl_version}, tex(upnmlgotheb-v.vf) = %{tl_version}
Provides:       tex(upnmlgothebn-h.vf) = %{tl_version}, tex(upnmlgothebn-v.vf) = %{tl_version}
Provides:       tex(upnmlgothr-h.vf) = %{tl_version}, tex(upnmlgothr-v.vf) = %{tl_version}
Provides:       tex(upnmlgothrn-h.vf) = %{tl_version}, tex(upnmlgothrn-v.vf) = %{tl_version}
Provides:       tex(upnmlmgothr-h.vf) = %{tl_version}, tex(upnmlmgothr-v.vf) = %{tl_version}
Provides:       tex(upnmlmgothrn-h.vf) = %{tl_version}, tex(upnmlmgothrn-v.vf) = %{tl_version}
Provides:       tex(upnmlminb-h.vf) = %{tl_version}, tex(upnmlminb-v.vf) = %{tl_version}
Provides:       tex(upnmlminbn-h.vf) = %{tl_version}, tex(upnmlminbn-v.vf) = %{tl_version}
Provides:       tex(upnmlminl-h.vf) = %{tl_version}, tex(upnmlminl-v.vf) = %{tl_version}
Provides:       tex(upnmlminln-h.vf) = %{tl_version}, tex(upnmlminln-v.vf) = %{tl_version}
Provides:       tex(upnmlminr-h.vf) = %{tl_version}, tex(upnmlminr-v.vf) = %{tl_version}
Provides:       tex(upnmlminrn-h.vf) = %{tl_version}, tex(upnmlminrn-v.vf) = %{tl_version}
Provides:       tex(upphirakakuw3-h.vf) = %{tl_version}, tex(upphirakakuw3-v.vf) = %{tl_version}
Provides:       tex(upphirakakuw6-h.vf) = %{tl_version}, tex(upphirakakuw6-v.vf) = %{tl_version}
Provides:       tex(upphiramaruw4-h.vf) = %{tl_version}, tex(upphiramaruw4-v.vf) = %{tl_version}
Provides:       tex(upphiraminw3-h.vf) = %{tl_version}, tex(upphiraminw3-v.vf) = %{tl_version}
Provides:       tex(upphiraminw6-h.vf) = %{tl_version}, tex(upphiraminw6-v.vf) = %{tl_version}
Provides:       tex(uprubygothb-h.vf) = %{tl_version}, tex(uprubygothb-v.vf) = %{tl_version}
Provides:       tex(uprubygotheb-h.vf) = %{tl_version}, tex(uprubygotheb-v.vf) = %{tl_version}
Provides:       tex(uprubygothr-h.vf) = %{tl_version}, tex(uprubygothr-v.vf) = %{tl_version}
Provides:       tex(uprubymgothr-h.vf) = %{tl_version}, tex(uprubymgothr-v.vf) = %{tl_version}
Provides:       tex(uprubyminb-h.vf) = %{tl_version}, tex(uprubyminb-v.vf) = %{tl_version}
Provides:       tex(uprubyminl-h.vf) = %{tl_version}, tex(uprubyminl-v.vf) = %{tl_version}
Provides:       tex(uprubyminr-h.vf) = %{tl_version}, tex(uprubyminr-v.vf) = %{tl_version}
Provides:       tex(utfcgrk-h.vf) = %{tl_version}, tex(utfcgrk-v.vf) = %{tl_version}
Provides:       tex(utfcgrl-h.vf) = %{tl_version}, tex(utfcgrl-v.vf) = %{tl_version}
Provides:       tex(utfcgrm-h.vf) = %{tl_version}, tex(utfcgrm-v.vf) = %{tl_version}
Provides:       tex(utfcgro-h.vf) = %{tl_version}, tex(utfcgro-v.vf) = %{tl_version}
Provides:       tex(utfcmrk-h.vf) = %{tl_version}, tex(utfcmrk-v.vf) = %{tl_version}
Provides:       tex(utfcmrl-h.vf) = %{tl_version}, tex(utfcmrl-v.vf) = %{tl_version}
Provides:       tex(utfcmrm-h.vf) = %{tl_version}, tex(utfcmrm-v.vf) = %{tl_version}
Provides:       tex(utfcmro-h.vf) = %{tl_version}, tex(utfcmro-v.vf) = %{tl_version}
Provides:       tex(utfgrj-h.vf) = %{tl_version}, tex(utfgrj-v.vf) = %{tl_version}
Provides:       tex(utfgrk-h.vf) = %{tl_version}, tex(utfgrk-v.vf) = %{tl_version}
Provides:       tex(utfgrl-h.vf) = %{tl_version}, tex(utfgrl-v.vf) = %{tl_version}
Provides:       tex(utfgrm-h.vf) = %{tl_version}, tex(utfgrm-v.vf) = %{tl_version}
Provides:       tex(utfgrn-h.vf) = %{tl_version}, tex(utfgrn-v.vf) = %{tl_version}
Provides:       tex(utfgro-h.vf) = %{tl_version}, tex(utfgro-v.vf) = %{tl_version}
Provides:       tex(utfgrp-h.vf) = %{tl_version}, tex(utfgrp-v.vf) = %{tl_version}
Provides:       tex(utfgrq-h.vf) = %{tl_version}, tex(utfgrq-v.vf) = %{tl_version}
Provides:       tex(utfgrr-h.vf) = %{tl_version}, tex(utfgrr-v.vf) = %{tl_version}
Provides:       tex(utfgrs-h.vf) = %{tl_version}, tex(utfgrs-v.vf) = %{tl_version}
Provides:       tex(utfgrt-h.vf) = %{tl_version}, tex(utfgrt-v.vf) = %{tl_version}
Provides:       tex(utfgru-h.vf) = %{tl_version}, tex(utfgru-v.vf) = %{tl_version}
Provides:       tex(utfgrv-h.vf) = %{tl_version}, tex(utfgrv-v.vf) = %{tl_version}
Provides:       tex(utfgrz-h.vf) = %{tl_version}, tex(utfgrz-v.vf) = %{tl_version}
Provides:       tex(utfjgbj-h.vf) = %{tl_version}, tex(utfjgbj-v.vf) = %{tl_version}
Provides:       tex(utfjgbk-h.vf) = %{tl_version}, tex(utfjgbk-v.vf) = %{tl_version}
Provides:       tex(utfjgbl-h.vf) = %{tl_version}, tex(utfjgbl-v.vf) = %{tl_version}
Provides:       tex(utfjgbm-h.vf) = %{tl_version}, tex(utfjgbm-v.vf) = %{tl_version}
Provides:       tex(utfjgbn-h.vf) = %{tl_version}, tex(utfjgbn-v.vf) = %{tl_version}
Provides:       tex(utfjgbo-h.vf) = %{tl_version}, tex(utfjgbo-v.vf) = %{tl_version}
Provides:       tex(utfjgbp-h.vf) = %{tl_version}, tex(utfjgbp-v.vf) = %{tl_version}
Provides:       tex(utfjgbq-h.vf) = %{tl_version}, tex(utfjgbq-v.vf) = %{tl_version}
Provides:       tex(utfjgbr-h.vf) = %{tl_version}, tex(utfjgbr-v.vf) = %{tl_version}
Provides:       tex(utfjgbs-h.vf) = %{tl_version}, tex(utfjgbs-v.vf) = %{tl_version}
Provides:       tex(utfjgbt-h.vf) = %{tl_version}, tex(utfjgbt-v.vf) = %{tl_version}
Provides:       tex(utfjgbu-h.vf) = %{tl_version}, tex(utfjgbu-v.vf) = %{tl_version}
Provides:       tex(utfjgbv-h.vf) = %{tl_version}, tex(utfjgbv-v.vf) = %{tl_version}
Provides:       tex(utfjgbz-h.vf) = %{tl_version}, tex(utfjgbz-v.vf) = %{tl_version}
Provides:       tex(utfjgej-h.vf) = %{tl_version}, tex(utfjgej-v.vf) = %{tl_version}
Provides:       tex(utfjgek-h.vf) = %{tl_version}, tex(utfjgek-v.vf) = %{tl_version}
Provides:       tex(utfjgel-h.vf) = %{tl_version}, tex(utfjgel-v.vf) = %{tl_version}
Provides:       tex(utfjgem-h.vf) = %{tl_version}, tex(utfjgem-v.vf) = %{tl_version}
Provides:       tex(utfjgen-h.vf) = %{tl_version}, tex(utfjgen-v.vf) = %{tl_version}
Provides:       tex(utfjgeo-h.vf) = %{tl_version}, tex(utfjgeo-v.vf) = %{tl_version}
Provides:       tex(utfjgep-h.vf) = %{tl_version}, tex(utfjgep-v.vf) = %{tl_version}
Provides:       tex(utfjgeq-h.vf) = %{tl_version}, tex(utfjgeq-v.vf) = %{tl_version}
Provides:       tex(utfjger-h.vf) = %{tl_version}, tex(utfjger-v.vf) = %{tl_version}
Provides:       tex(utfjges-h.vf) = %{tl_version}, tex(utfjges-v.vf) = %{tl_version}
Provides:       tex(utfjget-h.vf) = %{tl_version}, tex(utfjget-v.vf) = %{tl_version}
Provides:       tex(utfjgeu-h.vf) = %{tl_version}, tex(utfjgeu-v.vf) = %{tl_version}
Provides:       tex(utfjgev-h.vf) = %{tl_version}, tex(utfjgev-v.vf) = %{tl_version}
Provides:       tex(utfjgez-h.vf) = %{tl_version}, tex(utfjgez-v.vf) = %{tl_version}
Provides:       tex(utfjgrj-h.vf) = %{tl_version}, tex(utfjgrj-v.vf) = %{tl_version}
Provides:       tex(utfjgrk-h.vf) = %{tl_version}, tex(utfjgrk-v.vf) = %{tl_version}
Provides:       tex(utfjgrl-h.vf) = %{tl_version}, tex(utfjgrl-v.vf) = %{tl_version}
Provides:       tex(utfjgrm-h.vf) = %{tl_version}, tex(utfjgrm-v.vf) = %{tl_version}
Provides:       tex(utfjgrn-h.vf) = %{tl_version}, tex(utfjgrn-v.vf) = %{tl_version}
Provides:       tex(utfjgro-h.vf) = %{tl_version}, tex(utfjgro-v.vf) = %{tl_version}
Provides:       tex(utfjgrp-h.vf) = %{tl_version}, tex(utfjgrp-v.vf) = %{tl_version}
Provides:       tex(utfjgrq-h.vf) = %{tl_version}, tex(utfjgrq-v.vf) = %{tl_version}
Provides:       tex(utfjgrr-h.vf) = %{tl_version}, tex(utfjgrr-v.vf) = %{tl_version}
Provides:       tex(utfjgrs-h.vf) = %{tl_version}, tex(utfjgrs-v.vf) = %{tl_version}
Provides:       tex(utfjgrt-h.vf) = %{tl_version}, tex(utfjgrt-v.vf) = %{tl_version}
Provides:       tex(utfjgru-h.vf) = %{tl_version}, tex(utfjgru-v.vf) = %{tl_version}
Provides:       tex(utfjgrv-h.vf) = %{tl_version}, tex(utfjgrv-v.vf) = %{tl_version}
Provides:       tex(utfjgrz-h.vf) = %{tl_version}, tex(utfjgrz-v.vf) = %{tl_version}
Provides:       tex(utfjmbj-h.vf) = %{tl_version}, tex(utfjmbj-v.vf) = %{tl_version}
Provides:       tex(utfjmbk-h.vf) = %{tl_version}, tex(utfjmbk-v.vf) = %{tl_version}
Provides:       tex(utfjmbl-h.vf) = %{tl_version}, tex(utfjmbl-v.vf) = %{tl_version}
Provides:       tex(utfjmbm-h.vf) = %{tl_version}, tex(utfjmbm-v.vf) = %{tl_version}
Provides:       tex(utfjmbn-h.vf) = %{tl_version}, tex(utfjmbn-v.vf) = %{tl_version}
Provides:       tex(utfjmbo-h.vf) = %{tl_version}, tex(utfjmbo-v.vf) = %{tl_version}
Provides:       tex(utfjmbp-h.vf) = %{tl_version}, tex(utfjmbp-v.vf) = %{tl_version}
Provides:       tex(utfjmbq-h.vf) = %{tl_version}, tex(utfjmbq-v.vf) = %{tl_version}
Provides:       tex(utfjmbr-h.vf) = %{tl_version}, tex(utfjmbr-v.vf) = %{tl_version}
Provides:       tex(utfjmbs-h.vf) = %{tl_version}, tex(utfjmbs-v.vf) = %{tl_version}
Provides:       tex(utfjmbt-h.vf) = %{tl_version}, tex(utfjmbt-v.vf) = %{tl_version}
Provides:       tex(utfjmbu-h.vf) = %{tl_version}, tex(utfjmbu-v.vf) = %{tl_version}
Provides:       tex(utfjmbv-h.vf) = %{tl_version}, tex(utfjmbv-v.vf) = %{tl_version}
Provides:       tex(utfjmbz-h.vf) = %{tl_version}, tex(utfjmbz-v.vf) = %{tl_version}
Provides:       tex(utfjmgrj-h.vf) = %{tl_version}, tex(utfjmgrj-v.vf) = %{tl_version}
Provides:       tex(utfjmgrk-h.vf) = %{tl_version}, tex(utfjmgrk-v.vf) = %{tl_version}
Provides:       tex(utfjmgrl-h.vf) = %{tl_version}, tex(utfjmgrl-v.vf) = %{tl_version}
Provides:       tex(utfjmgrm-h.vf) = %{tl_version}, tex(utfjmgrm-v.vf) = %{tl_version}
Provides:       tex(utfjmgrn-h.vf) = %{tl_version}, tex(utfjmgrn-v.vf) = %{tl_version}
Provides:       tex(utfjmgro-h.vf) = %{tl_version}, tex(utfjmgro-v.vf) = %{tl_version}
Provides:       tex(utfjmgrp-h.vf) = %{tl_version}, tex(utfjmgrp-v.vf) = %{tl_version}
Provides:       tex(utfjmgrq-h.vf) = %{tl_version}, tex(utfjmgrq-v.vf) = %{tl_version}
Provides:       tex(utfjmgrr-h.vf) = %{tl_version}, tex(utfjmgrr-v.vf) = %{tl_version}
Provides:       tex(utfjmgrs-h.vf) = %{tl_version}, tex(utfjmgrs-v.vf) = %{tl_version}
Provides:       tex(utfjmgrt-h.vf) = %{tl_version}, tex(utfjmgrt-v.vf) = %{tl_version}
Provides:       tex(utfjmgru-h.vf) = %{tl_version}, tex(utfjmgru-v.vf) = %{tl_version}
Provides:       tex(utfjmgrv-h.vf) = %{tl_version}, tex(utfjmgrv-v.vf) = %{tl_version}
Provides:       tex(utfjmgrz-h.vf) = %{tl_version}, tex(utfjmgrz-v.vf) = %{tl_version}
Provides:       tex(utfjmlj-h.vf) = %{tl_version}, tex(utfjmlj-v.vf) = %{tl_version}
Provides:       tex(utfjmlk-h.vf) = %{tl_version}, tex(utfjmlk-v.vf) = %{tl_version}
Provides:       tex(utfjmll-h.vf) = %{tl_version}, tex(utfjmll-v.vf) = %{tl_version}
Provides:       tex(utfjmlm-h.vf) = %{tl_version}, tex(utfjmlm-v.vf) = %{tl_version}
Provides:       tex(utfjmln-h.vf) = %{tl_version}, tex(utfjmln-v.vf) = %{tl_version}
Provides:       tex(utfjmlo-h.vf) = %{tl_version}, tex(utfjmlo-v.vf) = %{tl_version}
Provides:       tex(utfjmlp-h.vf) = %{tl_version}, tex(utfjmlp-v.vf) = %{tl_version}
Provides:       tex(utfjmlq-h.vf) = %{tl_version}, tex(utfjmlq-v.vf) = %{tl_version}
Provides:       tex(utfjmlr-h.vf) = %{tl_version}, tex(utfjmlr-v.vf) = %{tl_version}
Provides:       tex(utfjmls-h.vf) = %{tl_version}, tex(utfjmls-v.vf) = %{tl_version}
Provides:       tex(utfjmlt-h.vf) = %{tl_version}, tex(utfjmlt-v.vf) = %{tl_version}
Provides:       tex(utfjmlu-h.vf) = %{tl_version}, tex(utfjmlu-v.vf) = %{tl_version}
Provides:       tex(utfjmlv-h.vf) = %{tl_version}, tex(utfjmlv-v.vf) = %{tl_version}
Provides:       tex(utfjmlz-h.vf) = %{tl_version}, tex(utfjmlz-v.vf) = %{tl_version}
Provides:       tex(utfjmrj-h.vf) = %{tl_version}, tex(utfjmrj-v.vf) = %{tl_version}
Provides:       tex(utfjmrk-h.vf) = %{tl_version}, tex(utfjmrk-v.vf) = %{tl_version}
Provides:       tex(utfjmrl-h.vf) = %{tl_version}, tex(utfjmrl-v.vf) = %{tl_version}
Provides:       tex(utfjmrm-h.vf) = %{tl_version}, tex(utfjmrm-v.vf) = %{tl_version}
Provides:       tex(utfjmrn-h.vf) = %{tl_version}, tex(utfjmrn-v.vf) = %{tl_version}
Provides:       tex(utfjmro-h.vf) = %{tl_version}, tex(utfjmro-v.vf) = %{tl_version}
Provides:       tex(utfjmrp-h.vf) = %{tl_version}, tex(utfjmrp-v.vf) = %{tl_version}
Provides:       tex(utfjmrq-h.vf) = %{tl_version}, tex(utfjmrq-v.vf) = %{tl_version}
Provides:       tex(utfjmrr-h.vf) = %{tl_version}, tex(utfjmrr-v.vf) = %{tl_version}
Provides:       tex(utfjmrs-h.vf) = %{tl_version}, tex(utfjmrs-v.vf) = %{tl_version}
Provides:       tex(utfjmrt-h.vf) = %{tl_version}, tex(utfjmrt-v.vf) = %{tl_version}
Provides:       tex(utfjmru-h.vf) = %{tl_version}, tex(utfjmru-v.vf) = %{tl_version}
Provides:       tex(utfjmrv-h.vf) = %{tl_version}, tex(utfjmrv-v.vf) = %{tl_version}
Provides:       tex(utfjmrz-h.vf) = %{tl_version}, tex(utfjmrz-v.vf) = %{tl_version}
Provides:       tex(utfmrj-h.vf) = %{tl_version}, tex(utfmrj-v.vf) = %{tl_version}
Provides:       tex(utfmrk-h.vf) = %{tl_version}, tex(utfmrk-v.vf) = %{tl_version}
Provides:       tex(utfmrl-h.vf) = %{tl_version}, tex(utfmrl-v.vf) = %{tl_version}
Provides:       tex(utfmrm-h.vf) = %{tl_version}, tex(utfmrm-v.vf) = %{tl_version}
Provides:       tex(utfmrn-h.vf) = %{tl_version}, tex(utfmrn-v.vf) = %{tl_version}
Provides:       tex(utfmro-h.vf) = %{tl_version}, tex(utfmro-v.vf) = %{tl_version}
Provides:       tex(utfmrp-h.vf) = %{tl_version}, tex(utfmrp-v.vf) = %{tl_version}
Provides:       tex(utfmrq-h.vf) = %{tl_version}, tex(utfmrq-v.vf) = %{tl_version}
Provides:       tex(utfmrr-h.vf) = %{tl_version}, tex(utfmrr-v.vf) = %{tl_version}
Provides:       tex(utfmrs-h.vf) = %{tl_version}, tex(utfmrs-v.vf) = %{tl_version}
Provides:       tex(utfmrt-h.vf) = %{tl_version}, tex(utfmrt-v.vf) = %{tl_version}
Provides:       tex(utfmru-h.vf) = %{tl_version}, tex(utfmru-v.vf) = %{tl_version}
Provides:       tex(utfmrv-h.vf) = %{tl_version}, tex(utfmrv-v.vf) = %{tl_version}
Provides:       tex(utfmrz-h.vf) = %{tl_version}, tex(utfmrz-v.vf) = %{tl_version}
Provides:       tex(utftgrk-h.vf) = %{tl_version}, tex(utftgrk-v.vf) = %{tl_version}
Provides:       tex(utftgrl-h.vf) = %{tl_version}, tex(utftgrl-v.vf) = %{tl_version}
Provides:       tex(utftgrm-h.vf) = %{tl_version}, tex(utftgrm-v.vf) = %{tl_version}
Provides:       tex(utftgrn-h.vf) = %{tl_version}, tex(utftgrn-v.vf) = %{tl_version}
Provides:       tex(utftgro-h.vf) = %{tl_version}, tex(utftgro-v.vf) = %{tl_version}
Provides:       tex(utftgrp-h.vf) = %{tl_version}, tex(utftgrp-v.vf) = %{tl_version}
Provides:       tex(utftgrq-h.vf) = %{tl_version}, tex(utftgrq-v.vf) = %{tl_version}
Provides:       tex(utftgrr-h.vf) = %{tl_version}, tex(utftgrr-v.vf) = %{tl_version}
Provides:       tex(utftgrs-h.vf) = %{tl_version}, tex(utftgrs-v.vf) = %{tl_version}
Provides:       tex(utftgrt-h.vf) = %{tl_version}, tex(utftgrt-v.vf) = %{tl_version}
Provides:       tex(utftgru-h.vf) = %{tl_version}, tex(utftgru-v.vf) = %{tl_version}
Provides:       tex(utftgrz-h.vf) = %{tl_version}, tex(utftgrz-v.vf) = %{tl_version}
Provides:       tex(utftmrk-h.vf) = %{tl_version}, tex(utftmrk-v.vf) = %{tl_version}
Provides:       tex(utftmrl-h.vf) = %{tl_version}, tex(utftmrl-v.vf) = %{tl_version}
Provides:       tex(utftmrm-h.vf) = %{tl_version}, tex(utftmrm-v.vf) = %{tl_version}
Provides:       tex(utftmrn-h.vf) = %{tl_version}, tex(utftmrn-v.vf) = %{tl_version}
Provides:       tex(utftmro-h.vf) = %{tl_version}, tex(utftmro-v.vf) = %{tl_version}
Provides:       tex(utftmrp-h.vf) = %{tl_version}, tex(utftmrp-v.vf) = %{tl_version}
Provides:       tex(utftmrq-h.vf) = %{tl_version}, tex(utftmrq-v.vf) = %{tl_version}
Provides:       tex(utftmrr-h.vf) = %{tl_version}, tex(utftmrr-v.vf) = %{tl_version}
Provides:       tex(utftmrs-h.vf) = %{tl_version}, tex(utftmrs-v.vf) = %{tl_version}
Provides:       tex(utftmrt-h.vf) = %{tl_version}, tex(utftmrt-v.vf) = %{tl_version}
Provides:       tex(utftmru-h.vf) = %{tl_version}, tex(utftmru-v.vf) = %{tl_version}
Provides:       tex(utftmrz-h.vf) = %{tl_version}, tex(utftmrz-v.vf) = %{tl_version}
Provides:       tex(mlutf.sty) = %{tl_version}, tex(otf.sty) = %{tl_version}

%description -n texlive-japanese-otf-uptex
The bundle offers support of the fonts in the japanese-otf
package, for use with the UpTeX distribution (version 0.20 or
later).

%package -n texlive-japanese-otf-uptex-doc
Summary:        Documentation for japanese-otf-uptex
Version:        svn47702
Provides:       tex-japanese-otf-uptex-doc
AutoReqProv:    No
Requires:       tex-japanese-otf-doc

%description -n texlive-japanese-otf-uptex-doc
Documentation for japanese-otf-uptex

%package -n texlive-jsclasses
Provides:       tex-jsclasses = %{tl_version}
License:        BSD
Summary:        Classes tailored for use with Japanese
Version:        svn48078
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(jsarticle.cls) = %{tl_version}, tex(jsbook.cls) = %{tl_version}
Provides:       tex(jspf.cls) = %{tl_version}, tex(jsverb.sty) = %{tl_version}
Provides:       tex(kiyou.cls) = %{tl_version}, tex(minijs.sty) = %{tl_version}
Provides:       tex(okumacro.sty) = %{tl_version}, tex(okuverb.sty) = %{tl_version}

%description -n texlive-jsclasses
Classes jsarticle and jsbook are provided, together with
packages okumacro and okuverb. These classes are
designed to work under ASCII Corporation's Japanese TeX system
ptex.

%package -n texlive-jsclasses-doc
Summary:        Documentation for jsclasses
Version:        svn48078
Provides:       tex-jsclasses-doc
AutoReqProv:    No

%description -n texlive-jsclasses-doc
Documentation for jsclasses

%package -n texlive-kotex-oblivoir
Provides:       tex-kotex-oblivoir = %{tl_version}
License:        LPPL 1.3
Summary:        A LaTeX document class for typesetting Korean documents
Version:        svn43130
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-memoir, tex-kotex-utf, tex(xparse.sty), tex(hologo.sty)
Requires:       tex(dhucs.sty), tex(memhfixc.sty), tex(hyperref.sty), tex(memucs-setspace.sty)
Requires:       tex(xkeyval.sty), tex(fontenc.sty), tex(polyglossia.sty), tex(luatexko.sty)
Requires:       tex(xob-dotemph.sty), tex(cjkutf8-ko.sty)
Requires:       tex(ifluatex.sty), tex(ifxetex.sty), tex(xetexko-space.sty), tex(xetexko-josa.sty)
Requires:       tex(xetexko-vertical.sty), tex(kolabels-utf.sty)
Requires:       tex(konames-utf.sty), tex(amssymb.sty), tex(fontspec.sty), tex(kotex.sty)
Requires:       tex(xetexko-font.sty), tex(paralist.sty)
Requires:       tex(iftex.sty), tex(dhucs-paralist.sty), tex(moreverb.sty), tex(amsmath.sty)
Requires:       tex(dhucs-cmap.sty), tex(microtype.sty), tex(type1cm.sty), tex(type1ec.sty)
Requires:       tex(enumerate.sty)
Provides:       tex(10_5.sty) = %{tl_version}, tex(fapapersize.sty) = %{tl_version}
Provides:       tex(hfontsel.sty) = %{tl_version}, tex(memhangul-common.sty) = %{tl_version}
Provides:       tex(memhangul-patch.sty) = %{tl_version}
Provides:       tex(memhangul-ucs.sty) = %{tl_version}, tex(memucs-enumerate.sty) = %{tl_version}
Provides:       tex(memucs-gremph.sty) = %{tl_version}, tex(memucs-interword.sty) = %{tl_version}
Provides:       tex(memucs-setspace.sty) = %{tl_version}
Provides:       tex(nanumfontsel.sty) = %{tl_version}, tex(ob-koreanappendix.sty) = %{tl_version}
Provides:       tex(ob-nokoreanappendix.sty) = %{tl_version}
Provides:       tex(ob-toclof.sty) = %{tl_version}, tex(memhangul-x.sty) = %{tl_version}
Provides:       tex(memucs-interword-x.sty) = %{tl_version}
Provides:       tex(xetexko-var.sty) = %{tl_version}, tex(xob-amssymb.sty) = %{tl_version}
Provides:       tex(xob-dotemph.sty) = %{tl_version}, tex(xob-font.sty) = %{tl_version}
Provides:       tex(xob-hyper.sty) = %{tl_version}, tex(xob-paralist.sty) = %{tl_version}
Provides:       tex(oblivoir-base.cls) = %{tl_version}, tex(oblivoir-xlua.cls) = %{tl_version}
Provides:       tex(oblivoir.cls) = %{tl_version}, tex(xoblivoir.cls) = %{tl_version}

%description -n texlive-kotex-oblivoir
The class is based on memoir, and is adapted to typesetting
Korean documents. The bundle (of class and associated packages)
belongs to the ko.TeX bundle.

%package -n texlive-kotex-oblivoir-doc
Summary:        Documentation for kotex-oblivoir
Version:        svn43130
Provides:       tex-kotex-oblivoir-doc
AutoReqProv:    No
Requires:       tex-memoir-doc, tex-kotex-utf-doc

%description -n texlive-kotex-oblivoir-doc
Documentation for kotex-oblivoir

%package -n texlive-kotex-utf
Provides:       tex-kotex-utf = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset Hangul, coded in UTF-8
Version:        svn38558

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-cjk-ko, tex(ifpdf.sty), tex(enumerate.sty), tex(enumitem.sty)
Requires:       tex(xkeyval.sty), tex(verbatim.sty), tex(paralist.sty), tex(sectsty.sty)
Requires:       tex(setspace.sty), tex(hyperref.sty), tex(hologo.sty), tex(varioref.sty)
Requires:       tex(fontenc.sty), tex(luatexko.sty), tex(xetexko.sty), tex(konames-utf.sty)
Requires:       tex(inputenc.sty), tex(kolabels-utf.sty)
Requires:       tex(kotexutf-core.tex)
Provides:       tex(dhucs-cmap.sty) = %{tl_version}, tex(dhucs-enumerate.sty) = %{tl_version}
Provides:       tex(dhucs-enumitem.sty) = %{tl_version}, tex(dhucs-gremph.sty) = %{tl_version}
Provides:       tex(dhucs-interword.sty) = %{tl_version}
Provides:       tex(dhucs-paralist.sty) = %{tl_version}, tex(dhucs-sectsty.sty) = %{tl_version}
Provides:       tex(dhucs-setspace.sty) = %{tl_version}, tex(dhucs-trivcj.sty) = %{tl_version}
Provides:       tex(dhucs-ucshyper.sty) = %{tl_version}, tex(dhucsfn.sty) = %{tl_version}
Provides:       tex(kotex-logo.sty) = %{tl_version}, tex(kotex-varioref.sty) = %{tl_version}
Provides:       tex(dhucs-nanumfont.sty) = %{tl_version}
Provides:       tex(dhucs.sty) = %{tl_version}, tex(kosections-utf.sty) = %{tl_version}
Provides:       tex(kotex.cfg) = %{tl_version}, tex(kotexutf.sty) = %{tl_version}
Provides:       tex(lucuhcmj.fd) = %{tl_version}, tex(dhucs.cfg) = %{tl_version}

%description -n texlive-kotex-utf
The package typesets Hangul, which is the native alphabet of
the Korean language; input Korean text should be encoded in UTF-
8. The bundle (of class and associated packages) belongs to the
ko.TeX bundle.

%package -n texlive-kotex-utf-doc
Summary:        Documentation for kotex-utf
Version:        svn38558

Provides:       tex-kotex-utf-doc
AutoReqProv:    No
Requires:       tex-cjk-ko-doc

%description -n texlive-kotex-utf-doc
Documentation for kotex-utf

%package -n texlive-kotex-plain
Provides:       tex-kotex-plain = %{tl_version}
License:        LPPL 1.3
Summary:        Macros for typesetting Korean under Plain TeX
Version:        svn38630

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hangulcweb.tex) = %{tl_version}, tex(kotexplain.tex) = %{tl_version}
Provides:       tex(kotexutf-core.tex) = %{tl_version}, tex(kotexutf.tex) = %{tl_version}

%description -n texlive-kotex-plain
The package provides macros for typesetting Hangul, the native
alphabet of the Korean language, using plain *TeX. Input Korean
text should be encoded in UTF-8. The package is belongs to the
ko.TeX bundle.

%package -n texlive-kotex-plain-doc
Summary:        Documentation for kotex-plain
Version:        svn38630

Provides:       tex-kotex-plain-doc
AutoReqProv:    No

%description -n texlive-kotex-plain-doc
Documentation for kotex-plain

%package -n texlive-jknapltx
Provides:       tex-jknapltx = %{tl_version}
License:        GPL+
Summary:        Miscellaneous packages by Joerg Knappen
Version:        svn19440.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(textcomp.sty)
Provides:       tex(greekctr.sty) = %{tl_version}, tex(holtpolt.sty) = %{tl_version}
Provides:       tex(latin1jk.def) = %{tl_version}, tex(latin2jk.def) = %{tl_version}
Provides:       tex(latin3jk.def) = %{tl_version}, tex(mathbbol.sty) = %{tl_version}
Provides:       tex(mathrsfs.sty) = %{tl_version}, tex(parboxx.sty) = %{tl_version}
Provides:       tex(sans.sty) = %{tl_version}, tex(semtrans.sty) = %{tl_version}
Provides:       tex(sgmlcmpt.sty) = %{tl_version}, tex(smartmn.sty) = %{tl_version}
Provides:       tex(tccompat.sty) = %{tl_version}, tex(ursfs.fd) = %{tl_version}
Provides:       tex(ustmary.fd) = %{tl_version}, tex(young.sty) = %{tl_version}

%description -n texlive-jknapltx
Miscellaneous macros by Jorg Knappen, including: represent
counters in greek; Maxwell's non-commutative division;
latin1jk, latin2jk and latin3jk, which are their inputenc
definition files that allow verbatim input in the respective
ISO Latin codes; blackboard bold fonts in maths; use of RSFS
fonts in maths; extra alignments for \parboxes; swap Roman and
Sans fonts; transliterate semitic languages; patches to make
(La)TeX formulae embeddable in SGML; use maths "minus" in text
as appropriate; simple Young tableaux.

%package -n texlive-jknapltx-doc
Summary:        Documentation for jknapltx
Version:        svn19440.0

Provides:       tex-jknapltx-doc
AutoReqProv:    No

%description -n texlive-jknapltx-doc
Documentation for jknapltx

%package -n texlive-koma-script
Provides:       tex-koma-script = %{tl_version}
License:        LPPL 1.3
Summary:        A bundle of versatile classes and packages
Version:        svn47249
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(inputenc.sty), tex(fontenc.sty), tex(babelbib.sty), tex(afterpage.sty)
Requires:       tex(makeidx.sty), tex(scrtime.sty), tex(picture.sty), tex(graphicx.sty)
Requires:       tex(booktabs.sty), tex(longtable.sty), tex(amsmath.sty), tex(listings.sty)
Requires:       tex(multicol.sty), tex(marginnote.sty), tex(tabularx.sty), tex(xcolor.sty)
Requires:       tex(hyperref.sty), tex(bookmark.sty), tex(mparhack.sty), tex(geometry.sty)
Requires:       tex(textcomp.sty), tex(tocbasic.sty), tex(keyval.sty), tex(etoolbox.sty)
Requires:       tex(marvosym.sty)
Provides:       tex(komabug.tex) = %{tl_version}, tex(adrconvnote.tex) = %{tl_version}
Provides:       tex(authorpart.tex) = %{tl_version}, tex(common-0.tex) = %{tl_version}
Provides:       tex(common-1.tex) = %{tl_version}, tex(common-12.tex) = %{tl_version}
Provides:       tex(common-13.tex) = %{tl_version}, tex(common-14.tex) = %{tl_version}
Provides:       tex(common-15.tex) = %{tl_version}, tex(common-2.tex) = %{tl_version}
Provides:       tex(common-20.tex) = %{tl_version}, tex(common-21.tex) = %{tl_version}
Provides:       tex(common-3.tex) = %{tl_version}, tex(common-4.tex) = %{tl_version}
Provides:       tex(common-5.tex) = %{tl_version}, tex(common-6.tex) = %{tl_version}
Provides:       tex(common-7.tex) = %{tl_version}, tex(common-8.tex) = %{tl_version}
Provides:       tex(common-9.tex) = %{tl_version}, tex(expertpart.tex) = %{tl_version}
Provides:       tex(guide-english.tex) = %{tl_version}, tex(guide.tex) = %{tl_version}
Provides:       tex(introduction.tex) = %{tl_version}, tex(japanlco.tex) = %{tl_version}
Provides:       tex(linkalias.tex) = %{tl_version}, tex(preface.tex) = %{tl_version}
Provides:       tex(scraddr.tex) = %{tl_version}, tex(scrbase.tex) = %{tl_version}
Provides:       tex(scrbookreportarticle-experts.tex) = %{tl_version}
Provides:       tex(scrbookreportarticle.tex) = %{tl_version}
Provides:       tex(scrdatetime.tex) = %{tl_version}, tex(scrextend.tex) = %{tl_version}
Provides:       tex(scrhack.tex) = %{tl_version}, tex(scrjura.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn-example.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn.tex) = %{tl_version}
Provides:       tex(scrlayer-scrpage-experts.tex) = %{tl_version}
Provides:       tex(scrlayer-scrpage.tex) = %{tl_version}
Provides:       tex(scrlayer.tex) = %{tl_version}, tex(scrlfile.tex) = %{tl_version}
Provides:       tex(scrlttr2-experts.tex) = %{tl_version}
Provides:       tex(scrlttr2.tex) = %{tl_version}, tex(scrwfile.tex) = %{tl_version}
Provides:       tex(tocbasic.tex) = %{tl_version}, tex(typearea-experts.tex) = %{tl_version}
Provides:       tex(typearea.tex) = %{tl_version}, tex(guide.tex) = %{tl_version}
Provides:       tex(linkalias.tex) = %{tl_version}, tex(adrconvnote.tex) = %{tl_version}
Provides:       tex(authorpart.tex) = %{tl_version}, tex(common-0.tex) = %{tl_version}
Provides:       tex(common-1.tex) = %{tl_version}, tex(common-12.tex) = %{tl_version}
Provides:       tex(common-13.tex) = %{tl_version}, tex(common-14.tex) = %{tl_version}
Provides:       tex(common-15.tex) = %{tl_version}, tex(common-2.tex) = %{tl_version}
Provides:       tex(common-20.tex) = %{tl_version}, tex(common-21.tex) = %{tl_version}
Provides:       tex(common-3.tex) = %{tl_version}, tex(common-4.tex) = %{tl_version}
Provides:       tex(common-5.tex) = %{tl_version}, tex(common-6.tex) = %{tl_version}
Provides:       tex(common-7.tex) = %{tl_version}, tex(common-8.tex) = %{tl_version}
Provides:       tex(common-9.tex) = %{tl_version}, tex(expertpart.tex) = %{tl_version}
Provides:       tex(guide-ngerman.tex) = %{tl_version}, tex(guide.tex) = %{tl_version}
Provides:       tex(introduction.tex) = %{tl_version}, tex(linkalias.tex) = %{tl_version}
Provides:       tex(preface.tex) = %{tl_version}, tex(scraddr.tex) = %{tl_version}
Provides:       tex(scrbase.tex) = %{tl_version}, tex(scrbookreportarticle-experts.tex) = %{tl_version}
Provides:       tex(scrbookreportarticle.tex) = %{tl_version}
Provides:       tex(scrdatetime.tex) = %{tl_version}, tex(scrextend.tex) = %{tl_version}
Provides:       tex(scrhack.tex) = %{tl_version}, tex(scrjura.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn-example.tex) = %{tl_version}
Provides:       tex(scrlayer-notecolumn.tex) = %{tl_version}
Provides:       tex(scrlayer-scrpage-experts.tex) = %{tl_version}
Provides:       tex(scrlayer-scrpage.tex) = %{tl_version}
Provides:       tex(scrlayer.tex) = %{tl_version}, tex(scrlfile.tex) = %{tl_version}
Provides:       tex(scrlttr2-experts.tex) = %{tl_version}
Provides:       tex(scrlttr2.tex) = %{tl_version}, tex(scrwfile.tex) = %{tl_version}
Provides:       tex(tocbasic.tex) = %{tl_version}, tex(typearea-experts.tex) = %{tl_version}
Provides:       tex(typearea.tex) = %{tl_version}, tex(scrguide.cls) = %{tl_version}
Provides:       tex(scrpage2.tex) = %{tl_version}, tex(scrdocstrip.tex) = %{tl_version}
Provides:       tex(scrsource.tex) = %{tl_version}, tex(scraddr.sty) = %{tl_version}
Provides:       tex(scrartcl.cls) = %{tl_version}, tex(scrbase.sty) = %{tl_version}
Provides:       tex(scrbook.cls) = %{tl_version}, tex(scrdate.sty) = %{tl_version}
Provides:       tex(scrdoc.cls) = %{tl_version}, tex(scrextend.sty) = %{tl_version}
Provides:       tex(scrfontsizes.sty) = %{tl_version}, tex(scrhack.sty) = %{tl_version}
Provides:       tex(scrjura.sty) = %{tl_version}, tex(scrkbase.sty) = %{tl_version}
Provides:       tex(scrlayer-notecolumn.sty) = %{tl_version}
Provides:       tex(scrlayer-scrpage.sty) = %{tl_version}
Provides:       tex(scrlayer.sty) = %{tl_version}, tex(scrletter.sty) = %{tl_version}
Provides:       tex(scrlfile.sty) = %{tl_version}, tex(scrlttr2.cls) = %{tl_version}
Provides:       tex(scrpage2.sty) = %{tl_version}, tex(scrreprt.cls) = %{tl_version}
Provides:       tex(scrsize10pt.clo) = %{tl_version}, tex(scrsize11pt.clo) = %{tl_version}
Provides:       tex(scrsize12pt.clo) = %{tl_version}, tex(scrtime.sty) = %{tl_version}
Provides:       tex(scrwfile.sty) = %{tl_version}, tex(tocbasic.sty) = %{tl_version}
Provides:       tex(tocstyle.sty) = %{tl_version}, tex(typearea.sty) = %{tl_version}

%description -n texlive-koma-script
The KOMA-Script bundle provides replacements for the article,
report, and book classes with emphasis on typography and
versatility. There is also a letter class. The bundle also
offers: a package for calculating type areas in the way laid
down by the typographer Jan Tschichold, a package for easily
changing and defining page styles, a package scrdate for
getting not only the current date but also the name of the day,
and a package scrtime for getting the current time. All these
packages may be used not only with KOMA-Script classes but also
with the standard classes. Since every package has its own
version number, the version number quoted only refers to the
version of scrbook, scrreprt, scrartcl, scrlttr2 and typearea
(which are the main parts of the bundle).

%package -n texlive-koma-script-examples-doc
Summary:        Documentation for koma-script-examples
Version:        svn34243.0

Provides:       tex-koma-script-examples-doc
AutoReqProv:    No

%description -n texlive-koma-script-examples-doc
Documentation for koma-script-examples

%package -n texlive-knitting
Provides:       tex-knitting = %{tl_version}
License:        LPPL 1.3
Summary:        Produce knitting charts, in Plain TeX or LaTeX
Version:        svn19595.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(color.sty)
Provides:       tex(knitfont.map) = %{tl_version}, tex(knitg_sc_in.tfm) = %{tl_version}
Provides:       tex(knitg_sc_out.tfm) = %{tl_version}, tex(knitgg.tfm) = %{tl_version}
Provides:       tex(knitgn.tfm) = %{tl_version}, tex(knitgp.tfm) = %{tl_version}
Provides:       tex(knitn_sc_in.tfm) = %{tl_version}, tex(knitn_sc_out.tfm) = %{tl_version}
Provides:       tex(knitnl.tfm) = %{tl_version}, tex(knitnn.tfm) = %{tl_version}
Provides:       tex(knitnp.tfm) = %{tl_version}, tex(knitnr.tfm) = %{tl_version}
Provides:       tex(knitw_sc_in.tfm) = %{tl_version}, tex(knitw_sc_out.tfm) = %{tl_version}
Provides:       tex(knitwg.tfm) = %{tl_version}, tex(knitwn.tfm) = %{tl_version}
Provides:       tex(knitwp.tfm) = %{tl_version}, tex(knitg_sc_in.pfb) = %{tl_version}
Provides:       tex(knitg_sc_out.pfb) = %{tl_version}, tex(knitgg.pfb) = %{tl_version}
Provides:       tex(knitgn.pfb) = %{tl_version}, tex(knitgp.pfb) = %{tl_version}
Provides:       tex(knitn_sc_in.pfb) = %{tl_version}, tex(knitn_sc_out.pfb) = %{tl_version}
Provides:       tex(knitnl.pfb) = %{tl_version}, tex(knitnn.pfb) = %{tl_version}
Provides:       tex(knitnp.pfb) = %{tl_version}, tex(knitnr.pfb) = %{tl_version}
Provides:       tex(knitw_sc_in.pfb) = %{tl_version}, tex(knitw_sc_out.pfb) = %{tl_version}
Provides:       tex(knitwg.pfb) = %{tl_version}, tex(knitwn.pfb) = %{tl_version}
Provides:       tex(knitwp.pfb) = %{tl_version}, tex(knitting.sty) = %{tl_version}
Provides:       tex(uknit.fd) = %{tl_version}, tex(knitting.tex) = %{tl_version}

%description -n texlive-knitting
The package provides symbol fonts and commands to write charted
instructions for cable and lace knitting patterns, using either
plain TeX or LaTeX. The fonts are available both as Metafont
source and in Adobe Type 1 format.

%package -n texlive-knitting-doc
Summary:        Documentation for knitting
Version:        svn19595.2.0

Provides:       tex-knitting-doc
AutoReqProv:    No

%description -n texlive-knitting-doc
Documentation for knitting

%package -n texlive-knittingpattern
Provides:       tex-knittingpattern = %{tl_version}
License:        LPPL 1.3
Summary:        Create knitting patterns
Version:        svn17205.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(float.sty), tex(fancyhdr.sty), tex(longtable.sty)
Requires:       tex(calc.sty), tex(xcolor.sty)
Provides:       tex(knittingpattern.cls) = %{tl_version}

%description -n texlive-knittingpattern
The class provides a simple, effective method for knitters to
produce high-quality, attractive patterns using LaTeX. It does
this by providing commands to handle as much of the layout of
the document as possible, leaving the author free to
concentrate on the pattern.

%package -n texlive-knittingpattern-doc
Summary:        Documentation for knittingpattern
Version:        svn17205.0

Provides:       tex-knittingpattern-doc
AutoReqProv:    No

%description -n texlive-knittingpattern-doc
Documentation for knittingpattern

%package -n texlive-iso
Provides:       tex-iso = %{tl_version}
License:        LPPL
Summary:        Generic ISO standards typesetting macros
Version:        svn15878.2.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(url.sty)
Provides:       tex(askincv1.sty) = %{tl_version}, tex(iso10.clo) = %{tl_version}
Provides:       tex(iso11.clo) = %{tl_version}, tex(iso9.clo) = %{tl_version}
Provides:       tex(isov2.cls) = %{tl_version}

%description -n texlive-iso
Generic class and package files for typesetting ISO
International Standard documents. Several standard documents
have been printed by ISO from camera-ready copy prepared using
LaTeX and these files. The class makes use of the isorot
package, rather than use other mechanisms directly.

%package -n texlive-isomath
Provides:       tex-isomath = %{tl_version}
License:        LPPL
Summary:        Mathematics style for science and technology
Version:        svn27654.0.6.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fixmath.sty), tex(kvoptions.sty)
Provides:       tex(isomath.sty) = %{tl_version}

%description -n texlive-isomath
The package provides tools for a mathematical style that
conforms to the International Standard ISO 80000-2 and is
common in science and technology. It changes the default shape
of capital Greek letters to italic, sets up bold italic and
sans-serif bold italic math alphabets with Latin and Greek
characters, and defines macros for markup of vector, matrix and
tensor symbols.

%package -n texlive-isomath-doc
Summary:        Documentation for isomath
Version:        svn27654.0.6.1

Provides:       tex-isomath-doc
AutoReqProv:    No

%description -n texlive-isomath-doc
Documentation for isomath

%package -n texlive-iso-doc
Summary:        Documentation for iso
Version:        svn15878.2.4

Provides:       tex-iso-doc
AutoReqProv:    No

%description -n texlive-iso-doc
Documentation for iso

%package -n texlive-iso10303
Provides:       tex-iso10303 = %{tl_version}
License:        LPPL
Summary:        Typesetting the STEP standards
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(aicv1.sty) = %{tl_version}, tex(apendint.tex) = %{tl_version}
Provides:       tex(apmpspec.tex) = %{tl_version}, tex(apmptbl.tex) = %{tl_version}
Provides:       tex(apmptempl.tex) = %{tl_version}, tex(apsstempl.tex) = %{tl_version}
Provides:       tex(apv12.sty) = %{tl_version}, tex(atsv11.sty) = %{tl_version}
Provides:       tex(bpfap1.tex) = %{tl_version}, tex(bpfap10.tex) = %{tl_version}
Provides:       tex(bpfap11.tex) = %{tl_version}, tex(bpfap12.tex) = %{tl_version}
Provides:       tex(bpfap13.tex) = %{tl_version}, tex(bpfap14.tex) = %{tl_version}
Provides:       tex(bpfap15.tex) = %{tl_version}, tex(bpfap16.tex) = %{tl_version}
Provides:       tex(bpfap2.tex) = %{tl_version}, tex(bpfap3.tex) = %{tl_version}
Provides:       tex(bpfap4.tex) = %{tl_version}, tex(bpfap5.tex) = %{tl_version}
Provides:       tex(bpfap6.tex) = %{tl_version}, tex(bpfap7.tex) = %{tl_version}
Provides:       tex(bpfap8.tex) = %{tl_version}, tex(bpfap9.tex) = %{tl_version}
Provides:       tex(bpfats1.tex) = %{tl_version}, tex(bpfats10.tex) = %{tl_version}
Provides:       tex(bpfats11.tex) = %{tl_version}, tex(bpfats12.tex) = %{tl_version}
Provides:       tex(bpfats14.tex) = %{tl_version}, tex(bpfats2.tex) = %{tl_version}
Provides:       tex(bpfats3.tex) = %{tl_version}, tex(bpfats4.tex) = %{tl_version}
Provides:       tex(bpfats5.tex) = %{tl_version}, tex(bpfats6.tex) = %{tl_version}
Provides:       tex(bpfats7.tex) = %{tl_version}, tex(bpfats8.tex) = %{tl_version}
Provides:       tex(bpfats9.tex) = %{tl_version}, tex(bpfir1.tex) = %{tl_version}
Provides:       tex(bpfir2.tex) = %{tl_version}, tex(bpfir3.tex) = %{tl_version}
Provides:       tex(bpfs1.tex) = %{tl_version}, tex(bpfs2.tex) = %{tl_version}
Provides:       tex(bpfs3.tex) = %{tl_version}, tex(irv12.sty) = %{tl_version}
Provides:       tex(stepman.tex) = %{tl_version}, tex(stepv13.sty) = %{tl_version}
Provides:       tex(stppdlst.tex) = %{tl_version}

%description -n texlive-iso10303
Class and package files building on iso for typesetting the ISO
10303 (STEP) standards. Standard documents prepared using these
packages have been published by ISO.

%package -n texlive-iso10303-doc
Summary:        Documentation for iso10303
Version:        svn15878.1.5

Provides:       tex-iso10303-doc
AutoReqProv:    No

%description -n texlive-iso10303-doc
Documentation for iso10303

%package -n texlive-isodate
Provides:       tex-isodate = %{tl_version}
License:        LPPL
Summary:        Tune the output format of dates according to language
Version:        svn16613.2.28

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(substr.sty), tex(calc.sty)
Provides:       tex(isodate.sty) = %{tl_version}, tex(isodateo.sty) = %{tl_version}

%description -n texlive-isodate
This package provides ten output formats of the commands
\today, \printdate, \printdateTeX, and \daterange (partly
language dependent). Formats available are: ISO (yyyy-mm-dd),
numeric (e.g. dd.\,mm.~yyyy), short (e.g. dd.\,mm.\,yy), TeX
(yyyy/mm/dd), original (e.g. dd. mmm yyyy), short original
(e.g. dd. mmm yy), as well as numerical formats with Roman
numerals for the month. The commands \printdate and
\printdateTeX print any date. The command \daterange prints a
date range and leaves out unnecessary year or month entries.
This package supports German (old and new rules), Austrian, US
English, British English, French, Danish, Swedish, and
Norwegian.

%package -n texlive-isodate-doc
Summary:        Documentation for isodate
Version:        svn16613.2.28

Provides:       tex-isodate-doc
AutoReqProv:    No

%description -n texlive-isodate-doc
Documentation for isodate

%package -n texlive-isodoc
Provides:       tex-isodoc = %{tl_version}
License:        LPPL 1.3
Summary:        A LaTeX class for typesetting letters and invoices
Version:        svn47868
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ctable.sty), tex(xcolor.sty), tex(tabularx.sty), tex(graphicx.sty)
Requires:       tex(xstring.sty), tex(calc.sty), tex(forarray.sty), tex(longtable.sty)
Requires:       tex(geometry.sty), tex(textpos.sty), tex(fancyhdr.sty)
Provides:       tex(isodoc.cls) = %{tl_version}

%description -n texlive-isodoc
The isodoc class can be used for the preparation of letters and
invoices (and, in the future, similar documents). Documents are
set up with options, thus making the class easily adaptable to
user's wishes and extensible for other document types. The
class is based on the NTG brief class by Victor Eijkhout, which
implements the NEN1026 standard.

%package -n texlive-isodoc-doc
Summary:        Documentation for isodoc
Version:        svn47868
Provides:       tex-isodoc-doc
AutoReqProv:    No

%description -n texlive-isodoc-doc
Documentation for isodoc

%package -n texlive-isonums
Provides:       tex-isonums = %{tl_version}
License:        LPPL
Summary:        Display numbers in maths mode according to ISO 31-0
Version:        svn17362.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(isonums.sty) = %{tl_version}

%description -n texlive-isonums
The package makes a quick hack to ziffer to display numbers in
maths mode according to ISO 31-0, regardless of input format
(European $1.235,7$ or Anglo-American $1,235.7$). The options
[euro, anglo] control the global input format. Default input
format is anglo. Documentation is included as comments to the
text source.

%package -n texlive-isonums-doc
Summary:        Documentation for isonums
Version:        svn17362.1.0

Provides:       tex-isonums-doc
AutoReqProv:    No

%description -n texlive-isonums-doc
Documentation for isonums

%package -n texlive-isorot
Provides:       tex-isorot = %{tl_version}
License:        LPPL
Summary:        Rotation of document elements
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(lscape.sty)
Provides:       tex(isorot.sty) = %{tl_version}

%description -n texlive-isorot
The package is for rotation of document elements. It is a
combination of the lscape package and an extension of the
rotating package. The package is designed for use with the iso
class but may be used with any normal class.

%package -n texlive-isorot-doc
Summary:        Documentation for isorot
Version:        svn15878.0

Provides:       tex-isorot-doc
AutoReqProv:    No

%description -n texlive-isorot-doc
Documentation for isorot

%package -n texlive-isotope
Provides:       tex-isotope = %{tl_version}
License:        LPPL
Summary:        A package for typesetting isotopes
Version:        svn23711.v0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(isotope.sty) = %{tl_version}

%description -n texlive-isotope
The package provides a command \isotope for setting the atomic
weight and atomic number indications of isotopes. (The naive
way of doing the job with (La)TeX mathematics commands produces
an unsatisfactory result.)

%package -n texlive-isotope-doc
Summary:        Documentation for isotope
Version:        svn23711.v0.3

Provides:       tex-isotope-doc
AutoReqProv:    No

%description -n texlive-isotope-doc
Documentation for isotope

%package -n texlive-issuulinks
Provides:       tex-issuulinks = %{tl_version}
License:        LPPL 1.3
Summary:        Produce external links instead of internal ones
Version:        svn25742.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty)
Provides:       tex(issuulinks.sty) = %{tl_version}

%description -n texlive-issuulinks
The PDF visualizer http://issuu.com/ISSUU is a popular service
which shows PDF documents "a page a time". Due to the way it is
implemented, internal links in these documents are not allowed.
Instead, they must be converted to external ones in the form
http://issuu.com/action/page?page=PAGENUMBER. The package
patches hyperref to produce external links in the required form
instead of internal links created by \ref, \cite and other
commands. Since the package redefines the internals of
hyperref, it must be loaded it AFTER hyperref.

%package -n texlive-issuulinks-doc
Summary:        Documentation for issuulinks
Version:        svn25742.1.1

Provides:       tex-issuulinks-doc
AutoReqProv:    No

%description -n texlive-issuulinks-doc
Documentation for issuulinks

%package -n texlive-iwhdp
Provides:       tex-iwhdp = %{tl_version}
License:        LPPL 1.3
Summary:        Halle Institute for Economic Research (IWH) Discussion Papers
Version:        svn37552.0.50

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(iwhdp.cls) = %{tl_version}

%description -n texlive-iwhdp
The document class is for creating Discussion Papers of the
Halle Institute for Economic Research (IWH) in Halle, Germany.
The class offers options for both English and German texts.

%package -n texlive-iwhdp-doc
Summary:        Documentation for iwhdp
Version:        svn37552.0.50

Provides:       tex-iwhdp-doc
AutoReqProv:    No

%description -n texlive-iwhdp-doc
Documentation for iwhdp

%package -n texlive-jlabels
Provides:       tex-jlabels = %{tl_version}
License:        Bibtex or LPPL
Summary:        Make letter-sized pages of labels
Version:        svn24858.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(ifthen.sty), tex(pstricks.sty), tex(etoolbox.sty)
Provides:       tex(jlabels.sty) = %{tl_version}

%description -n texlive-jlabels
The package provides controls for the numbers of rows and
columns.

%package -n texlive-jlabels-doc
Summary:        Documentation for jlabels
Version:        svn24858.0

Provides:       tex-jlabels-doc
AutoReqProv:    No

%description -n texlive-jlabels-doc
Documentation for jlabels

%package -n texlive-jslectureplanner
Provides:       tex-jslectureplanner = %{tl_version}
License:        LPPL 1.3
Summary:        Creation and management of university course material
Version:        svn43476
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty), tex(advdate.sty), tex(xkeyval.sty), tex(datetime.sty)
Requires:       tex(calc.sty), tex(ifthen.sty), tex(array.sty), tex(longtable.sty)
Requires:       tex(hhline.sty), tex(datatool.sty)
Provides:       tex(jslectureplanner.sty) = %{tl_version}
Provides:       tex(jsmembertable.sty) = %{tl_version}

%description -n texlive-jslectureplanner
The jslectureplanner package facilitates the generation and
management of university course material. It provides an
interface to set up and access centralized course data that can
be reused in all course documents. Furthermore, the package is
able to calculate the session dates of a whole semester and
generate course programs, if the course is held weekly and the
date of the first lecture is specified. Moreover, the package
can be used to generate a sectioned course bibliography via
biblatex.

%package -n texlive-jslectureplanner-doc
Summary:        Documentation for jslectureplanner
Version:        svn43476
Provides:       tex-jslectureplanner-doc
AutoReqProv:    No

%description -n texlive-jslectureplanner-doc
Documentation for jslectureplanner

%package -n texlive-jumplines
Provides:       tex-jumplines = %{tl_version}
License:        LPPL 1.3
Summary:        Articles with teasers and continuation later on
Version:        svn37553.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(xparse.sty), tex(xkeyval.sty), tex(xcolor.sty)
Requires:       tex(tcolorbox.sty), tex(babel.sty), tex(tocloft.sty), tex(ifluatex.sty)
Requires:       tex(hyperref.sty), tex(bookmark.sty), tex(luacolor.sty)
Provides:       tex(jumplines.sty) = %{tl_version}

%description -n texlive-jumplines
Jumplines is a package for typesetting (newspaper) articles
that show a teaser (some few lines of text/content) and are
continued at a later place, with optional hyperlinking and a
list of articles. It requires lualatex for colour support in
split boxes.

%package -n texlive-jumplines-doc
Summary:        Documentation for jumplines
Version:        svn37553.0.2

Provides:       tex-jumplines-doc
AutoReqProv:    No

%description -n texlive-jumplines-doc
Documentation for jumplines

%package -n texlive-jvlisting
Provides:       tex-jvlisting = %{tl_version}
License:        LPPL
Summary:        A replacement for LaTeX's verbatim package
Version:        svn24638.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(jvlisting.sty) = %{tl_version}

%description -n texlive-jvlisting
This package provides a LaTeX environment listing, an
alternative to the built-in verbatim environment. The listing
environment is tailored for including listings of computer
program source code into documents. The main advantages over
the original verbatim environment are: environments
automatically fixes leading whitespace so that the environment
and program listing can be indented with the rest of the
document source, and; listing environments may easily be
customised and extended.

%package -n texlive-jvlisting-doc
Summary:        Documentation for jvlisting
Version:        svn24638.0.7

Provides:       tex-jvlisting-doc
AutoReqProv:    No

%description -n texlive-jvlisting-doc
Documentation for jvlisting

%package -n texlive-kantlipsum
Provides:       tex-kantlipsum = %{tl_version}
License:        LPPL 1.3
Summary:        Generate sentences in Kant's style
Version:        svn45866
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(kantlipsum.sty) = %{tl_version}

%description -n texlive-kantlipsum
The package spits out sentences in Kantian style; the text is
provided by the Kant generator for Python by Mark Pilgrim,
described in the book "Dive into Python". The package is
modelled on lipsum, and may be used for similar purposes.

%package -n texlive-kantlipsum-doc
Summary:        Documentation for kantlipsum
Version:        svn45866
Provides:       tex-kantlipsum-doc
AutoReqProv:    No

%description -n texlive-kantlipsum-doc
Documentation for kantlipsum

%package -n texlive-kerntest
Provides:       tex-kerntest = %{tl_version}
License:        LPPL
Summary:        Print tables and generate control files to adjust kernings
Version:        svn15878.1.32

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(helvet.sty), tex(calc.sty), tex(longtable.sty)
Requires:       tex(array.sty), tex(color.sty), tex(ifthen.sty), tex(keyval.sty)
Requires:       tex(fontenc.sty)
Provides:       tex(kerntest.cls) = %{tl_version}, tex(ly1mtx.clo) = %{tl_version}
Provides:       tex(ot1mtx.clo) = %{tl_version}, tex(t1cmr-1200.fd) = %{tl_version}
Provides:       tex(t1mtx.clo) = %{tl_version}, tex(t2amtx.clo) = %{tl_version}
Provides:       tex(t2bmtx.clo) = %{tl_version}, tex(ts1mtx.clo) = %{tl_version}

%description -n texlive-kerntest
This class makes it easy to generate tables that show many
different kerning pairs of an arbitrary font, usable by LaTeX.
It shows the kerning values that are used in the font by
default. In addition, this class enables the user to alter the
kernings and to observe the results. Kerning pairs can be
defined for groups of similar glyphs at the same time. An mtx
file is generated automatically. The mtx file may then be
loaded by fontinst to introduce the user-made kernings into the
virtual font for later use in LaTeX.

%package -n texlive-kerntest-doc
Summary:        Documentation for kerntest
Version:        svn15878.1.32

Provides:       tex-kerntest-doc
AutoReqProv:    No

%description -n texlive-kerntest-doc
Documentation for kerntest

%package -n texlive-keycommand
Provides:       tex-keycommand = %{tl_version}
License:        LPPL
Summary:        Simple creation of commands with key-value arguments
Version:        svn18042.3.1415

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(kvsetkeys.sty), tex(xkeyval.sty), tex(etoolbox.sty)
Provides:       tex(keycommand.sty) = %{tl_version}

%description -n texlive-keycommand
The package (which requires e-TeX) provides a natural way to
define commands with optional keys. The package provides
\newkeycommand, \renewkeycommand, \providekeycommand,
\newkeyenvironment and \renewkeyenvironment, together with
\keycmd for a more advanced interface. The package is based on
kvsetkeys by Heiko Oberdiek.

%package -n texlive-keycommand-doc
Summary:        Documentation for keycommand
Version:        svn18042.3.1415

Provides:       tex-keycommand-doc
AutoReqProv:    No

%description -n texlive-keycommand-doc
Documentation for keycommand

%package -n texlive-keyreader
Provides:       tex-keyreader = %{tl_version}
License:        LPPL 1.3
Summary:        A robust interface to xkeyval
Version:        svn28195.0.5b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pdftexcmds.sty)
Provides:       tex(keyreader.sty) = %{tl_version}

%description -n texlive-keyreader
The package provides a robust interface to controlling keys in
xkeyval, removing some of that package's restrictions. The
package also addresses some of the issues now covered by the
author's ltxkeys package, which was assumed to be a replacement
for keyreader. Since keyreader has remained a favourite with
users, it has been reinstated.

%package -n texlive-keyreader-doc
Summary:        Documentation for keyreader
Version:        svn28195.0.5b

Provides:       tex-keyreader-doc
AutoReqProv:    No

%description -n texlive-keyreader-doc
Documentation for keyreader

%package -n texlive-keystroke
Provides:       tex-keystroke = %{tl_version}
License:        GPL+
Summary:        Graphical representation of keys on keyboard
Version:        svn17992.v1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(keystroke.sty) = %{tl_version}

%description -n texlive-keystroke
A LaTeX package which provides macros for the graphical
representation of the keys on a computer keyboard.

%package -n texlive-keystroke-doc
Summary:        Documentation for keystroke
Version:        svn17992.v1.6

Provides:       tex-keystroke-doc
AutoReqProv:    No

%description -n texlive-keystroke-doc
Documentation for keystroke

%package -n texlive-keyval2e
Provides:       tex-keyval2e = %{tl_version}
License:        LPPL 1.3
Summary:        A lightweight and robust key-value parser
Version:        svn23698.0.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(catoptions.sty)
Provides:       tex(keyval2e.sty) = %{tl_version}

%description -n texlive-keyval2e
The package provides lightweight and robust facilities for
creating and managing keys. Its machinery isn't as extensive as
that of, e.g., the ltxkeys package, but it is equally robust;
ease of use and speed of processing are the design aims of the
package.

%package -n texlive-keyval2e-doc
Summary:        Documentation for keyval2e
Version:        svn23698.0.0.2

Provides:       tex-keyval2e-doc
AutoReqProv:    No

%description -n texlive-keyval2e-doc
Documentation for keyval2e

%package -n texlive-kix
Provides:       tex-kix = %{tl_version}
License:        LPPL
Summary:        Typeset KIX codes
Version:        svn21606.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(kix.sty) = %{tl_version}

%description -n texlive-kix
Implements KIX codes as used by the Dutch PTT for bulk mail
addressing. (Royal Mail 4 State Code.) KIX is a registered
trade mark of PTT Post Holdings B. V.

%package -n texlive-kix-doc
Summary:        Documentation for kix
Version:        svn21606.0

Provides:       tex-kix-doc
AutoReqProv:    No

%description -n texlive-kix-doc
Documentation for kix

%package -n texlive-koma-moderncvclassic
Provides:       tex-koma-moderncvclassic = %{tl_version}
License:        LPPL 1.3
Summary:        Makes the style and command of moderncv (style classic) available for koma-classes and thus compatible with biblatex
Version:        svn25025.v0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(ifpdf.sty), tex(xcolor.sty), tex(lmodern.sty)
Requires:       tex(marvosym.sty), tex(url.sty), tex(graphicx.sty), tex(hyperref.sty)
Provides:       tex(koma-moderncvclassic.sty) = %{tl_version}

%description -n texlive-koma-moderncvclassic
This package provides an imitation of the moderncv class with
the classic style (by Xavier Danaux), to be used in conjunction
with the koma-classes. Thus it is possible to configure
pagelayout, headings etc. the way it is done in koma-classes.
Moreover, it is possible to use biblatex, while the original
moderncv-class is incompatible with biblatex.

%package -n texlive-koma-moderncvclassic-doc
Summary:        Documentation for koma-moderncvclassic
Version:        svn25025.v0.5

Provides:       tex-koma-moderncvclassic-doc
AutoReqProv:    No

%description -n texlive-koma-moderncvclassic-doc
Documentation for koma-moderncvclassic

%package -n texlive-koma-script-sfs
Provides:       tex-koma-script-sfs = %{tl_version}
License:        LPPL
Summary:        Koma-script letter class option for Finnish
Version:        svn26137.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-koma-script-sfs
A koma-script parameter set for letters on A4 paper, complying
with Finnish standards SFS 2486, 2487 and 2488; suitable for
window envelopes with window on the left size in the sizes C5,
C65, E5 and E65 (although, because the address window is
smaller, for sizes E5 and E65 the address may not fit within
the window, but ordinary 3-line address should fit).

%package -n texlive-koma-script-sfs-doc
Summary:        Documentation for koma-script-sfs
Version:        svn26137.1.0

Provides:       tex-koma-script-sfs-doc
AutoReqProv:    No

%description -n texlive-koma-script-sfs-doc
Documentation for koma-script-sfs

%package -n texlive-komacv
Provides:       tex-komacv = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting a beuatiful CV with various style options
Version:        svn43902
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(kvoptions.sty), tex(calc.sty), tex(xcolor.sty)
Requires:       tex(etoolbox.sty), tex(ifpdf.sty), tex(ifluatex.sty), tex(ifxetex.sty)
Requires:       tex(scrpage2.sty), tex(marvosym.sty), tex(array.sty), tex(graphicx.sty)
Requires:       tex(microtype.sty), tex(enumitem.sty), tex(hyperref.sty), tex(fontspec.sty)
Requires:       tex(inputenc.sty), tex(fontenc.sty), tex(lastpage.sty)
Provides:       tex(komacv-casual.sty) = %{tl_version}, tex(komacv-classic.sty) = %{tl_version}
Provides:       tex(komacv-oldstyle.sty) = %{tl_version}
Provides:       tex(komacv.cls) = %{tl_version}

%description -n texlive-komacv
The class simplifies the creation of beautiful CV. The user may
choose between different styles, and may adjust settings to
tune the output.

%package -n texlive-komacv-doc
Summary:        Documentation for komacv
Version:        svn43902
Provides:       tex-komacv-doc
AutoReqProv:    No

%description -n texlive-komacv-doc
Documentation for komacv

%package -n texlive-ktv-texdata
Provides:       tex-ktv-texdata = %{tl_version}
License:        GPL+
Summary:        Extract subsets of documents
Version:        svn27369.05.34

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty)
Provides:       tex(ktv-buildnum.sty) = %{tl_version}, tex(ktv-texdata.sty) = %{tl_version}

%description -n texlive-ktv-texdata
The package defines an exercice environment which numbers every
exercise, and a command \get to extract a collection whose
argument is a comma-separated set of exercise index numbers.
While the package was designed for teachers constructing tables
of exercises, it plainly has more general application.

%package -n texlive-ktv-texdata-doc
Summary:        Documentation for ktv-texdata
Version:        svn27369.05.34

Provides:       tex-ktv-texdata-doc
AutoReqProv:    No

%description -n texlive-ktv-texdata-doc
Documentation for ktv-texdata


%package -n texlive-js-misc
Provides:       tex-js-misc = %{tl_version}
License:        Public Domain
Summary:        Miscellaneous macros from Joachim Schrod
Version:        svn16211.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cassette.tex) = %{tl_version}, tex(idverb.tex) = %{tl_version}
Provides:       tex(js-misc.tex) = %{tl_version}, tex(schild.tex) = %{tl_version}
Provides:       tex(sperr.tex) = %{tl_version}, tex(xfig.tex) = %{tl_version}

%description -n texlive-js-misc
A bunch of packages, including: idverb.tex, for 'short
verbatim'; xfig.tex, for including xfig/transfig output in a
TeX document; and cassette.tex for setting cassette labels.

%package -n texlive-js-misc-doc
Summary:        Documentation for js-misc
Version:        svn16211.0

Provides:       tex-js-misc-doc
AutoReqProv:    No

%description -n texlive-js-misc-doc
Documentation for js-misc

%package -n texlive-jmlr
Provides:       tex-jmlr = %{tl_version}
License:        LPPL 1.3
Summary:        Class files for the Journal of Machine Learning Research
Version:        svn44935
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(calc.sty), tex(etoolbox.sty), tex(amsmath.sty)
Requires:       tex(amssymb.sty), tex(natbib.sty), tex(graphicx.sty), tex(url.sty)
Requires:       tex(xcolor.sty), tex(algorithm2e.sty), tex(hyperref.sty), tex(nameref.sty)
Requires:       tex(setspace.sty), tex(currfile.sty), tex(fink.sty), tex(xmpincl.sty)
Requires:       tex(combnat.sty)
Provides:       tex(jmlr.cls) = %{tl_version}, tex(jmlrbook.cls) = %{tl_version}

%description -n texlive-jmlr
The jmlr bundle provides a class for authors (jmlr) and a class
for production editors (jmlrbook), as well as a script
makejmlrbook The jmlrbook class can be used to combine articles
written using the jmlr class into a book. The class uses the
combine class and the hyperref package to produce either a
colour hyperlinked book for on-line viewing or a greyscale
nonhyperlinked book for printing. The makejmlrbook Perl script
can be used to create the colour hyperlinked and greyscale
nonhyperlinked PDFs of a document using the jmlrbook class. It
can also create a set of HTML files that list the included
papers with links to their abstracts and the individual
articles as PDFs.

%package -n texlive-jmlr-doc
Summary:        Documentation for jmlr
Version:        svn44935
Provides:       tex-jmlr-doc
AutoReqProv:    No

%description -n texlive-jmlr-doc
Documentation for jmlr

%package -n texlive-jpsj
Provides:       tex-jpsj = %{tl_version}
License:        LPPL
Summary:        Document Class for Journal of the Physical Society of Japan
Version:        svn15878.1.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(graphicx.sty), tex(overcite.sty)
Provides:       tex(jpsj2.cls) = %{tl_version}

%description -n texlive-jpsj
jpsj package

%package -n texlive-jpsj-doc
Summary:        Documentation for jpsj
Version:        svn15878.1.2.2

Provides:       tex-jpsj-doc
AutoReqProv:    No

%description -n texlive-jpsj-doc
Documentation for jpsj

%package -n texlive-kdgdocs
Provides:       tex-kdgdocs = %{tl_version}
License:        LPPL 1.3
Summary:        Document classes for Karel de Grote University College
Version:        svn24498.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(ifxetex.sty), tex(cmbright.sty), tex(fontspec.sty)
Requires:       tex(ifthen.sty), tex(graphicx.sty), tex(eso-pic.sty), tex(color.sty)
Requires:       tex(tikz.sty), tex(fancyhdr.sty), tex(hyperref.sty)
Provides:       tex(kdgcoursetext.cls) = %{tl_version}, tex(kdgmasterthesis.cls) = %{tl_version}

%description -n texlive-kdgdocs
The bundle provides two classes for usage by KdG professors and
master students: kdgcoursetext: for writing course texts, and
kdgmasterthesis: for writing master's theses. The bundle
replaces the original kdgcoursetext package (now removed from
the archive).

%package -n texlive-kdgdocs-doc
Summary:        Documentation for kdgdocs
Version:        svn24498.1.0

Provides:       tex-kdgdocs-doc
AutoReqProv:    No

%description -n texlive-kdgdocs-doc
Documentation for kdgdocs

%package -n texlive-kluwer
Provides:       tex-kluwer = %{tl_version}
License:        LPPL
Summary:        kluwer package
Version:        svn45756
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(amssymb.sty), tex(wasysym.sty), tex(fontenc.sty), tex(textcomp.sty)
Requires:       tex(mathptm.sty)
Provides:       tex(klu10.clo) = %{tl_version}, tex(klu105.clo) = %{tl_version}
Provides:       tex(klu11.clo) = %{tl_version}, tex(klu12.clo) = %{tl_version}
Provides:       tex(klu9.clo) = %{tl_version}, tex(klucite.sty) = %{tl_version}
Provides:       tex(kluedit.sty) = %{tl_version}, tex(klufloa.sty) = %{tl_version}
Provides:       tex(klulist.sty) = %{tl_version}, tex(klumac.sty) = %{tl_version}
Provides:       tex(klumath.sty) = %{tl_version}, tex(klumono.sty) = %{tl_version}
Provides:       tex(klunote.sty) = %{tl_version}, tex(kluopen.sty) = %{tl_version}
Provides:       tex(klups.sty) = %{tl_version}, tex(kluref.sty) = %{tl_version}
Provides:       tex(klusec.sty) = %{tl_version}, tex(klut10.clo) = %{tl_version}
Provides:       tex(klut11.clo) = %{tl_version}, tex(klut12.clo) = %{tl_version}
Provides:       tex(klut9.clo) = %{tl_version}, tex(klutab.sty) = %{tl_version}
Provides:       tex(kluwer.cls) = %{tl_version}

%description -n texlive-kluwer
kluwer package

%package -n texlive-kluwer-doc
Summary:        Documentation for kluwer
Version:        svn45756
Provides:       tex-kluwer-doc
AutoReqProv:    No

%description -n texlive-kluwer-doc
Documentation for kluwer

%package -n texlive-karnaugh
Provides:       tex-karnaugh = %{tl_version}
License:        LPPL
Summary:        Typeset Karnaugh-Veitch-maps
Version:        svn21338.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(kvmacros.tex) = %{tl_version}

%description -n texlive-karnaugh
The package provides macros for typesetting Karnaugh-Maps and
Veitch-Charts in a simple and user-friendly way. Karnaugh-Maps
and Veitch-Charts are used to display and simplify logic
functions "manually". These macros can typeset Karnaugh-Maps
and Veitch-Charts with up to ten variables (=1024 entries).

%package -n texlive-karnaugh-doc
Summary:        Documentation for karnaugh
Version:        svn21338.0

Provides:       tex-karnaugh-doc
AutoReqProv:    No

%description -n texlive-karnaugh-doc
Documentation for karnaugh

%package -n texlive-karnaughmap
Provides:       tex-karnaughmap = %{tl_version}
License:        LPPL 1.2
Summary:        Typeset Karnaugh maps
Version:        svn36989.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(xkeyval.sty), tex(ifthen.sty), tex(xstring.sty)
Provides:       tex(karnaughmap.sty) = %{tl_version}

%description -n texlive-karnaughmap
This package provides an easy to use interface to typeset
Karnaugh maps using TikZ. Though similar to the karnaugh
macros, it provides a key-value system to customize
karnaughmaps and a proper LaTeX package.

%package -n texlive-karnaughmap-doc
Summary:        Documentation for karnaughmap
Version:        svn36989.2.0

Provides:       tex-karnaughmap-doc
AutoReqProv:    No

%description -n texlive-karnaughmap-doc
Documentation for karnaughmap

%package -n texlive-jacow-doc
Provides:       tex-jacow-doc = %{tl_version}
License:        LPPL
Summary:        doc files of jacow
Version:        svn47287
AutoReqProv:    No

%description -n texlive-jacow-doc
Documentation for jacow

%package -n texlive-jacow
Provides:       tex-jacow = %{tl_version}
License:        LPPL
Summary:        The "jacow.cls" class is used for submissions to the proceedings of conferences on JACoW.org
Version:        svn47287
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(jacow.cls) = %{tl_version}

%description -n texlive-jacow
The jacow class is used for submissions to the proceedings of
conferences on Joint Accelerator Conferences Website (JACoW),
an international collaboration that publishes the proceedings
of accelerator conferences held around the world.

%package -n texlive-keyvaltable-doc
Provides:       tex-keyvaltable-doc = %{tl_version}
License:        LPPL
Summary:        doc files of keyvaltable
Version:        svn41414

AutoReqProv:    No

%description -n texlive-keyvaltable-doc
Documentation for keyvaltable

%package -n texlive-keyvaltable
Provides:       tex-keyvaltable = %{tl_version}
License:        LPPL
Summary:        Re-usable tables separating content and presentation
Version:        svn41414

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(keyvaltable.sty) = %{tl_version}

%description -n texlive-keyvaltable
The main goal of the keyvaltable package is to offer means for
typesetting tables easily and yet still looking rather nicely
in a way that separates content from presentation and with re-
usable layout for tables of the same type. For this purpose,
the package provides the environment KeyValTable, which allows
one to typeset tables that have a previously defined column
layout and whose rows can be produced in a key-value fashion.

%package -n texlive-ksp-thesis-doc
Provides:       tex-ksp-thesis-doc = %{tl_version}
License:        LPPL
Summary:        doc files of ksp-thesis
Version:        svn39080

AutoReqProv:    No

%description -n texlive-ksp-thesis-doc
Documentation for ksp-thesis

%package -n texlive-ksp-thesis
Provides:       tex-ksp-thesis = %{tl_version}
License:        LPPL
Summary:        A LaTeX class for theses published with KIT Scientific Publishing
Version:        svn39080

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ksp-thesis.cls) = %{tl_version}

%description -n texlive-ksp-thesis
This package provides a LaTeX class intended for authors who
want to publish their thesis or other scientific work with KIT
Scientific Publishing (KSP). The class is based on the scrbook
class of the KOMA-script bundle in combination with the
ClassicThesis and ArsClassica packages. It modifies some of the
layout and style definitions of these packages in order to
provide a document layout that should be compatible with the
requirements by KSP.

%package -n texlive-iscram
Summary:        a LaTeX class to publish article to ISCRAM conferences
Version:        svn45801
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(iscram.cls) = %{tl_version}

%description -n texlive-iscram
LaTeX class to publish article to ISCRAM (International
Conference on Information Systems for Crisis Response and
Management).

%package -n texlive-isopt
Summary:        writing a TeX length with a space between number and unit
Version:        svn45509
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(isopt.sty) = %{tl_version}

%description -n texlive-isopt
Writing a TeX length with \the writes the value and the unit
without a space. Package isopt provides a macro \ISO which
inserts a user defined space between number and unit.

%package -n texlive-istgame
Summary:        Drawing Game Trees with TikZ
Version:        svn45417
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(istgame.sty) = %{tl_version}

%description -n texlive-istgame
This LaTeX package provides macros based on TikZ to draw a game
tree. The main idea underlying its core macros is the
completion of a whole tree by using a sequence of simple
'parent-child' tree structures, with no longer nested relations
involved (like the use of 'grandchildren' or
'great-grandchildren'). Using this package you can draw a game
tree as easily as drawing a game tree with pen and paper. This
package depends on expl3, TikZ, and xparse. The 'ist' prefix
stands for "it's a simple tree" or "In-Sung's simple tree."

%package -n texlive-jlreq
Summary:        Japanese document class based on requirements for Japanese text layout
Version:        svn48376
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bjlreq-v.tfm) = %{tl_version}, tex(bjlreq.tfm) = %{tl_version}
Provides:       tex(bjlreqg-v.tfm) = %{tl_version}, tex(bjlreqg.tfm) = %{tl_version}
Provides:       tex(bzjlreq-v.tfm) = %{tl_version}, tex(bzjlreq.tfm) = %{tl_version}
Provides:       tex(bzjlreqg-v.tfm) = %{tl_version}, tex(bzjlreqg.tfm) = %{tl_version}
Provides:       tex(jlreq-v.tfm) = %{tl_version}, tex(jlreq.tfm) = %{tl_version}
Provides:       tex(jlreqg-v.tfm) = %{tl_version}, tex(jlreqg.tfm) = %{tl_version}
Provides:       tex(ubjlreq-q.tfm) = %{tl_version}, tex(ubjlreq-v.tfm) = %{tl_version}
Provides:       tex(ubjlreq.tfm) = %{tl_version}, tex(ubjlreqg-q.tfm) = %{tl_version}
Provides:       tex(ubjlreqg-v.tfm) = %{tl_version}, tex(ubjlreqg.tfm) = %{tl_version}
Provides:       tex(ubzjlreq-q.tfm) = %{tl_version}, tex(ubzjlreq-v.tfm) = %{tl_version}
Provides:       tex(ubzjlreq.tfm) = %{tl_version}, tex(ubzjlreqg-q.tfm) = %{tl_version}
Provides:       tex(ubzjlreqg-v.tfm) = %{tl_version}, tex(ubzjlreqg.tfm) = %{tl_version}
Provides:       tex(ujlreq-q.tfm) = %{tl_version}, tex(ujlreq-v.tfm) = %{tl_version}
Provides:       tex(ujlreq.tfm) = %{tl_version}, tex(ujlreqg-q.tfm) = %{tl_version}
Provides:       tex(ujlreqg-v.tfm) = %{tl_version}, tex(ujlreqg.tfm) = %{tl_version}
Provides:       tex(uzjlreq-q.tfm) = %{tl_version}, tex(uzjlreq-v.tfm) = %{tl_version}
Provides:       tex(uzjlreq.tfm) = %{tl_version}, tex(uzjlreqg-q.tfm) = %{tl_version}
Provides:       tex(uzjlreqg-v.tfm) = %{tl_version}, tex(uzjlreqg.tfm) = %{tl_version}
Provides:       tex(zjlreq-v.tfm) = %{tl_version}, tex(zjlreq.tfm) = %{tl_version}
Provides:       tex(zjlreqg-v.tfm) = %{tl_version}, tex(zjlreqg.tfm) = %{tl_version}
Provides:       tex(jlreq.cls) = %{tl_version}, tex(bjlreq-v.vf) = %{tl_version}
Provides:       tex(bjlreq.vf) = %{tl_version}, tex(bjlreqg-v.vf) = %{tl_version}
Provides:       tex(bjlreqg.vf) = %{tl_version}, tex(bzjlreq-v.vf) = %{tl_version}
Provides:       tex(bzjlreq.vf) = %{tl_version}, tex(bzjlreqg-v.vf) = %{tl_version}
Provides:       tex(bzjlreqg.vf) = %{tl_version}, tex(jlreq-v.vf) = %{tl_version}
Provides:       tex(jlreq.vf) = %{tl_version}, tex(jlreqg-v.vf) = %{tl_version}
Provides:       tex(jlreqg.vf) = %{tl_version}, tex(ubjlreq-q.vf) = %{tl_version}
Provides:       tex(ubjlreq-v.vf) = %{tl_version}, tex(ubjlreq.vf) = %{tl_version}
Provides:       tex(ubjlreqg-q.vf) = %{tl_version}, tex(ubjlreqg-v.vf) = %{tl_version}
Provides:       tex(ubjlreqg.vf) = %{tl_version}, tex(ubzjlreq-q.vf) = %{tl_version}
Provides:       tex(ubzjlreq-v.vf) = %{tl_version}, tex(ubzjlreq.vf) = %{tl_version}
Provides:       tex(ubzjlreqg-q.vf) = %{tl_version}, tex(ubzjlreqg-v.vf) = %{tl_version}
Provides:       tex(ubzjlreqg.vf) = %{tl_version}, tex(ujlreq-q.vf) = %{tl_version}
Provides:       tex(ujlreq-v.vf) = %{tl_version}, tex(ujlreq.vf) = %{tl_version}
Provides:       tex(ujlreqg-q.vf) = %{tl_version}, tex(ujlreqg-v.vf) = %{tl_version}
Provides:       tex(ujlreqg.vf) = %{tl_version}, tex(uzjlreq-q.vf) = %{tl_version}
Provides:       tex(uzjlreq-v.vf) = %{tl_version}, tex(uzjlreq.vf) = %{tl_version}
Provides:       tex(uzjlreqg-q.vf) = %{tl_version}, tex(uzjlreqg-v.vf) = %{tl_version}
Provides:       tex(uzjlreqg.vf) = %{tl_version}, tex(zjlreq-v.vf) = %{tl_version}
Provides:       tex(zjlreq.vf) = %{tl_version}, tex(zjlreqg-v.vf) = %{tl_version}
Provides:       tex(zjlreqg.vf) = %{tl_version}

%description -n texlive-jlreq
This package provides a Japanese document class based on
requirements for Japanese text layout. The class file and the
JFM (Japanese font metric) files for LuaTeX-ja / pLaTeX /
upLaTeX are provided.

%package -n texlive-keyfloat
Summary:        provides a key/value interface for generating floats
Version:        svn44306
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(keyfloat.sty) = %{tl_version}

%description -n texlive-keyfloat
The keyfloat package provides a key/value user interface for
quickly creating figures with a single image each, figures with
arbitrary contents, tables, subfloats, rows of floats, floats
located [H]ere, floats in the [M]argin, and floats with text
[W]rapped around them. Key/value combinations may specify a
caption and label, a width proportional to \linewidth, a fixed
width and/or height, rotation, scaling, a tight or loose frame,
an \arraystretch, a continued float, additional supplemental
text, and an artist/author's name with automatic index entry.
When used with the tocdata package, the name also appears in
the List of Figures. Floats may be placed into a row
environment, and are typeset to fit within the given number of
columns, continuing to the next row if necessary. Nested
sub-rows may be used to generate layouts such as two small
figures placed vertically next to one larger figure. Subfloats
are supported by two environments.

%package -n texlive-knowledge
Summary:        Displaying, hyperlinking, and indexing notions in a document
Version:        svn48280
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(knowledge.sty) = %{tl_version}

%description -n texlive-knowledge
The package offers a systematic way to handle
notions/concepts/terms throughout a document. It helps building
an index. In combination with hyperref it makes it easy to have
every reference of a concept linked to its introduction. It
also offers simple notations.

%package -n texlive-komacv-rg
Summary:        LaTeX packages that aid in creating CVs based on the komacv class and creating related documents
Version:        svn47668
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(komacv-addons.sty) = %{tl_version}, tex(komacv-lco.sty) = %{tl_version}
Provides:       tex(komacv-multilang.sty) = %{tl_version}

%description -n texlive-komacv-rg
The komacv-rg bundle provides packages that aid in creating CVs
based on the komacv class and creating related documents, such
as cover letters and cover sheets for job applications.
Concretely, the bundle consists of three packages:
komacv-addons, komacv-lco, and komacv-multilang. komacv-addons
is a small collection of add-ons and fixes for the komacv
class; komacv-lco enables the use of letter class options from
scrlttr2 also in komacv-based and other non-scrlttr2-based
documents; komacv-multilang enables the provisioning of CVs in
multiple languages and the selection of a language via babel or
polyglossia.

%package -n texlive-ku-template
Summary:        Template for University of Copenhagen logos
Version:        svn45935
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ku-template.sty) = %{tl_version}

%description -n texlive-ku-template
A comprehensive package for adding University of Copenhagen or
faculty logo to your front page. For use by student or staff at
University of Copenhagen / Københavns Universitet.


%package -n texlive-jnuexam
Summary:        Exam class for Jinan University
Version:        svn48157
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(jnuexam.cls) = %{tl_version}

%description -n texlive-jnuexam
The package provides an exam class for Jinan University
(China).

%package -n texlive-kanaparser
Summary:        Kana parser for LuaTeX
Version:        svn48052
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(kanaparser.lua) = %{tl_version}, tex(kanaparser.tex) = %{tl_version}

%description -n texlive-kanaparser
The package provides a kana parser for LuaTeX. It is a set of 4
macros that handle transliteration of text: from hiragana and
katakana to Latin from Latin and katakana to hiragana from
Latin and hiragana to katakana It can be used to write kana
directly using only the ASCII character set or for education
purposes. The package has support for obsolete and rarely used
syllables, some only accessible via the provided toggle macro.

%package -n texlive-karnaugh-map
Summary:        LaTeX package for drawing karnaugh maps with up to 6 variables
Version:        svn44131
License:        CC-BY-SA
Requires:       texlive-base texlive-kpathsea, tex(tikz.sty)
Requires:       tex(xparse.sty), tex(xstring.sty)
Provides:       tex(karnaugh-map.sty) = %{tl_version}

%description -n texlive-karnaugh-map
This package draws karnaugh maps with 2, 3, 4, 5, and 6
variables. It also contains commands for filling the karnaugh
map with terms semi-automatically or manually. Last but not
least it contains commands for drawing implicants on top of the
map. This package depends on the TikZ, xparse, and xstring
packages.

%package -n texlive-kurdishlipsum
Summary:        A package similar to the lipsum and ptext packages for the Kurdish language
Version:        svn47518
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(kurdishlipsum.sty) = %{tl_version}

%description -n texlive-kurdishlipsum
This package provides lispum-like facilities for the Kurdish
language. This package gives you easy access to the Kurdish
poerty and balladry text of the Diwany Vafaiy, Ahmedy Xani,
Naly, Mahwy,.... The package needs to be run under XeLaTeX.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="nowacki/iwona nowacki/kurier"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -rf %{buildroot}%{_datadir}/texlive/texmf-dist/source/latex/koma-script/*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-knuth-lib
%license knuth.txt
%{_texdir}/texmf-dist/fonts/source/public/knuth-lib/
%{_texdir}/texmf-dist/fonts/tfm/public/knuth-lib/
%{_texdir}/texmf-dist/tex/generic/knuth-lib/
%{_texdir}/texmf-dist/tex/plain/knuth-lib/

%files -n texlive-knuth-local
%license knuth.txt
%{_texdir}/texmf-dist/fonts/source/public/knuth-local/
%{_texdir}/texmf-dist/fonts/tfm/public/knuth-local/
%{_texdir}/texmf-dist/mft/knuth-local/
%{_texdir}/texmf-dist/tex/plain/knuth-local/

%files -n texlive-jneurosci
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/jneurosci/
%{_texdir}/texmf-dist/tex/latex/jneurosci/

%files -n texlive-jneurosci-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/jneurosci/

%files -n texlive-jurabib
%license gpl.txt
%{_texdir}/texmf-dist/bibtex/bib/jurabib/
%{_texdir}/texmf-dist/bibtex/bst/jurabib/
%{_texdir}/texmf-dist/tex/latex/jurabib/

%files -n texlive-jurabib-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/jurabib/

%files -n texlive-ksfh_nat
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/ksfh_nat/

%files -n texlive-jmn
%{_texdir}/texmf-dist/fonts/afm/jmn/
%{_texdir}/texmf-dist/fonts/enc/dvips/jmn/
%{_texdir}/texmf-dist/fonts/map/dvips/jmn/
%{_texdir}/texmf-dist/fonts/tfm/jmn/
%{_texdir}/texmf-dist/fonts/type1/jmn/

%files -n texlive-iwona
%license gfsl.txt
%{_datadir}/fonts/iwona
%{_texdir}/texmf-dist/fonts/afm/nowacki/iwona/
%{_texdir}/texmf-dist/fonts/enc/dvips/iwona/
%{_texdir}/texmf-dist/fonts/map/dvips/iwona/
%{_texdir}/texmf-dist/fonts/opentype/nowacki/iwona/
%{_texdir}/texmf-dist/fonts/tfm/nowacki/iwona/
%{_texdir}/texmf-dist/fonts/type1/nowacki/iwona/
%{_texdir}/texmf-dist/tex/latex/iwona/
%{_texdir}/texmf-dist/tex/plain/iwona/

%files -n texlive-iwona-doc
%license gfsl.txt
%{_texdir}/texmf-dist/doc/fonts/iwona/

%files -n texlive-jablantile
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/jablantile/

%files -n texlive-jablantile-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/jablantile/

%files -n texlive-jamtimes
%{_texdir}/texmf-dist/fonts/map/dvips/jamtimes/
%{_texdir}/texmf-dist/fonts/tfm/public/jamtimes/
%{_texdir}/texmf-dist/fonts/vf/public/jamtimes/
%{_texdir}/texmf-dist/tex/latex/jamtimes/

%files -n texlive-jamtimes-doc
%{_texdir}/texmf-dist/doc/latex/jamtimes/

%files -n texlive-junicode
%license gpl.txt
%{_texdir}/texmf-dist/fonts/truetype/public/junicode/
%{_texdir}/texmf-dist/tex/latex/junicode/

%files -n texlive-junicode-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/junicode/

%files -n texlive-kixfont
%{_texdir}/texmf-dist/fonts/source/public/kixfont/
%{_texdir}/texmf-dist/fonts/tfm/public/kixfont/

%files -n texlive-kixfont-doc
%{_texdir}/texmf-dist/doc/fonts/kixfont/

%files -n texlive-kpfonts
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/kpfonts/
%{_texdir}/texmf-dist/fonts/enc/dvips/kpfonts/
%{_texdir}/texmf-dist/fonts/enc/pdftex/kpfonts/
%{_texdir}/texmf-dist/fonts/map/dvips/kpfonts/
%{_texdir}/texmf-dist/fonts/source/public/kpfonts/
%{_texdir}/texmf-dist/fonts/tfm/public/kpfonts/
%{_texdir}/texmf-dist/fonts/type1/public/kpfonts/
%{_texdir}/texmf-dist/fonts/vf/public/kpfonts/
%{_texdir}/texmf-dist/tex/latex/kpfonts/

%files -n texlive-kpfonts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/kpfonts/

%files -n texlive-kurier
%license gfsl.txt
%{_datadir}/fonts/kurier
%{_texdir}/texmf-dist/fonts/afm/nowacki/kurier/
%{_texdir}/texmf-dist/fonts/enc/dvips/kurier/
%{_texdir}/texmf-dist/fonts/map/dvips/kurier/
%{_texdir}/texmf-dist/fonts/opentype/nowacki/kurier/
%{_texdir}/texmf-dist/fonts/tfm/nowacki/kurier/
%{_texdir}/texmf-dist/fonts/type1/nowacki/kurier/
%{_texdir}/texmf-dist/tex/latex/kurier/
%{_texdir}/texmf-dist/tex/plain/kurier/

%files -n texlive-kurier-doc
%license gfsl.txt
%{_texdir}/texmf-dist/doc/fonts/kurier/

%files -n texlive-kastrup
%license other-free.txt
%{_texdir}/texmf-dist/tex/generic/kastrup/

%files -n texlive-kastrup-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/generic/kastrup/

%files -n texlive-jura
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/jura/

%files -n texlive-jura-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/jura/

%files -n texlive-juraabbrev
%license gpl.txt
%{_texdir}/texmf-dist/makeindex/juraabbrev/
%{_texdir}/texmf-dist/tex/latex/juraabbrev/

%files -n texlive-juraabbrev-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/juraabbrev/

%files -n texlive-juramisc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/juramisc/

%files -n texlive-juramisc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/juramisc/

%files -n texlive-jurarsp
%license gpl.txt
%{_texdir}/texmf-dist/bibtex/bst/jurarsp/
%{_texdir}/texmf-dist/tex/latex/jurarsp/

%files -n texlive-jurarsp-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/jurarsp/

%files -n texlive-knuth-doc
%license knuth.txt
%{_texdir}/texmf-dist/doc/generic/knuth/

%files -n texlive-koma-script-examples-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/koma-script-examples/

%files -n texlive-kerkis
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/
%{_texdir}/texmf-dist/fonts/map/dvips/kerkis/
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/
%{_texdir}/texmf-dist/fonts/type1/public/
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/
%{_texdir}/texmf-dist/tex/latex/kerkis/

%files -n texlive-kerkis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/kerkis/

%files -n texlive-itnumpar
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/itnumpar/

%files -n texlive-itnumpar-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/itnumpar/

%files -n texlive-japanese-otf
%{_texdir}/texmf-dist/fonts/map/dvipdfmx/japanese-otf/
%{_texdir}/texmf-dist/fonts/ofm/public/japanese-otf/
%{_texdir}/texmf-dist/fonts/tfm/public/japanese-otf/
%{_texdir}/texmf-dist/fonts/vf/public/japanese-otf/
%{_texdir}/texmf-dist/tex/platex/japanese-otf/

%files -n texlive-japanese-otf-doc
%{_texdir}/texmf-dist/doc/fonts/japanese-otf/

%files -n texlive-japanese-otf-uptex
%license bsd.txt
%{_texdir}/texmf-dist/fonts/tfm/public/japanese-otf-uptex/
%{_texdir}/texmf-dist/fonts/vf/public/japanese-otf-uptex/
%{_texdir}/texmf-dist/tex/platex/japanese-otf-uptex/

%files -n texlive-japanese-otf-uptex-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/fonts/japanese-otf-uptex/

%files -n texlive-jsclasses
%license bsd.txt
%{_texdir}/texmf-dist/tex/platex/jsclasses/

%files -n texlive-jsclasses-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/platex/jsclasses/


%files -n texlive-kotex-oblivoir
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/kotex-oblivoir/

%files -n texlive-kotex-oblivoir-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/kotex-oblivoir/

%files -n texlive-kotex-utf
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/kotex-utf/

%files -n texlive-kotex-utf-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/kotex-utf/

%files -n texlive-kotex-plain
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/plain/kotex-plain/

%files -n texlive-kotex-plain-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/plain/kotex-plain/

%files -n texlive-jknapltx
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/jknapltx/

%files -n texlive-jknapltx-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/jknapltx/

%files -n texlive-koma-script
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/koma-script/
%{_texdir}/texmf-dist/doc/latex/koma-script/

%files -n texlive-knitting
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/knitting/
%{_texdir}/texmf-dist/fonts/map/dvips/knitting/
%{_texdir}/texmf-dist/fonts/source/public/knitting/
%{_texdir}/texmf-dist/fonts/tfm/public/knitting/
%{_texdir}/texmf-dist/fonts/type1/public/knitting/
%{_texdir}/texmf-dist/tex/latex/knitting/
%{_texdir}/texmf-dist/tex/plain/knitting/

%files -n texlive-knitting-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/knitting/

%files -n texlive-knittingpattern
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/knittingpattern/

%files -n texlive-knittingpattern-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/knittingpattern/

%files -n texlive-iso
%license lppl1.txt
%{_texdir}/texmf-dist/makeindex/iso/
%{_texdir}/texmf-dist/tex/latex/iso/

%files -n texlive-iso-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/iso/

%files -n texlive-iso10303
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/iso10303/

%files -n texlive-iso10303-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/iso10303/

%files -n texlive-isodate
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/isodate/

%files -n texlive-isodate-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/isodate/

%files -n texlive-isodoc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/isodoc/

%files -n texlive-isodoc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/isodoc/

%files -n texlive-isonums
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/isonums/

%files -n texlive-isonums-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/isonums/

%files -n texlive-isorot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/isorot/

%files -n texlive-isorot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/isorot/

%files -n texlive-isotope
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/isotope/

%files -n texlive-isotope-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/isotope/

%files -n texlive-issuulinks
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/issuulinks/

%files -n texlive-issuulinks-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/issuulinks/

%files -n texlive-iwhdp
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/iwhdp/

%files -n texlive-iwhdp-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/iwhdp/

%files -n texlive-jlabels
%{_texdir}/texmf-dist/tex/latex/jlabels/

%files -n texlive-jlabels-doc
%{_texdir}/texmf-dist/doc/latex/jlabels/

%files -n texlive-jslectureplanner
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/jslectureplanner/

%files -n texlive-jslectureplanner-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/jslectureplanner/

%files -n texlive-jumplines
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/jumplines/

%files -n texlive-jumplines-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/jumplines/

%files -n texlive-jvlisting
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/jvlisting/

%files -n texlive-jvlisting-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/jvlisting/

%files -n texlive-kantlipsum
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/kantlipsum/

%files -n texlive-kantlipsum-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/kantlipsum/

%files -n texlive-kerntest
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/kerntest/

%files -n texlive-kerntest-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/kerntest/

%files -n texlive-keycommand
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/keycommand/

%files -n texlive-keycommand-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/keycommand/

%files -n texlive-keyreader
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/keyreader/

%files -n texlive-keyreader-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/keyreader/

%files -n texlive-keystroke
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/keystroke/

%files -n texlive-keystroke-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/keystroke/

%files -n texlive-keyval2e
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/keyval2e/

%files -n texlive-keyval2e-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/keyval2e/

%files -n texlive-kix
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/kix/

%files -n texlive-kix-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/kix/

%files -n texlive-koma-moderncvclassic
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/koma-moderncvclassic/

%files -n texlive-koma-moderncvclassic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/koma-moderncvclassic/

%files -n texlive-koma-script-sfs
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/koma-script-sfs/

%files -n texlive-koma-script-sfs-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/koma-script-sfs/

%files -n texlive-komacv
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/komacv/

%files -n texlive-komacv-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/komacv/

%files -n texlive-ktv-texdata
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/ktv-texdata/

%files -n texlive-ktv-texdata-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/ktv-texdata/

%files -n texlive-isomath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/isomath/

%files -n texlive-isomath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/isomath/

%files -n texlive-js-misc
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/js-misc/

%files -n texlive-js-misc-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/plain/js-misc/

%files -n texlive-jmlr
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/jmlr/
%{_texdir}/texmf-dist/tex/latex/jmlr/

%files -n texlive-jmlr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/jmlr/

%files -n texlive-jpsj
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/jpsj/

%files -n texlive-jpsj-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/jpsj/

%files -n texlive-kdgdocs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/kdgdocs/

%files -n texlive-kdgdocs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/kdgdocs/

%files -n texlive-kluwer
%{_texdir}/texmf-dist/bibtex/bst/kluwer/
%{_texdir}/texmf-dist/tex/latex/kluwer/

%files -n texlive-kluwer-doc
%{_texdir}/texmf-dist/doc/latex/kluwer/

%files -n texlive-karnaugh
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/karnaugh/

%files -n texlive-karnaugh-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/karnaugh/

%files -n texlive-karnaughmap
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/karnaughmap/

%files -n texlive-karnaughmap-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/karnaughmap/

%files -n texlive-jacow-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/jacow/

%files -n texlive-jacow
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/jacow/

%files -n texlive-keyvaltable-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/keyvaltable/

%files -n texlive-keyvaltable
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/keyvaltable/

%files -n texlive-ksp-thesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ksp-thesis/

%files -n texlive-ksp-thesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ksp-thesis/

%files -n texlive-iscram
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/iscram/
%{_texdir}/texmf-dist/tex/latex/iscram/

%files -n texlive-isopt
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/latex/isopt/
%{_texdir}/texmf-dist/tex/latex/isopt/

%files -n texlive-istgame
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/istgame/
%{_texdir}/texmf-dist/tex/latex/istgame/

%files -n texlive-jlreq
%license bsd.txt
%doc %{_texdir}/texmf-dist/doc/latex/jlreq/
%{_texdir}/texmf-dist/fonts/tfm/public/jlreq/
%{_texdir}/texmf-dist/fonts/vf/public/jlreq/
%{_texdir}/texmf-dist/tex/latex/jlreq/
%{_texdir}/texmf-dist/tex/luatex/jlreq/

%files -n texlive-keyfloat
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/keyfloat/
%{_texdir}/texmf-dist/tex/latex/keyfloat/

%files -n texlive-knowledge
%license lppl1.2.txt
%doc %{_texdir}/texmf-dist/doc/latex/knowledge/
%{_texdir}/texmf-dist/tex/latex/knowledge/

%files -n texlive-komacv-rg
%license lppl1.2.txt
%doc %{_texdir}/texmf-dist/doc/latex/komacv-rg/
%{_texdir}/texmf-dist/tex/latex/komacv-rg/

%files -n texlive-ku-template
%doc %{_texdir}/texmf-dist/doc/latex/ku-template/
%{_texdir}/texmf-dist/tex/latex/ku-template/

%files -n texlive-jnuexam
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/jnuexam/
%doc %{_texdir}/texmf-dist/doc/latex/jnuexam/

%files -n texlive-kanaparser
%license bsd.txt
%{_texdir}/texmf-dist/tex/luatex/kanaparser/
%doc %{_texdir}/texmf-dist/doc/luatex/kanaparser/

%files -n texlive-karnaugh-map
%{_texdir}/texmf-dist/tex/latex/karnaugh-map/
%doc %{_texdir}/texmf-dist/doc/latex/karnaugh-map/

%files -n texlive-kurdishlipsum
%license lppl.txt
%{_texdir}/texmf-dist/tex/xelatex/kurdishlipsum/
%doc %{_texdir}/texmf-dist/doc/xelatex/kurdishlipsum/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
