Name:           libformula
Version:        1.1.6
Release:        %mkrel 3
Summary:        Formula Parser
License:        LGPLv2+
Group:          System/Libraries
Source0:        http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
URL:            http://reporting.pentaho.org/
BuildRequires:  ant, ant-contrib, ant-nodeps, java-devel, jpackage-utils, libbase >= 1.1.3
Requires:       java, jpackage-utils, jakarta-commons-logging, libbase >= 1.1.3
BuildArch:      noarch
Patch0:         libformula-1.1.2-fix-build.patch

%description
LibFormula provides Excel-Style-Expressions. The implementation provided
here is very generic and can be used in any application that needs to
compute formulas.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -c
%patch0 -p0
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib commons-logging-api libbase
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc

%install
mkdir -p %{buildroot}%{_javadir}
cp -p ./dist/%{name}-%{version}.jar %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}


%changelog

* Sat Jan 12 2013 umeabot <umeabot> 1.1.6-3.mga3
+ Revision: 357124
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Oct 14 2012 ennael <ennael> 1.1.6-2.mga3
+ Revision: 305436
- Documentation group

* Sat Jan 21 2012 kamil <kamil> 1.1.6-1.mga2
+ Revision: 198938
- new version 1.1.6
- rediff and rename patch to fix-build
- drop gcj support
- clean .spec

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.3-3.mga1
+ Revision: 74310
- Really build without gcj

* Fri Mar 18 2011 ennael <ennael> 1.1.3-2.mga1
+ Revision: 74283
- build without gcj

* Mon Jan 24 2011 dmorgan <dmorgan> 1.1.3-1.mga1
+ Revision: 35748
- Fix macros
- Adapt for mageia
- imported package libformula

