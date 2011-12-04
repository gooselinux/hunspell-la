Name: hunspell-la
Summary: Latin hunspell dictionaries
%define upstreamid 20080903
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/1141/0/dict-la_2008-09-03.oxt
URL: http://extensions.services.openoffice.org/project/dict-la
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Latin hunspell dictionaries.

%prep
%setup -q -c -n hunspell-la

%build
for i in README_extension_owner-la.txt la/README-la-2008-09-03.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p la/la.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/la_VA.dic
cp -p la/la.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/la_VA.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_extension_owner-la.txt la/README-la-2008-09-03.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080903-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080903-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080903-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080903-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080903-1
- initial version
