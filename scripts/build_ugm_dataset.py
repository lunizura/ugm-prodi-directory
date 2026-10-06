"""
Dataset generation engine for Universitas Gadjah Mada (UGM) Study Programs Directory.
Generates comprehensive prodi catalog across S1 (Sarjana), D4 (Sarjana Terapan Sekolah Vokasi),
and elite Pascasarjana (S2) with 18 Faculties + 1 Sekolah Vokasi, international accreditations
(AACSB, ASIIN, ABET, RSC, IABEE, AUN-QA), quota allocations (SNBP, SNBT, UM UGM CBT),
bilingual curricula, and graduate career trajectories.
Zero emoji compliance strictly enforced.
"""

import json
import csv
import os
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

UGM_METADATA = {
    "universitas": "Universitas Gadjah Mada",
    "universitas_en": "Gadjah Mada University",
    "singkatan": "UGM",
    "motto": "Mengakar Kuat, Menjulang Tinggi",
    "tahun_berdiri": 1949,
    "rektor": "Prof. dr. Ova Emilia, M.Med.Ed., Sp.OG(K)., Ph.D.",
    "website_utama": "https://www.ugm.ac.id",
    "portal_spmb": "https://um.ugm.ac.id",
    "lokasi_utama": "Kawasan Bulaksumur, Caturtunggal, Depok, Kabupaten Sleman, D.I. Yogyakarta 55281",
    "jalur_masuk": [
        "SNBP (Seleksi Nasional Berdasarkan Prestasi)",
        "SNBT (Seleksi Nasional Berdasarkan Tes / UTBK)",
        "UM UGM CBT (Ujian Mandiri Computer Based Test)",
        "IUP UGM (International Undergraduate Program)",
        "Penelusuran Bibit Unggul (PBU Kemitraan / Tidak Mampu / Olahraga & Seni)"
    ],
    "akreditasi_internasional_list": ["AACSB", "ASIIN", "ABET", "RSC", "IABEE", "AUN-QA"]
}

# Master program items: exactly balancing daya_tampung == dt_snbp + dt_snbt + dt_umugm
RAW_PRODI = [
    # =========================================================================
    # 1. FEB - Fakultas Ekonomika dan Bisnis (AACSB Accredited)
    # =========================================================================
    {
        "id": "s1-akuntansi",
        "kode": "31101",
        "nama": "Akuntansi",
        "nama_en": "Accounting",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ekonomika dan Bisnis", "fakultas_singkatan": "FEB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["AACSB"],
        "daya_tampung": 150, "dt_snbp": 45, "dt_snbt": 45, "dt_umugm": 60,
        "website": "https://feb.ugm.ac.id/akuntansi",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Program studi akuntansi terdepan di Indonesia yang terakreditasi AACSB internasional, menekankan integritas audit forensik, akuntansi keberlanjutan ESG, dan analitika data keuangan digital.",
            "en": "Indonesia's premier AACSB-accredited accounting degree focusing on forensic audit integrity, ESG sustainability accounting, and digital corporate financial analytics."
        },
        "fokus": {
            "id": ["Audit Lanjutan & Investigasi Forensik", "Pelaporan Keberlanjutan & ESG Accounting", "Analitika Data Keuangan & Pajak Digital", "Tata Kelola Perusahaan & Pengendalian Internal"],
            "en": ["Advanced Audit & Forensic Investigation", "Sustainability & ESG Corporate Reporting", "Financial Data Analytics & Digital Taxation", "Corporate Governance & Internal Control"]
        },
        "karir": {
            "id": ["Auditor Senior di Big Four Accounting Firms", "Financial Controller & Corporate Treasurer", "Konsultan Pajak & Manajemen Risiko Keuangan", "Analis Keuangan BPK / OJK / Bank Indonesia"],
            "en": ["Senior Auditor at Big Four Accounting Firms", "Corporate Financial Controller & Treasurer", "Tax Consultant & Risk Advisory Specialist", "Public Financial Analyst at BPK / OJK / Central Bank"]
        }
    },
    {
        "id": "s1-manajemen",
        "kode": "31102",
        "nama": "Manajemen",
        "nama_en": "Management",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ekonomika dan Bisnis", "fakultas_singkatan": "FEB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["AACSB"],
        "daya_tampung": 150, "dt_snbp": 45, "dt_snbt": 45, "dt_umugm": 60,
        "website": "https://feb.ugm.ac.id/manajemen",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Pendidikan manajemen bisnis berstandar global AACSB yang mencetak pemimpin strategis di bidang keuangan korporasi, pemasaran digital, operasi cerdas, dan modal ventura.",
            "en": "Global AACSB-standard business management education developing strategic leaders in corporate finance, digital marketing, smart operations, and venture capital."
        },
        "fokus": {
            "id": ["Kepemimpinan Strategis & Inovasi Bisnis", "Manajemen Investasi & Valuasi Korporasi", "Pemasaran Digital & Analitika Konsumen", "Operasi Rantai Pasok Berkelanjutan"],
            "en": ["Strategic Leadership & Business Innovation", "Investment Management & Corporate Valuation", "Digital Marketing & Consumer Analytics", "Sustainable Supply Chain Operations"]
        },
        "karir": {
            "id": ["Management Consultant di Firma Strategi Global", "Investment Banking Analyst & Portofolio Lead", "Brand Manager & Digital Marketing Strategist", "Business Founder & Venture Capital Associate"],
            "en": ["Management Consultant at Global Strategy Firms", "Investment Banking Analyst & Portfolio Lead", "Brand Manager & Digital Strategist", "Business Founder & Venture Capital Associate"]
        }
    },
    {
        "id": "s1-ilmu-ekonomi",
        "kode": "31103",
        "nama": "Ilmu Ekonomi",
        "nama_en": "Economics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ekonomika dan Bisnis", "fakultas_singkatan": "FEB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["AACSB"],
        "daya_tampung": 100, "dt_snbp": 30, "dt_snbt": 30, "dt_umugm": 40,
        "website": "https://feb.ugm.ac.id/ilmu-ekonomi",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Analisis teori ekonomi makro dan mikro terapan, pemodelan ekonometrika lanjutan, kebijakan moneter dan fiskal, serta pembangunan ekonomi inklusif berstandar AACSB.",
            "en": "Rigorous applied macro and microeconomic theory, advanced econometric modeling, monetary and fiscal policy, and inclusive economic development under AACSB standards."
        },
        "fokus": {
            "id": ["Ekonometrika Lanjutan & Data Spasial", "Kebijakan Moneter & Stabilitas Finansial", "Ekonomi Pembangunan & Pengentasan Kemiskinan", "Ekonomi Lingkungan & Transisi Energi"],
            "en": ["Advanced Econometrics & Spatial Analytics", "Monetary Policy & Financial Stability", "Development Economics & Poverty Alleviation", "Environmental Economics & Energy Transition"]
        },
        "karir": {
            "id": ["Economist di Bank Sentral & Kementerian Keuangan", "Policy Researcher di Bank Dunia / Asian Development Bank", "Macroeconomic Strategist di Bank Investasi", "Analis Data Kebijakan Publik Bappenas"],
            "en": ["Central Bank & Finance Ministry Economist", "Policy Researcher at World Bank / ADB", "Macroeconomic Strategist in Investment Banks", "Public Policy Data Analyst at Planning Agencies"]
        }
    },

    # =========================================================================
    # 2. FK-KMK - Fakultas Kedokteran, Kesehatan Masyarakat, dan Keperawatan
    # =========================================================================
    {
        "id": "s1-kedokteran",
        "kode": "31201",
        "nama": "Kedokteran",
        "nama_en": "Medicine",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Medika",
        "fakultas": "Fakultas Kedokteran, Kesehatan Masyarakat, dan Keperawatan", "fakultas_singkatan": "FK-KMK",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "392",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 180, "dt_snbp": 54, "dt_snbt": 54, "dt_umugm": 72,
        "website": "https://fk.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 24.700.000)",
        "deskripsi": {
            "id": "Pendidikan dokter terbaik Indonesia dengan kurikulum berbasis kompetensi klinis terpadu, kedokteran keluarga komunitas, bioetika luhur, dan riset translasi biomedika.",
            "en": "Indonesia's premier medical education integrating clinical competencies, community-oriented family medicine, high bioethical standards, and translational biomedicine."
        },
        "fokus": {
            "id": ["Keterampilan Klinis & Diagnosis Terpadu", "Kedokteran Keluarga & Komunitas", "Riset Translasi Kedokteran Tropis", "Teknologi Kedokteran Cerdas & Telemedisin"],
            "en": ["Clinical Competencies & Integrated Diagnosis", "Family & Community Primary Medicine", "Tropical Disease Translational Research", "Smart Medical Technologies & Telemedicine"]
        },
        "karir": {
            "id": ["Dokter Pelayanan Primer & Rumah Sakit", "Residen Pendidikan Dokter Spesialis (PPDS)", "Peneliti Medis di Lembaga Riset Biomedis", "Health Administrator Organisasi Kesehatan Dunia (WHO)"],
            "en": ["Primary Care Physician & Hospital Doctor", "Specialist Medical Resident (Residency)", "Biomedical & Clinical Trial Researcher", "Global Health Officer at Health Agencies / WHO"]
        }
    },
    {
        "id": "s1-keperawatan",
        "kode": "31202",
        "nama": "Ilmu Keperawatan",
        "nama_en": "Nursing Science",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Medika",
        "fakultas": "Fakultas Kedokteran, Kesehatan Masyarakat, dan Keperawatan", "fakultas_singkatan": "FK-KMK",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 120, "dt_snbp": 36, "dt_snbt": 36, "dt_umugm": 48,
        "website": "https://fk.ugm.ac.id/keperawatan",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Pendidikan profesi keperawatan komprehensif berstandar internasional ASIIN yang mencakup asuhan keperawatan kritis, komunitas, jiwa, dan manajemen keselamatan pasien.",
            "en": "Comprehensive ASIIN-accredited nursing science education encompassing critical care, community health, psychiatric nursing, and patient safety clinical management."
        },
        "fokus": {
            "id": ["Keperawatan Gawat Darurat & Kritis", "Keperawatan Komunitas & Geriatri", "Manajemen Keselamatan Pasien Terpadu", "Informatika Keperawatan Digital"],
            "en": ["Emergency & Critical Care Nursing", "Community & Geriatric Healthcare", "Patient Safety & Clinical Management", "Digital Nursing Informatics"]
        },
        "karir": {
            "id": ["Perawat Klinis di Rumah Sakit Internasional", "Clinical Nurse Specialist / Nurse Educator", "Manajer Mutu & Keselamatan Pasien Rumah Sakit", "Public Health Nurse di Lembaga Kesehatan"],
            "en": ["Clinical Nurse in International Hospitals", "Clinical Nurse Specialist / Nurse Educator", "Hospital Quality & Patient Safety Manager", "Public Health Nurse in Health Departments"]
        }
    },
    {
        "id": "s1-gizi-kesehatan",
        "kode": "31203",
        "nama": "Gizi Kesehatan",
        "nama_en": "Health Nutrition",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Medika",
        "fakultas": "Fakultas Kedokteran, Kesehatan Masyarakat, dan Keperawatan", "fakultas_singkatan": "FK-KMK",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 100, "dt_snbp": 30, "dt_snbt": 30, "dt_umugm": 40,
        "website": "https://gizi.fk.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Pengembangan sains gizi klinis, gizi masyarakat pencegahan stunting, keamanan pangan fungsional, dan terapi nutrisi berbasis bukti (dietetika).",
            "en": "Clinical nutrition science, community public nutrition for stunting eradication, functional food safety, and evidence-based medical nutrition therapy."
        },
        "fokus": {
            "id": ["Nutrisi Klinis & Dietetika Terapi", "Gizi Masyarakat & Intervensi Stunting", "Sains Makanan Fungsional & Metabolisme", "Manajemen Sistem Pelayanan Makanan"],
            "en": ["Clinical Nutrition & Medical Dietetics", "Community Nutrition & Stunting Mitigation", "Functional Food Sciences & Metabolism", "Food Service Systems Management"]
        },
        "karir": {
            "id": ["Dietisien Terdaftar di Rumah Sakit Terakreditasi", "Nutrition Program Officer UNICEF / Kemenkes", "Nutrisionis Korporasi Industri Pangan & Wellness", "Konsultan Pola Makan Atlet & Personalisasi Gizi"],
            "en": ["Registered Clinical Dietitian", "Nutrition Program Officer (UNICEF/Health Ministry)", "Corporate Nutritionist in Food & Wellness Brands", "Sports & Personalized Nutrition Consultant"]
        }
    },

    # =========================================================================
    # 3. FKG - Fakultas Kedokteran Gigi
    # =========================================================================
    {
        "id": "s1-kedokteran-gigi",
        "kode": "31301",
        "nama": "Kedokteran Gigi",
        "nama_en": "Dentistry",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Medika",
        "fakultas": "Fakultas Kedokteran Gigi", "fakultas_singkatan": "FKG",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 150, "dt_snbp": 45, "dt_snbt": 45, "dt_umugm": 60,
        "website": "https://fkg.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 23.500.000)",
        "deskripsi": {
            "id": "Pendidikan dokter gigi terkemuka dengan keunggulan bedah mulut, ortodonsia, konservasi gigi, prostodonsia, serta teknologi rekonstruksi digital kedokteran gigi.",
            "en": "Leading dental education specializing in oral maxillofacial surgery, orthodontics, conservative dentistry, and digital dental reconstruction technology."
        },
        "fokus": {
            "id": ["Konservasi Gigi & Endodonsia Digital", "Bedah Mulut & Maksilofasial", "Ortodonsia & Estetika Dental", "Kesehatan Gigi Masyarakat & Pencegahan Karies"],
            "en": ["Conservative Dentistry & Digital Endodontics", "Oral & Maxillofacial Surgery", "Orthodontics & Dental Aesthetics", "Community Oral Health & Preventive Care"]
        },
        "karir": {
            "id": ["Dokter Gigi Praktik Mandiri & Rumah Sakit", "Residen Spesialis Kedokteran Gigi (PPDGS)", "Konsultan Estetika & Implantologi Dental", "Dosen & Peneliti Material Kedokteran Gigi"],
            "en": ["General Dental Practitioner & Hospital Dentist", "Dental Specialist Resident (PPDGS)", "Dental Implantology & Aesthetics Consultant", "Biomaterials Dental Lecturer & Researcher"]
        }
    },
    {
        "id": "s1-higiene-gigi",
        "kode": "31302",
        "nama": "Higiene Gigi",
        "nama_en": "Dental Hygiene",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Medika",
        "fakultas": "Fakultas Kedokteran Gigi", "fakultas_singkatan": "FKG",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "368",
        "akreditasi_internasional": [],
        "daya_tampung": 50, "dt_snbp": 15, "dt_snbt": 15, "dt_umugm": 20,
        "website": "https://fkg.ugm.ac.id/higiene-gigi",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Pendidikan higienis gigi profesional yang berfokus pada terapi promotif dan preventif kesehatan mulut, manajemen plak, dan edukasi kesehatan gigi komunitas.",
            "en": "Professional dental hygiene education focusing on preventive oral therapy, periodontics scaling, plaque management, and community oral health education."
        },
        "fokus": {
            "id": ["Promotif & Preventif Kesehatan Rongga Mulut", "Terapi Periodontal Non-Bedah", "Edukasi Kebersihan Gigi Komunitas & Sekolah", "Manajemen Sterilisasi Fasilitas Dental"],
            "en": ["Oral Health Promotion & Preventive Therapy", "Non-Surgical Periodontal Debridement", "Community & School Oral Hygiene Education", "Dental Clinic Sterilization & Infection Control"]
        },
        "karir": {
            "id": ["Dental Hygienist di Klinik Gigi Spesialistik", "Promotor Kesehatan Gigi Puskesmas & Dinas Kesehatan", "Manajer Operasional Klinik Kedokteran Gigi", "Pendidik Kesehatan Mulut Masyarakat"],
            "en": ["Registered Dental Hygienist in Specialist Clinics", "Oral Health Educator in Public Health Centers", "Dental Clinic Operations Manager", "Community Oral Hygiene Consultant"]
        }
    },

    # =========================================================================
    # 4. Farmasi - Fakultas Farmasi (ASIIN Accredited)
    # =========================================================================
    {
        "id": "s1-farmasi",
        "kode": "31401",
        "nama": "Farmasi",
        "nama_en": "Pharmacy",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Medika",
        "fakultas": "Fakultas Farmasi", "fakultas_singkatan": "Farmasi",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 240, "dt_snbp": 72, "dt_snbt": 72, "dt_umugm": 96,
        "website": "https://farmasi.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 15.000.000)",
        "deskripsi": {
            "id": "Pendidikan farmasi tertua dan terbaik di Indonesia dengan keunggulan riset fitofarmaka herbal nusantara, farmakoterapi klinik, nanoteknologi formulasi obat, dan bioteknologi farmasi.",
            "en": "Indonesia's oldest and premier pharmacy education leading in standardized phytomedicine, clinical pharmacotherapy, nanotech drug formulation, and pharmaceutical biotechnology."
        },
        "fokus": {
            "id": ["Farmakologi & Farmasi Klinis Rumah Sakit", "Teknologi Formulasi Sediaan Farmasi Maju", "Kimia Medisinal & Penemuan Obat Baru", "Standardisasi Obat Bahan Alam Nusantara"],
            "en": ["Pharmacology & Clinical Pharmacy", "Advanced Pharmaceutical Formulation Tech", "Medicinal Chemistry & Drug Discovery", "Standardization of Natural Herbal Medicines"]
        },
        "karir": {
            "id": ["Apoteker Klinis di Rumah Sakit & Instalasi Farmasi", "Formulator & R&D Scientist Industri Farmasi Global", "Regulatory Affairs & Pengawas Obat BPOM", "Peneliti Biofarmasetika & Produk Biologis"],
            "en": ["Hospital Clinical Pharmacist", "R&D Scientist in Global Pharmaceutical Corporations", "Regulatory Affairs Specialist at FDA / BPOM", "Biopharmaceutical Formulation Researcher"]
        }
    },

    # =========================================================================
    # 5. FT - Fakultas Teknik (ABET, IABEE, JABEE)
    # =========================================================================
    {
        "id": "s1-teknik-sipil",
        "kode": "31501",
        "nama": "Teknik Sipil",
        "nama_en": "Civil Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 180, "dt_snbp": 54, "dt_snbt": 54, "dt_umugm": 72,
        "website": "https://tsipil.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Pendidikan rekayasa sipil berstandar ABET, merancang mega-struktur tahan gempa, pelabuhan, bendungan, bandara, serta sistem transportasi berkelanjutan cerdas.",
            "en": "ABET-accredited civil engineering degree designing earthquake-resilient mega-structures, dams, ports, airports, and smart transportation infrastructure."
        },
        "fokus": {
            "id": ["Rekayasa Struktur Tahan Gempa & BIM", "Geoteknik & Stabilitas Pondasi Dalam", "Teknik Sumber Daya Air & Pengendalian Banjir", "Manajemen Rekayasa Transportasi & Jalan Rel"],
            "en": ["Earthquake Structural Engineering & BIM", "Geotechnical Engineering & Deep Foundations", "Water Resources & Flood Mitigation", "Transportation Systems & Rail Engineering"]
        },
        "karir": {
            "id": ["Senior Structural Engineer di Mega-Proyek Konstruksi", "Project Director di BUMN Karya & Multinasional", "Geotechnical & Tunneling Specialist", "Konsultan Perencana Infrastruktur Transportasi"],
            "en": ["Senior Structural Engineer for Mega-projects", "Infrastructure Construction Project Director", "Geotechnical & Tunneling Specialist", "Transportation Infrastructure Consultant"]
        }
    },
    {
        "id": "s1-arsitektur",
        "kode": "31502",
        "nama": "Arsitektur",
        "nama_en": "Architecture",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["KAAB", "IABEE"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://arsitektur.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Pendidikan arsitektur terakreditasi internasional KAAB yang memadukan kepekaan budaya nusantara, desain parametrik ramah lingkungan, dan efisiensi energi bangunan hijau (net-zero energy building).",
            "en": "KAAB-accredited architectural program synthesizing archipelago vernacular wisdom, parametric biomimicry, and net-zero energy sustainable building design."
        },
        "fokus": {
            "id": ["Desain Arsitektur Tropis Berkelanjutan", "Komputasi Desain & Parametrik BIM", "Konservasi Warisan Arsitektur Nusantara", "Efisiensi Energi Bangunan Hijau (Green Building)"],
            "en": ["Sustainable Tropical Architectural Design", "Computational & Parametric BIM Design", "Archipelago Architectural Heritage Conservation", "Net-Zero Energy & Green Building Performance"]
        },
        "karir": {
            "id": ["Principal Architect di Firma Arsitektur Global", "Green Building Consultant Bersertifikat", "Urban Designer & Masterplanner Kawasan Terpadu", "BIM Specialist & Computational Design Lead"],
            "en": ["Principal Architect at Global Design Studios", "Certified Green Building Consultant", "Urban Masterplanner & District Designer", "BIM Architect & Computational Design Lead"]
        }
    },
    {
        "id": "s1-perencanaan-wilayah-dan-kota",
        "kode": "31503",
        "nama": "Perencanaan Wilayah dan Kota",
        "nama_en": "Urban and Regional Planning",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://pwk.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Kajian komprehensif penataan ruang kota pintar (smart city), ketahanan bencana perkotaan, keadilan spasial, dan perancangan koridor wilayah metropolitan terintegrasi.",
            "en": "Comprehensive study of smart city spatial planning, urban climate resilience, spatial equity, and integrated metropolitan regional growth corridor planning."
        },
        "fokus": {
            "id": ["Perencanaan Kota Cerdas (Smart Cities)", "Ketahanan Iklim & Mitigasi Bencana Spasial", "Sistem Informasi Geografis & Big Data Wilayah", "Manajemen Transportasi Terpadu (TOD)"],
            "en": ["Smart City Analytics & Urban Planning", "Climate Resilience & Spatial Disaster Planning", "Geospatial Big Data & Urban Modeling", "Transit-Oriented Development (TOD) Planning"]
        },
        "karir": {
            "id": ["Perencana Kota & Wilayah di Bappenas / Kementerian ATR", "Urban Planner Masterplan Kawasan Strategis Swasta", "GIS Analyst & Spatial Modeler", "Konsultan Manajemen Transportasi Urban"],
            "en": ["Urban & Regional Planner at National Agencies", "Masterplan Urban Development Lead", "GIS Spatial Data Modeler", "Urban Transportation Policy Consultant"]
        }
    },
    {
        "id": "s1-teknik-mesin",
        "kode": "31504",
        "nama": "Teknik Mesin",
        "nama_en": "Mechanical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 140, "dt_snbp": 42, "dt_snbt": 42, "dt_umugm": 56,
        "website": "https://me.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Pendidikan rekayasa termal dan fluida, desain sistem mekanikal otomasi, konversi energi terbarukan, manufaktur cerdas, dan kendaraan listrik terakreditasi ABET.",
            "en": "ABET-accredited program advancing thermal-fluid sciences, mechanical automation, renewable energy conversion, precision manufacturing, and electric vehicles."
        },
        "fokus": {
            "id": ["Konversi Energi & Sistem Tenaga Terbarukan", "Desain Mekanikal & Analisis Elemen Hingga (FEA)", "Manufaktur Presisi & Mekatronika Robotika", "Teknologi Kendaraan Listrik (Electric Vehicle)"],
            "en": ["Energy Conversion & Renewable Power Systems", "Mechanical Design & Finite Element Analysis", "Precision Manufacturing & Robotics Mechatronics", "Electric Vehicle Powertrain Engineering"]
        },
        "karir": {
            "id": ["Mechanical Design Engineer Industri Alat Berat & Otomotif", "Plant Operations Lead di Pembangkit Energi Terbarukan", "Manufacturing Automation Specialist", "Rotating Equipment Engineer di Sektor Energi"],
            "en": ["Mechanical Design Engineer in Heavy Machinery/Auto", "Renewable Power Plant Operations Lead", "Manufacturing Automation Specialist", "Rotating Equipment Engineer in Energy Fields"]
        }
    },
    {
        "id": "s1-teknik-industri",
        "kode": "31505",
        "nama": "Teknik Industri",
        "nama_en": "Industrial Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 140, "dt_snbp": 42, "dt_snbt": 42, "dt_umugm": 56,
        "website": "https://ti.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Optimasi sistem integral manusia, mesin, material, dan energi berbasis riset operasi lanjutan, ergonomi industri terapan, rantai pasok cerdas, dan rekayasa kualitas digital.",
            "en": "Optimization of integrated human, machine, material, and energy systems utilizing advanced operations research, industrial ergonomics, smart supply chains, and digital quality engineering."
        },
        "fokus": {
            "id": ["Riset Operasi Lanjutan & Optimasi Sistem", "Manajemen Rantai Pasok Global (Global SCM)", "Ergonomi Industri & Keselamatan Kerja (K3)", "Rekayasa Kualitas & Lean Six Sigma Manufaktur"],
            "en": ["Advanced Operations Research & Systems Optimization", "Global Supply Chain Management (SCM)", "Occupational Ergonomics & Safety Engineering", "Quality Engineering & Lean Six Sigma"]
        },
        "karir": {
            "id": ["Supply Chain & Logistics Director di Korporasi Global", "Operations Research Analyst di Industri Big Tech", "Continuous Improvement & Lean Six Sigma Black Belt", "Management Consultant di Firma Konsultasi Strategi"],
            "en": ["Global Supply Chain & Operations Director", "Operations Research Analyst in Big Tech", "Lean Six Sigma Black Belt Improvement Lead", "Strategy Management Consultant"]
        }
    },
    {
        "id": "s1-teknik-kimia",
        "kode": "31506",
        "nama": "Teknik Kimia",
        "nama_en": "Chemical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 150, "dt_snbp": 45, "dt_snbt": 45, "dt_umugm": 60,
        "website": "https://chemeng.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Transformasi material mentah menjadi produk bernilai tambah tinggi melalui reaksi kimia, pemisahan termodinamika, rekayasa bioproses, dan teknologi penangkapan karbon (CCUS).",
            "en": "ABET-accredited chemical engineering program transforming raw materials into high-value products through thermodynamic separation, bioprocess engineering, and carbon capture (CCUS)."
        },
        "fokus": {
            "id": ["Perancangan Pabrik Kimia & Simulasi Aspen Plus", "Teknologi Bioproses & Bioenergi Berkelanjutan", "Termodinamika Pemisahan & Katalisis Industri", "Penangkapan Karbon (CCS/CCUS) & Transisi Bersih"],
            "en": ["Chemical Plant Design & Aspen Process Simulation", "Bioprocess Engineering & Sustainable Biofuels", "Separation Thermodynamics & Heterogeneous Catalysis", "Carbon Capture (CCUS) & Clean Energy Transition"]
        },
        "karir": {
            "id": ["Process Engineer di Industri Petrokimia & Energi", "Plant Operations Lead Fasilitas Pengolahan Gas", "R&D Bioprocess & Renewable Chemicals Lead", "Environmental & Carbon Management Specialist"],
            "en": ["Process Engineer in Petrochemical & Energy", "Gas Processing Facility Operations Lead", "R&D Bioprocess & Renewable Chemicals Lead", "Carbon Management & Environmental Specialist"]
        }
    },
    {
        "id": "s1-teknik-elektro",
        "kode": "31507",
        "nama": "Teknik Elektro",
        "nama_en": "Electrical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 110, "dt_snbp": 33, "dt_snbt": 33, "dt_umugm": 44,
        "website": "https://jteti.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Pendidikan teknik elektro unggulan berstandar ABET yang mencakup smart grid tenaga listrik, elektronika daya, sistem telekomunikasi 5G/6G, dan mikroelektronika semikonduktor.",
            "en": "ABET-accredited electrical engineering focusing on smart electric grids, power electronics, 5G/6G wireless communications, and semiconductor microelectronics."
        },
        "fokus": {
            "id": ["Smart Grid & Integrasi Energi Terbarukan", "Elektronika Daya & Penggerak Motor Listrik", "Sistem Telekomunikasi Nirkabel 5G/6G", "Perancangan Rangkaian Terintegrasi (VLSI)"],
            "en": ["Smart Grid & Renewable Energy Integration", "Power Electronics & EV Motor Drives", "5G/6G Wireless Telecommunications", "VLSI Integrated Circuit Semiconductor Design"]
        },
        "karir": {
            "id": ["Power Systems Engineer di Perusahaan Listrik / PLN", "RF & Telecommunications Network Architect", "Semiconductor & Hardware Design Engineer", "Control & Protection Systems Lead"],
            "en": ["Power Systems Engineer at Electric Utilities", "RF & Wireless Telecommunications Architect", "Hardware & Semiconductor Design Engineer", "Power Grid Automation & Protection Lead"]
        }
    },
    {
        "id": "s1-teknologi-informasi",
        "kode": "31508",
        "nama": "Teknologi Informasi",
        "nama_en": "Information Technology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 110, "dt_snbp": 33, "dt_snbt": 33, "dt_umugm": 44,
        "website": "https://jteti.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Program studi teknologi informasi prestisius terakreditasi ABET, berfokus pada arsitektur komputasi awan, keamanan siber, rekayasa perangkat lunak skala masif, dan sistem cerdas.",
            "en": "Prestigious ABET-accredited IT degree concentrating on enterprise cloud architecture, cybersecurity defense, large-scale software engineering, and intelligent systems."
        },
        "fokus": {
            "id": ["Arsitektur Komputasi Awan Skala Masif", "Keamanan Siber & Pertahanan Jaringan Kritis", "Rekayasa Perangkat Lunak Enterprise & DevOps", "Kecerdasan Artifisial & Pemrosesan Data Cerdas"],
            "en": ["Hyperscale Cloud Systems Architecture", "Cybersecurity & Critical Infrastructure Defense", "Enterprise Software Engineering & DevOps", "Applied Artificial Intelligence & Data Systems"]
        },
        "karir": {
            "id": ["Cloud Infrastructure Lead di Global Tech", "Cybersecurity Specialist & Penetration Tester", "Lead Software Architect di Korporasi FinTech", "DevOps & Platform Engineering Manager"],
            "en": ["Cloud Infrastructure Lead at Global Tech Firms", "Cybersecurity Architect & Security Analyst", "Principal Software Architect in FinTech", "Platform Engineer & DevOps Manager"]
        }
    },
    {
        "id": "s1-teknik-biomedis",
        "kode": "31509",
        "nama": "Teknik Biomedis",
        "nama_en": "Biomedical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://jteti.ugm.ac.id/biomedis",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Integrasi prinsip keteknikan dan ilmu kedokteran untuk menghasilkan instrumentasi medis canggih, pemrosesan sinyal biologis, biomekanika ortopedi, dan citra medis AI.",
            "en": "Integration of engineering principles and medical sciences to develop advanced medical instrumentation, biological signal processing, orthopaedic biomechanics, and medical imaging AI."
        },
        "fokus": {
            "id": ["Instrumentasi Medis & Sensor Fisiologis", "Pemrosesan Citra Medis Berbasis Kecerdasan Buatan", "Biomekanika & Rekayasa Prostesis", "Informatika Medis & Regulasi Alat Kesehatan"],
            "en": ["Medical Instrumentation & Physiological Sensors", "AI-Driven Medical Imaging Diagnostics", "Biomechanics & Prosthetics Engineering", "Healthcare Informatics & Medical Device Compliance"]
        },
        "karir": {
            "id": ["Biomedical Equipment Specialist di Rumah Sakit", "Medical Device R&D Engineer di Korporasi Medis", "Clinical Systems Specialist di Produsen Alat Kesehatan", "Peneliti Bioinstrumentasi Kedokteran"],
            "en": ["Hospital Biomedical Engineering Specialist", "R&D Engineer in Medical Device Corporations", "Clinical Application Specialist (MRI/CT/Ultrasound)", "Bioinstrumentation Research Scientist"]
        }
    },
    {
        "id": "s1-teknik-geodesi",
        "kode": "31510",
        "nama": "Teknik Geodesi",
        "nama_en": "Geodetic Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 140, "dt_snbp": 42, "dt_snbt": 42, "dt_umugm": 56,
        "website": "https://geodesi.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Penentuan posisi spasial presisi tinggi permukaan bumi, geodesi satelit GNSS, fotogrametri drone, survei hidrografi laut, dan pemetaan batas wilayah nasional terakreditasi ABET.",
            "en": "ABET-accredited geodetic engineering determining precise spatial earth positioning, GNSS satellite geodesy, drone photogrammetry, hydrographic surveying, and cadastral mapping."
        },
        "fokus": {
            "id": ["Satelit Geodesi & Penentuan Posisi GNSS", "Fotogrametri Drone LiDAR & Penginderaan Jauh", "Survei Hidrografi & Pemetaan Laut Lepas Pantai", "Kadaster 3D & Sistem Informasi Spasial"],
            "en": ["Satellite Geodesy & GNSS Precision Positioning", "LiDAR UAV Photogrammetry & Remote Sensing", "Offshore Hydrographic Marine Surveying", "3D Cadastre & Spatial Information Systems"]
        },
        "karir": {
            "id": ["Geodetic Surveyor di Industri Konstruksi & Migas", "Spatial Data Architect di Perusahaan Pemetaan Digital", "Surveyor Ahli Kadaster Kementerian ATR/BPN", "Hydrographic Surveyor Eksplorasi Bawah Laut"],
            "en": ["Geodetic Surveyor in Civil Infrastructure/Energy", "Spatial Data Architect in Digital Mapping", "Cadastral Surveyor at National Land Agencies", "Offshore Hydrographic Surveyor"]
        }
    },
    {
        "id": "s1-teknik-geologi",
        "kode": "31511",
        "nama": "Teknik Geologi",
        "nama_en": "Geological Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 140, "dt_snbp": 42, "dt_snbt": 42, "dt_umugm": 56,
        "website": "https://geologi.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Eksplorasi sumber daya bumi (mineral, batubara, geotermal, migas), mitigasi bahaya kegempaan dan gunung api aktif, serta geologi tata lingkungan terakreditasi ABET.",
            "en": "ABET-accredited geological engineering exploring minerals, geothermal, and hydrocarbons, mitigating volcanic and seismic hazards, and engineering environmental geology."
        },
        "fokus": {
            "id": ["Eksplorasi Energi Panas Bumi (Geotermal)", "Geologi Struktur & Tektonika Gunung Api Aktif", "Geoteknik Pondasi & Analisis Kestabilan Lereng", "Hidrogeologi & Pengelolaan Air Tanah"],
            "en": ["Geothermal Energy Exploration", "Structural Geology & Active Volcanotectonics", "Geotechnical Site Investigation & Slope Stability", "Hydrogeology & Groundwater Management"]
        },
        "karir": {
            "id": ["Exploration Geologist di Korporasi Tambang & Energi", "Geothermal Reservoir Geologist", "Engineering Geologist Proyek Infrastruktur Terowongan", "Penyelidik Vulkanologi & Bencana Badan Geologi"],
            "en": ["Exploration Geologist in Mining & Energy", "Geothermal Reservoir Geologist", "Engineering Geologist for Tunnels & Dam Foundations", "Volcanologist at Geological Geological Agencies"]
        }
    },
    {
        "id": "s1-teknik-nuklir",
        "kode": "31512",
        "nama": "Teknik Nuklir",
        "nama_en": "Nuclear Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://tf.ugm.ac.id/nuklir",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Satu-satunya program studi sarjana teknik nuklir di Indonesia yang terakreditasi ABET, berfokus pada keselamatan reaktor daya nuklir, teknologi radiasi medis, dan material maju nuklir.",
            "en": "Indonesia's sole ABET-accredited nuclear engineering degree advancing nuclear power reactor safety, medical radiation technology, and radiation physics."
        },
        "fokus": {
            "id": ["Fisika Reaktor Nuklir & Pembangkit PLTN", "Proteksi Radiasi & Keselamatan Lingkungan", "Aplikasi Radioisotop di Medis & Industri", "Manajemen Bahan Bakar & Limbah Radioaktif"],
            "en": ["Nuclear Reactor Physics & SMR Power Plants", "Radiation Protection & Environmental Safety", "Radioisotope Applications in Medicine & Industry", "Nuclear Fuel Cycle & Radioactive Waste Management"]
        },
        "karir": {
            "id": ["Nuclear Safety Engineer di Badan Tenaga Nuklir", "Medical Physicist di Pusat Terapi Kanker Rumah Sakit", "Radiation Protection Officer (PPR) Industri", "Peneliti Fisika Reaktor di Lembaga Internasional (IAEA)"],
            "en": ["Nuclear Safety Engineer at Regulatory Bodies", "Medical Physicist in Oncology Radiotherapy", "Industrial Radiation Protection Officer", "Reactor Physicist at International Agencies (IAEA)"]
        }
    },
    {
        "id": "s1-teknik-fisika",
        "kode": "31513",
        "nama": "Teknik Fisika",
        "nama_en": "Engineering Physics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Teknik", "fakultas_singkatan": "FT",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 120, "dt_snbp": 36, "dt_snbt": 36, "dt_umugm": 48,
        "website": "https://tf.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.300.000)",
        "deskripsi": {
            "id": "Jembatan sains terapan dan rekayasa industri dalam instrumentasi kontrol otomatis, akustik getaran arsitektural, pengkondisian termal gedung, dan fotonika sensor maju.",
            "en": "ABET-accredited engineering physics synthesizing applied physics and engineering into industrial control instrumentation, architectural acoustics, building thermal systems, and photonics."
        },
        "fokus": {
            "id": ["Instrumentasi Cerdas & Kontrol Otomasi Pabrik", "Fisika Bangunan Hijau & Pengkondisian Termal", "Akustik Ruang & Pengendalian Kebisingan Getaran", "Fotonika & Teknologi Sensor Mutakhir"],
            "en": ["Smart Instrumentation & Factory Automation Control", "Green Building Physics & Thermal Energy Auditing", "Architectural Acoustics & Vibration Control", "Photonics & Advanced Optical Sensors"]
        },
        "karir": {
            "id": ["Automation & Control Systems Engineer", "Building Energy Auditor & Acoustic Consultant", "Instrumentation Lead di Fasilitas Industri Migas", "Sensor Systems & IoT Hardware Engineer"],
            "en": ["Automation & Control Systems Engineer", "Building Energy Auditor & Acoustic Specialist", "Lead Instrumentation Engineer in Energy Facilities", "Sensor Hardware & IoT Solutions Engineer"]
        }
    },

    # =========================================================================
    # 6. FMIPA - Fakultas Matematika dan Ilmu Pengetahuan Alam (ASIIN, RSC)
    # =========================================================================
    {
        "id": "s1-ilmu-komputer",
        "kode": "31601",
        "nama": "Ilmu Komputer",
        "nama_en": "Computer Science",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 27, "dt_umugm": 36,
        "website": "https://dcse.fmipa.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Pendidikan ilmu komputasi fundamental dan terapan berstandar ASIIN, berfokus pada teori algoritma lanjutan, kecerdasan buatan, visi komputer, dan sistem komputasi berkinerja tinggi (HPC).",
            "en": "ASIIN-accredited fundamental computer science focusing on advanced algorithmic theory, artificial intelligence, computer vision, and high-performance computing (HPC)."
        },
        "fokus": {
            "id": ["Kompleksitas Algoritma & Komputasi Teoretis", "Kecerdasan Artifisial & Pemrosesan Bahasa Alami", "Visi Komputer & Pengenalan Pola Citra", "Komputasi Berkinerja Tinggi & Cloud Distributed"],
            "en": ["Algorithmic Complexity & Theoretical Computing", "Artificial Intelligence & NLP", "Computer Vision & Pattern Recognition", "High-Performance Distributed Cloud Computing"]
        },
        "karir": {
            "id": ["Staff / Lead Software Engineer di Global Big Tech", "AI & Machine Learning Research Scientist", "Data Scientist di Korporasi FinTech", "Algorithmic Trader & Quant Analyst"],
            "en": ["Staff / Principal Software Engineer", "AI & Machine Learning Research Scientist", "Data Scientist in FinTech Unicorns", "Quantitative Algorithmic Analyst"]
        }
    },
    {
        "id": "s1-statistika",
        "kode": "31602",
        "nama": "Statistika",
        "nama_en": "Statistics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://math.fmipa.ugm.ac.id/statistika",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Pondasi teori probabilitas, inferensi statistik Bayesian, pemodelan data berdimensi tinggi, pembelajaran mesin statistik, dan peramalan data deret waktu finansial.",
            "en": "Foundation in probability theory, Bayesian statistical inference, high-dimensional analytics, statistical machine learning, and financial time-series forecasting."
        },
        "fokus": {
            "id": ["Statistika Matematika & Inferensi Bayesian", "Analitika Data Besar & Statistical Learning", "Pemodelan Deret Waktu & Peramalan Finansial", "Biostatistika & Rancangan Percobaan Klinis"],
            "en": ["Mathematical Statistics & Bayesian Inference", "Big Data Analytics & Statistical Learning", "Time Series Modeling & Financial Forecasting", "Biostatistics & Clinical Trial Design"]
        },
        "karir": {
            "id": ["Lead Data Scientist di Industri Perbankan / Tech", "Statistical Modeler di Lembaga Survei & Riset", "Risk Modeler & Credit Scoring Specialist", "Biostatistician di Riset Farmasi"],
            "en": ["Principal Data Scientist in Banking/Tech", "Statistical Research Modeler", "Credit Risk & Actuarial Modeler", "Clinical Trial Biostatistician"]
        }
    },
    {
        "id": "s1-matematika",
        "kode": "31603",
        "nama": "Matematika",
        "nama_en": "Mathematics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://math.fmipa.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Penguasaan logika matematika murni dan komputasi terapan, analisis fungsional, aljabar abstrak, kriptografi bilangan, dan pemodelan dinamika sistem kontinu.",
            "en": "Mastery of pure mathematics and applied computation, functional analysis, abstract algebra, cryptographic number theory, and dynamical system modeling."
        },
        "fokus": {
            "id": ["Aljabar Abstrak & Kriptografi Matematika", "Analisis Fungsional & Persamaan Diferensial", "Matematika Keuangan & Valuasi Derivatif", "Optimasi Numerik & Riset Operasi"],
            "en": ["Abstract Algebra & Post-Quantum Cryptography", "Functional Analysis & Differential Equations", "Financial Mathematics & Derivatives Valuation", "Numerical Optimization & Combinatorics"]
        },
        "karir": {
            "id": ["Kriptografer & Keamanan Siber Teoretis", "Quantitative Financial Analyst (Quant)", "Dosen & Peneliti Matematika Murni", "Operations Research Modeler Industri Logistik"],
            "en": ["Cryptographer in Cybersecurity Labs", "Quantitative Finance Researcher (Quant)", "Pure Mathematics Academic / Researcher", "Operations Research Modeler"]
        }
    },
    {
        "id": "s1-aktuaria",
        "kode": "31604",
        "nama": "Aktuaria",
        "nama_en": "Actuarial Science",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://aktuaria.fmipa.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Aplikasi matematika dan statistika untuk mengevaluasi dan memitigasi risiko finansial pada asuransi jiwa, dana pensiun, investasi, dan jaminan sosial nasional.",
            "en": "Application of mathematical and statistical models to quantify and mitigate financial risk in life insurance, pension funds, investment portfolios, and social security."
        },
        "fokus": {
            "id": ["Matematika Asuransi Jiwa & Kesehatan", "Teori Risiko Finansial & Solvensi Dana Pensiun", "Model Stokastik Aktuaria & Valuasi Cadangan", "Enterprise Risk Management (ERM) Korporasi"],
            "en": ["Life & Health Actuarial Mathematics", "Pension Solvency & Financial Risk Theory", "Stochastic Actuarial Reserving Models", "Enterprise Risk Management (ERM)"]
        },
        "karir": {
            "id": ["Aksuaris Tersertifikasi (FSAI / ASAI)", "Valuation Actuary di Perusahaan Asuransi Multinasional", "Pension Fund & Investment Risk Consultant", "Analis Risiko Finansial Otoritas Jasa Keuangan (OJK)"],
            "en": ["Fellow / Associate Certified Actuary (FSAI)", "Valuation Actuary in Global Insurance Groups", "Pension & Investment Risk Consultant", "Financial Solvency Analyst at OJK / Regulators"]
        }
    },
    {
        "id": "s1-kimia",
        "kode": "31605",
        "nama": "Kimia",
        "nama_en": "Chemistry",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["RSC", "ASIIN"],
        "daya_tampung": 140, "dt_snbp": 42, "dt_snbt": 42, "dt_umugm": 56,
        "website": "https://chem.fmipa.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Pendidikan kimia terakreditasi Royal Society of Chemistry (RSC) Britania Raya, berfokus pada sintesis material maju, kimia komputasi, nanokatalis hijau, dan analitika lingkungan.",
            "en": "Royal Society of Chemistry (RSC) accredited program pioneering advanced materials synthesis, computational chemistry, green nanocatalysis, and environmental analysis."
        },
        "fokus": {
            "id": ["Sintesis Nanomaterial & Polimer Fungsional", "Kimia Komputasi & Pemodelan Molekuler", "Katalisis Hijau & Energi Bersih", "Kimia Analisis Forensik & Instrumen Spektrometri"],
            "en": ["Functional Nanomaterials & Polymers", "Computational Chemistry & Molecular Modeling", "Green Catalysis & Clean Energy", "Forensic Analytical Chemistry & Spectrometry"]
        },
        "karir": {
            "id": ["R&D Chemist di Industri Manufaktur & Kosmetik", "Analytical Laboratory Manager Terakreditasi ISO", "Peneliti Material Baru di BRIN / Lembaga Riset", "Quality Assurance & Formulator Specialist"],
            "en": ["R&D Chemist in Global Consumer Goods/Cosmetics", "Analytical Testing Laboratory Manager", "Advanced Materials Scientist at Research Labs", "Formulation & Quality Assurance Specialist"]
        }
    },
    {
        "id": "s1-fisika",
        "kode": "31606",
        "nama": "Fisika",
        "nama_en": "Physics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://physics.fmipa.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Pemahaman hukum-hukum fundamental alam semesta, mekanika kuantum, fisika zat padat, superkonduktivitas, dan eksperimen fisika nuklir terapan.",
            "en": "Comprehension of fundamental physical laws, quantum mechanics, condensed matter physics, superconductivity, and applied particle physics experimentation."
        },
        "fokus": {
            "id": ["Mekanika Kuantum & Komputasi Kuantum", "Fisika Zat Padat & Semikonduktor Maju", "Fisika Nuklir & Partikel Elementer", "Eksperimen Fisika Material Termal"],
            "en": ["Quantum Mechanics & Quantum Computing", "Solid-State & Semiconductor Physics", "Nuclear & Elementary Particle Physics", "Experimental Materials Physics"]
        },
        "karir": {
            "id": ["Research Scientist di Lembaga Fisika & Antariksa", "Semiconductor Fabrication Engineer", "Data Scientist & Scientific Software Developer", "Dosen & Pengajar Fisika Perguruan Tinggi"],
            "en": ["Research Scientist in Space & Physics Institutes", "Semiconductor Process Engineer", "Scientific Software Developer & Data Analyst", "University Physics Academic"]
        }
    },
    {
        "id": "s1-geofisika",
        "kode": "31607",
        "nama": "Geofisika",
        "nama_en": "Geophysics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://geofisika.fmipa.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Eksplorasi bawah permukaan bumi menggunakan metode seismik, gravitasi, magnetik, dan elektromagnetik untuk identifikasi energi panas bumi, migas, dan mitigasi gempa bumi.",
            "en": "Subsurface exploration utilizing seismic, gravity, magnetic, and electromagnetic methods for geothermal reservoirs, energy, and earthquake hazard mitigation."
        },
        "fokus": {
            "id": ["Pengolahan Data Seismik & Inversi 3D", "Eksplorasi Geotermal & Hidrokarbon", "Metode Elektromagnetik & Magnetotellurik", "Seismologi Gempa Bumi & Mitigasi Tsunami"],
            "en": ["Seismic Data Processing & 3D Inversion", "Geothermal & Hydrocarbon Geophysical Surveying", "Magnetotelluric & Electromagnetic Methods", "Earthquake Seismology & Tsunami Risk Assessment"]
        },
        "karir": {
            "id": ["Exploration Geophysicist di Perusahaan Energi", "Seismic Data Processing Specialist", "Analis Seismologi BMKG / Pusat Gempa Nasional", "Near-Surface Geotechnical Geophysicist"],
            "en": ["Exploration Geophysicist in Energy Firms", "Seismic Data Processing & Imaging Specialist", "Seismologist at Disaster Monitoring Agencies", "Near-Surface Geotechnical Surveyor"]
        }
    },
    {
        "id": "s1-elektronika-dan-instrumentasi",
        "kode": "31608",
        "nama": "Elektronika dan Instrumentasi",
        "nama_en": "Electronics and Instrumentation (Elins)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://dcse.fmipa.ugm.ac.id/elins",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Sinergi mikrokontroler terbenam (embedded systems), Internet of Things (IoT), robotika otonom, sistem instrumentasi industri cerdas, dan pengolahan sinyal digital.",
            "en": "Synergy of embedded microcontrollers, Internet of Things (IoT), autonomous robotics, intelligent industrial instrumentation, and digital signal processing."
        },
        "fokus": {
            "id": ["Sistem Komputasi Terbenam (Embedded Systems)", "Internet of Things (IoT) & Sensor Nirkabel", "Robotika Otonom & Kontrol Cerdas", "Instrumentasi Kalibrasi Industri Otomatis"],
            "en": ["Embedded Systems & Microcontroller Firmware", "Internet of Things (IoT) & Smart Sensing", "Autonomous Robotics & Intelligent Control", "Automated Industrial Calibration Systems"]
        },
        "karir": {
            "id": ["Embedded Firmware Engineer di Industri Elektronika", "Robotics & Automation Engineer Pabrik Pintar", "IoT Solution Architect di Perusahaan Teknologi", "Instrument Engineer di Sektor Manufaktur"],
            "en": ["Embedded Firmware Engineer in Electronics", "Robotics & Smart Factory Automation Engineer", "IoT Solutions Architect in Tech Enterprises", "Instrumentation Systems Specialist"]
        }
    },

    # =========================================================================
    # 7. FH - Fakultas Hukum (AUN-QA Accredited)
    # =========================================================================
    {
        "id": "s1-hukum",
        "kode": "31701",
        "nama": "Hukum",
        "nama_en": "Law / Jurisprudence",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Hukum", "fakultas_singkatan": "FH",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "390",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 330, "dt_snbp": 99, "dt_snbt": 99, "dt_umugm": 132,
        "website": "https://law.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Fakultas hukum paling disegani di Indonesia yang mencetak hakim agung, praktisi hukum korporasi, perancang undang-undang, diplomat, dan advokat berintegritas tinggi.",
            "en": "Indonesia's foremost law school cultivating supreme court justices, corporate legal counsels, legislative drafters, diplomats, and ethical advocates."
        },
        "fokus": {
            "id": ["Hukum Bisnis Korporasi & Transaksi Internasional", "Hukum Tata Negara & Kebijakan Konstitusi", "Hukum Pidana & Keadilan Restoratif", "Hukum Internasional & Penyelesaian Sengketa"],
            "en": ["Corporate Business Law & Cross-Border Deals", "Constitutional Law & Governance Policy", "Criminal Justice & Restorative Rights", "Public International Law & Dispute Resolution"]
        },
        "karir": {
            "id": ["Corporate Lawyer di Top Tier Law Firms", "In-House Legal Counsel Korporasi Multinasional", "Hakim / Jaksa di Lembaga Peradilan Nasional", "Legal Drafter di Kementerian & Lembaga Negara"],
            "en": ["Corporate Attorney at Top Tier Law Firms", "In-House Legal Counsel in Multinational Firms", "Judge / Public Prosecutor in Judicial Systems", "Legislative & Policy Drafter in Government"]
        }
    },

    # =========================================================================
    # 8. FISIPOL - Fakultas Ilmu Sosial dan Ilmu Politik
    # =========================================================================
    {
        "id": "s1-ilmu-hubungan-internasional",
        "kode": "31801",
        "nama": "Ilmu Hubungan Internasional",
        "nama_en": "International Relations",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Sosial dan Ilmu Politik", "fakultas_singkatan": "FISIPOL",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://hi.fisipol.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Kajian diplomasi global, ekonomi politik internasional, keamanan transnasional, hukum humaniter, dan negosiasi multilateral pencetak diplomat ulung Indonesia.",
            "en": "Rigorous study of global diplomacy, international political economy, transnational security, multilateral negotiations, and strategic foreign policy."
        },
        "fokus": {
            "id": ["Diplomasi Pertahanan & Keamanan Transnasional", "Ekonomi Politik Global & Perdagangan Dunia", "Tata Kelola Global & Organisasi Internasional", "Studi Kawasan Strategis Indo-Pasifik"],
            "en": ["Defense Diplomacy & Global Security", "International Political Economy & Global Trade", "Global Governance & Multilateral Organizations", "Indo-Pacific Regional Geopolitical Studies"]
        },
        "karir": {
            "id": ["Diplomat di Kementerian Luar Negeri RI", "International Officer di Badan PBB (UN / UNESCO)", "Geopolitical Risk Analyst Firma Konsultan Global", "Program Manager di Lembaga NGO Internasional"],
            "en": ["Foreign Service Diplomat at Ministry of Foreign Affairs", "International Civil Servant at United Nations", "Geopolitical Risk Analyst in Strategic Consultancies", "International NGO Program Director"]
        }
    },
    {
        "id": "s1-ilmu-komunikasi",
        "kode": "31802",
        "nama": "Ilmu Komunikasi",
        "nama_en": "Communication Studies",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Sosial dan Ilmu Politik", "fakultas_singkatan": "FISIPOL",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://komunikasi.fisipol.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Analisis komunikasi media digital, jurnalisme investigatif multiplatform, hubungan masyarakat strategis, dan studi kritis budaya media massa kontemporer.",
            "en": "Analysis of digital media communications, multi-platform investigative journalism, strategic public relations, and contemporary media cultural studies."
        },
        "fokus": {
            "id": ["Komunikasi Korporasi & Strategic PR", "Media Digital & Manajemen Konten Interaktif", "Jurnalisme Data & Produksi Media Multiplatform", "Komunikasi Kebijakan Publik & Advokasi"],
            "en": ["Corporate Communications & Strategic PR", "Digital Media Ecosystems & Content Strategy", "Data Journalism & Multi-platform Broadcasting", "Public Policy Communication & Civic Advocacy"]
        },
        "karir": {
            "id": ["Head of Corporate Communications di Unicorn/Multinasional", "Digital Content Director di Media Global", "Public Relations Strategist & Media Spokesperson", "Jurnalis Investigasi Data Terkemuka"],
            "en": ["Corporate Communications Director", "Digital Content Director in Global Media", "Strategic PR & Crisis Communications Lead", "Data Investigative Journalist"]
        }
    },
    {
        "id": "s1-manajemen-dan-kebijakan-publik",
        "kode": "31803",
        "nama": "Manajemen dan Kebijakan Publik",
        "nama_en": "Public Policy and Management (MKP)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Sosial dan Ilmu Politik", "fakultas_singkatan": "FISIPOL",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://mkp.fisipol.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Formulasi, implementasi, dan evaluasi kebijakan publik berbasis bukti (evidence-based policy), tata kelola birokrasi reformis, dan inovasi pelayanan publik digital.",
            "en": "Evidence-based public policy formulation, evaluation, transformative bureaucratic reform governance, and digital public sector innovation."
        },
        "fokus": {
            "id": ["Formulasi & Analisis Kebijakan Berbasis Bukti", "Reformasi Birokrasi & Tata Kelola Digital", "Evaluasi Dampak Kebijakan Sosial Publik", "Manajemen Pelayanan Publik Berkelanjutan"],
            "en": ["Evidence-Based Policy Formulation & Analysis", "Bureaucratic Reform & Digital Governance", "Social Impact Evaluation of Public Interventions", "Sustainable Public Sector Management"]
        },
        "karir": {
            "id": ["Policy Analyst di Kementerian / Lembaga Negara", "Program Manager di Lembaga Think Tank & Riset", "ESG & Public Sector Consultant di Firma Global", "Pegawai Negeri Sipil / Aparatur Sipil Negara Berprestasi"],
            "en": ["Public Policy Analyst in Government Ministries", "Think Tank Policy Research Director", "ESG & Public Sector Advisory Consultant", "Civil Service Leadership Officer"]
        }
    },
    {
        "id": "s1-politik-dan-pemerintahan",
        "kode": "31804",
        "nama": "Politik dan Pemerintahan",
        "nama_en": "Politics and Government",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Sosial dan Ilmu Politik", "fakultas_singkatan": "FISIPOL",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": [],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://dpp.fisipol.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Studi dinamika kekuasaan politik, tata kelola pemerintahan daerah, partai politik dan pemilu demokratis, serta gerakan masyarakat sipil kontemporer.",
            "en": "Study of political power dynamics, regional governance autonomy, electoral democracy systems, and contemporary civil society movements."
        },
        "fokus": {
            "id": ["Tata Kelola Pemerintahan Daerah & Otonomi", "Sistem Kepartaian & Perilaku Pemilih Pemilu", "Resolusi Konflik & Demokrasi Deliberatif", "Politik Sumber Daya Alam & Lingkungan"],
            "en": ["Regional Governance & Decentralization Policy", "Party Politics & Electoral Behavior", "Conflict Resolution & Deliberative Democracy", "Natural Resource & Environmental Politics"]
        },
        "karir": {
            "id": ["Analis Politik di Lembaga Riset & Survei Nasional", "Konsultan Tata Kelola Pemerintahan Daerah", "Spesialis Riset Parlemen di DPR / DPD RI", "Aktivis Demokrasi & Hak Asasi Manusia"],
            "en": ["National Political Analyst & Polling Researcher", "Local Government Governance Advisor", "Parliamentary Legislative Research Specialist", "Democratic Governance & Human Rights Advocate"]
        }
    },

    # =========================================================================
    # 9. FPsi - Fakultas Psikologi (AUN-QA Accredited)
    # =========================================================================
    {
        "id": "s1-psikologi",
        "kode": "31901",
        "nama": "Psikologi",
        "nama_en": "Psychology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Psikologi", "fakultas_singkatan": "FPsi",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 240, "dt_snbp": 72, "dt_snbt": 72, "dt_umugm": 96,
        "website": "https://psikologi.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Pendidikan psikologi terkemuka di Asia Tenggara yang mempelajari perilaku manusia, proses mental kognitif, psikologi industri dan organisasi, serta intervensi kesehatan mental.",
            "en": "Southeast Asia's leading psychology program studying human behavior, cognitive mental processes, organizational psychology, and evidence-based mental health interventions."
        },
        "fokus": {
            "id": ["Psikologi Industri & Pengembangan Organisasi (PIO)", "Psikometri & Konstruksi Tes Psikologis", "Psikologi Klinis & Konseling Kesehatan Mental", "Psikologi Perkembangan & Pendidikan Anak"],
            "en": ["Industrial & Organizational Psychology (I/O)", "Psychometrics & Psychological Test Construction", "Clinical Psychology & Mental Wellbeing Counseling", "Developmental & Educational Psychology"]
        },
        "karir": {
            "id": ["Human Resources (HR) Director di Perusahaan Multinasional", "People & Culture Lead di Ekosistem Startup Tech", "Asisten Psikolog & Konsultan Asesmen Talenta", "Peneliti Perilaku Konsumen (Consumer Insights Lead)"],
            "en": ["Head of Human Resources in Global Corporations", "People & Culture Lead in Tech Companies", "Psychological Assessment & Talent Consultant", "Consumer Behavior & Behavioral Insights Lead"]
        }
    },

    # =========================================================================
    # 10. Fakultas Biologi (ASIIN Accredited)
    # =========================================================================
    {
        "id": "s1-biologi",
        "kode": "32001",
        "nama": "Biologi",
        "nama_en": "Biology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Biologi", "fakultas_singkatan": "Biologi",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 220, "dt_snbp": 66, "dt_snbt": 66, "dt_umugm": 88,
        "website": "https://biologi.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Eksplorasi megabiodiversitas nusantara berstandar internasional ASIIN, mencakup biologi molekuler genomik, bioteknologi rekayasa genetika, bioinformatika, dan konservasi hayati.",
            "en": "ASIIN-accredited biological science exploring mega-biodiversity, molecular genomics, genetic engineering biotechnology, bioinformatics, and ecological conservation."
        },
        "fokus": {
            "id": ["Biologi Molekuler & Rekayasa Genomik", "Bioteknologi Lingkungan & Mikroba Fungsional", "Bioinformatika & Analisis Data DNA/RNA", "Ekologi Konservasi & Megabiodiversitas Tropis"],
            "en": ["Molecular Biology & Genomic Engineering", "Environmental Biotechnology & Microbial Systems", "Bioinformatics & Genomic Sequence Analytics", "Tropical Conservation Ecology & Biodiversity"]
        },
        "karir": {
            "id": ["Biotechnologist di Industri Farmasi & Agribisnis", "Bioinformatics Analyst di Laboratorium Genomik", "Conservation Scientist di Taman Nasional & NGO Lingkungan", "Peneliti Biologi Terapan di BRIN / Lembaga Riset"],
            "en": ["Biotechnologist in Pharma & Agribusiness", "Bioinformatics Scientist in Genomic Labs", "Wildlife & Ecological Conservation Director", "Applied Biology Researcher at National Labs"]
        }
    },

    # =========================================================================
    # 11. Fakultas Pertanian (ASIIN Accredited)
    # =========================================================================
    {
        "id": "s1-agronomi",
        "kode": "32101",
        "nama": "Agronomi",
        "nama_en": "Agronomy",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Pertanian", "fakultas_singkatan": "Pertanian",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://faperta.ugm.ac.id/agronomi",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Pemuliaan tanaman unggul, fisiologi tanaman budidaya, pertanian presisi berbasis sensor cerdas, dan peningkatan produktivitas tanaman pangan strategis.",
            "en": "ASIIN-accredited agronomy optimizing crop breeding, plant physiology, smart sensor precision farming, and strategic food crop yield enhancement."
        },
        "fokus": {
            "id": ["Pemuliaan Tanaman & Genetika Varietas Unggul", "Fisiologi Tanaman & Nutrisi Lahan Budidaya", "Pertanian Presisi (Precision Smart Agriculture)", "Manajemen Perkebunan Berkelanjutan"],
            "en": ["Crop Breeding & Superior Cultivar Genetics", "Crop Physiology & Soil Fertility Nutrition", "Smart Precision Farming & Sensor Tech", "Sustainable Plantation Management"]
        },
        "karir": {
            "id": ["Agronomist Lead di Perusahaan Perkebunan Global", "Plant Breeder & Seed Production Manager", "Smart Agriculture Consultant di AgTech Startup", "Peneliti Pertanian Pangan Kementan / BRIN"],
            "en": ["Lead Agronomist in Global Plantation Groups", "Plant Breeding & Hybrid Seed Manager", "Smart Precision Farming Consultant", "Agricultural Crop Researcher in National Agencies"]
        }
    },
    {
        "id": "s1-ekonomi-pertanian-dan-agribisnis",
        "kode": "32102",
        "nama": "Ekonomi Pertanian dan Agribisnis",
        "nama_en": "Agricultural Economics and Agribusiness",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Pertanian", "fakultas_singkatan": "Pertanian",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://faperta.ugm.ac.id/agribisnis",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Manajemen rantai pasok komoditas pertanian, valuasi ekonomi sumber daya pedesaan, perdagangan komoditas berjangka, dan kewirausahaan agribisnis modern.",
            "en": "Agricultural commodity supply chain governance, rural resource economics valuation, futures commodity trading, and modern agribusiness entrepreneurship."
        },
        "fokus": {
            "id": ["Manajemen Rantai Nilai Agribisnis Terpadu", "Ekonomi Pembangunan Pertanian Pedesaan", "Perdagangan Komoditas & Pemasaran Global", "Analisis Kelayakan Finansial Usaha Tani"],
            "en": ["Integrated Agribusiness Value Chain Management", "Rural Agricultural Development Economics", "Global Commodity Trading & Export Marketing", "Agribusiness Financial Feasibility Analytics"]
        },
        "karir": {
            "id": ["Supply Chain Manager di Korporasi Makanan & Agribisnis", "Agricultural Credit Specialist di Bank BUMN", "Commodity Trading & Market Analyst", "Wirausahawan Inovasi Produk Pertanian Modern"],
            "en": ["Supply Chain Manager in Food Corporations", "Agricultural Credit & Finance Officer in Banks", "Commodity Trader & Market Analyst", "Modern Agribusiness Startup Founder"]
        }
    },
    {
        "id": "s1-akuakultur",
        "kode": "32103",
        "nama": "Akuakultur (Budidaya Perikanan)",
        "nama_en": "Aquaculture",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Pertanian", "fakultas_singkatan": "Pertanian",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://perikanan.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Rekayasa budidaya biota perairan tawar, payau, dan laut berwawasan lingkungan, teknologi bioflok, nutrisi pakan ikan, dan penanggulangan penyakit akuatik.",
            "en": "Sustainable engineering of freshwater and marine aquaculture, biofloc technology, aquatic animal nutrition, and fish pathology management."
        },
        "fokus": {
            "id": ["Teknologi Budidaya Perairan Berkelanjutan (Bioflok)", "Nutrisi Pakan & Formulasi Pakan Akuatik", "Kesehatan Ikan & Pengendalian Penyakit Udang", "Genetika & Pemuliaan Induk Ikan Unggul"],
            "en": ["Sustainable Aquaculture Systems (Biofloc/RAS)", "Aquatic Feed Formulation & Fish Nutrition", "Fish Pathology & Shrimp Disease Control", "Fish Breeding Genetics & Hatchery Management"]
        },
        "karir": {
            "id": ["Aquaculture Production Manager Tambak Modern", "Formulator Pakan Ikan & Udang Korporasi Pakan", "Hatchery Specialist & Quality Inspector Perikanan", "Analis Kebijakan Perikanan Budidaya KKP"],
            "en": ["Aquaculture Farm Operations Manager", "Aquatic Feed Formulator in Feed Corporations", "Hatchery Specialist & Aquaculture Inspector", "Aquaculture Policy Analyst at Fisheries Ministry"]
        }
    },

    # =========================================================================
    # 12. Fakultas Kehutanan
    # =========================================================================
    {
        "id": "s1-kehutanan",
        "kode": "32201",
        "nama": "Kehutanan",
        "nama_en": "Forestry",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Kehutanan", "fakultas_singkatan": "Kehutanan",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 300, "dt_snbp": 90, "dt_snbt": 90, "dt_umugm": 120,
        "website": "https://fkt.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Fakultas kehutanan almamater Presiden RI, memimpin pengelolaan hutan tropis lestari, konservasi satwa liar, teknologi hasil hutan ramah lingkungan, dan perdagangan kredit karbon hutan.",
            "en": "Indonesia's apex forestry faculty leading sustainable tropical forest management, biodiversity conservation, sustainable timber technology, and forest carbon credit offsets."
        },
        "fokus": {
            "id": ["Silvikultur & Pemulihan Ekosistem Hutan Tropis", "Konservasi Sumber Daya Hutan & Ekowisata", "Teknologi Biomassa Kayu & Hasil Hutan Bukan Kayu", "Perdagangan Karbon Hutan & Sertifikasi Lestari"],
            "en": ["Tropical Silviculture & Ecological Restoration", "Forest Conservation & Wildlife Management", "Wood Biomass Tech & Non-Timber Forest Products", "Forest Carbon Offsets & Global FSC Certification"]
        },
        "karir": {
            "id": ["Forestry Operations Director di Korporasi Konsesi Hutan", "Carbon Project Developer di Pasar Karbon Global", "Wildlife Conservation Officer di WWF / Lembaga Konservasi", "Pengendali Ekosistem Hutan di Kementerian LHK"],
            "en": ["Forestry Concession Operations Director", "Forest Carbon Project Developer (VCS/Verra)", "Conservation Officer at WWF / National Parks", "Forest Ecosystem Specialist at Environment Ministry"]
        }
    },

    # =========================================================================
    # 13. Fakultas Peternakan (ASIIN Accredited)
    # =========================================================================
    {
        "id": "s1-ilmu-dan-industri-peternakan",
        "kode": "32301",
        "nama": "Ilmu dan Industri Peternakan",
        "nama_en": "Animal Science and Industry",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Peternakan", "fakultas_singkatan": "Peternakan",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 300, "dt_snbp": 90, "dt_snbt": 90, "dt_umugm": 120,
        "website": "https://fapet.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Pendidikan peternakan terakreditasi ASIIN yang berfokus pada teknologi nutrisi pakan ternak tropis, pemuliaan genetik ternak, teknologi pengolahan hasil ternak (susu, daging, telur), dan agribisnis peternakan modern.",
            "en": "ASIIN-accredited animal science advancing tropical livestock nutrition, breeding genetics, dairy and meat processing technology, and modern livestock agribusiness."
        },
        "fokus": {
            "id": ["Nutrisi & Bioteknologi Pakan Ternak", "Pemuliaan Ternak & Reproduksi Inseminasi Buatan", "Teknologi Pengolahan Daging & Susu Higienis", "Manajemen Industri Peternakan Cerdas (Smart Farm)"],
            "en": ["Livestock Feed Nutrition & Biotechnology", "Animal Breeding Genetics & Artificial Insemination", "Dairy and Meat Processing Hygiene Technology", "Smart Livestock Farming Systems Management"]
        },
        "karir": {
            "id": ["Farm Manager di Peternakan Skala Industri", "Nutrisionis & Formulator Pakan di Korporasi Feedmill", "R&D Specialist Industri Produk Olahan Daging/Susu", "Wirausahawan Agribisnis Peternakan Terpadu"],
            "en": ["Commercial Livestock Farm Operations Manager", "Animal Feed Nutritionist in Feedmill Corporations", "Dairy & Meat Processing R&D Specialist", "Integrated Livestock Agribusiness Founder"]
        }
    },

    # =========================================================================
    # 14. FTP - Fakultas Teknologi Pertanian (IABEE, IFT)
    # =========================================================================
    {
        "id": "s1-teknik-pertanian",
        "kode": "32401",
        "nama": "Teknik Pertanian",
        "nama_en": "Agricultural Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Teknologi Pertanian", "fakultas_singkatan": "FTP",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 100, "dt_snbp": 30, "dt_snbt": 30, "dt_umugm": 40,
        "website": "https://tpb.tp.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Mekanisasi dan otomatisasi alat mesin pertanian, rekayasa irigasi hemat air, bangunan pertanian cerdas (greenhouse), dan sistem robotika penanganan hasil panen.",
            "en": "Agricultural machinery automation, precision irrigation engineering, smart climate-controlled greenhouses, and robotic post-harvest handling."
        },
        "fokus": {
            "id": ["Traktor & Mekanisasi Alat Mesin Pertanian", "Rekayasa Irigasi Presisi & Sumber Daya Air", "Bangunan Pertanian Cerdas & Controlled Greenhouse", "Sistem Penanganan Pascapanen Berkelanjutan"],
            "en": ["Agricultural Machinery & Autonomous Tractors", "Precision Irrigation & Soil Water Engineering", "Smart Controlled-Environment Greenhouses", "Post-Harvest Machinery & Systems Engineering"]
        },
        "karir": {
            "id": ["Agricultural Machinery Engineer di Produsen Alsintan", "Irrigation & Water Management Engineer", "Greenhouse Climate & Automation Specialist", "Konsultan Mekanisasi Perkebunan Modern"],
            "en": ["Agricultural Machinery Design Engineer", "Precision Irrigation Systems Specialist", "Commercial Greenhouse Automation Engineer", "Plantation Mechanization Consultant"]
        }
    },
    {
        "id": "s1-teknologi-pangan-dan-hasil-pertanian",
        "kode": "32402",
        "nama": "Teknologi Pangan dan Hasil Pertanian",
        "nama_en": "Food Technology and Agricultural Products",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Teknologi Pertanian", "fakultas_singkatan": "FTP",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["IFT", "IABEE"],
        "daya_tampung": 110, "dt_snbp": 33, "dt_snbt": 33, "dt_umugm": 44,
        "website": "https://tip.tp.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Pengembangan teknologi pengolahan pangan bermutu internasional (IFT Approved), mikrobiologi pangan, kimia cita rasa, jaminan mutu HACCP, dan formulasi pangan fungsional.",
            "en": "Institute of Food Technologists (IFT) approved program mastering advanced food processing, sensory science, HACCP safety certification, and functional food formulation."
        },
        "fokus": {
            "id": ["Pengolahan & Pengawetan Pangan Modern", "Kimia Pangan & Analisis Cita Rasa (Flavor)", "Keamanan Pangan & Sistem Jaminan Mutu HACCP", "Mikrobiologi Fermentasi Pangan Fungsional"],
            "en": ["Thermal & Non-Thermal Food Processing", "Food Chemistry & Sensory Flavor Analytics", "Food Safety Standards & HACCP Quality Systems", "Fermentation Biotechnology & Functional Foods"]
        },
        "karir": {
            "id": ["Food Product Developer (R&D) di Korporasi FMCG", "Quality Assurance & Food Safety Manager", "Sensory & Consumer Science Specialist", "Regulatory Affairs Specialist Industri Pangan"],
            "en": ["Food Product R&D Scientist in Global FMCG", "Quality Assurance & Food Safety Manager", "Sensory Scientist & Flavor Technologist", "Food Standards Regulatory Affairs Manager"]
        }
    },

    # =========================================================================
    # 15. FKH - Fakultas Kedokteran Hewan (ASIIN Accredited)
    # =========================================================================
    {
        "id": "s1-kedokteran-hewan",
        "kode": "32501",
        "nama": "Kedokteran Hewan",
        "nama_en": "Veterinary Medicine",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Medika",
        "fakultas": "Fakultas Kedokteran Hewan", "fakultas_singkatan": "FKH",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "388",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 200, "dt_snbp": 60, "dt_snbt": 60, "dt_umugm": 80,
        "website": "https://fkh.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 15.000.000)",
        "deskripsi": {
            "id": "Pendidikan dokter hewan berstandar internasional ASIIN yang mencakup diagnosis penyakit hewan kecil, ternak besar, satwa liar eksotis, zoonosis, dan ketahanan kesehatan One Health.",
            "en": "ASIIN-accredited veterinary medicine covering small animal clinical practice, large livestock medicine, wildlife diagnostics, zoonotic disease control, and One Health global frameworks."
        },
        "fokus": {
            "id": ["Kedokteran Hewan Klinis & Bedah Hewan Kecil", "Penyakit Menular Zoonosis & Pendekatan One Health", "Kesehatan Sapi Perah & Ternak Produktif", "Konservasi & Penanganan Medis Satwa Liar"],
            "en": ["Small Animal Clinical Practice & Surgery", "Zoonotic Infectious Diseases & One Health", "Large Livestock & Dairy Herd Health", "Exotic Wildlife Diagnostics & Conservation Medicine"]
        },
        "karir": {
            "id": ["Dokter Hewan Praktisi Klinik Hewan & Rumah Sakit", "Veterinary Epidemiologist Balai Karantina Pertanian", "Veterinarian Satwa Liar di Kebun Binatang & Taman Nasional", "Technical Services Manager Industri Farmasi Hewan"],
            "en": ["Veterinary Clinical Practitioner & Hospital Surgeon", "Veterinary Quarantine & Epidemiological Officer", "Wildlife Veterinarian in Conservation Zoos", "Animal Health Technical Manager in Animal Pharma"]
        }
    },

    # =========================================================================
    # 16. Fakultas Geografi (ASIIN Accredited)
    # =========================================================================
    {
        "id": "s1-geografi-lingkungan",
        "kode": "32601",
        "nama": "Geografi Lingkungan",
        "nama_en": "Environmental Geography",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Geografi", "fakultas_singkatan": "Geografi",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 100, "dt_snbp": 30, "dt_snbt": 30, "dt_umugm": 40,
        "website": "https://geo.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Analisis geomorfologi lingkungan, hidrologi daerah aliran sungai (DAS), dinamika perubahan iklim, mitigasi bencana ekologis, dan analisis dampak lingkungan (AMDAL).",
            "en": "ASIIN-accredited environmental geography assessing geomorphological processes, watershed hydrology, climate change dynamics, ecological hazard mitigation, and environmental impact assessments."
        },
        "fokus": {
            "id": ["Pengelolaan Daerah Aliran Sungai (DAS) Terpadu", "Geomorfologi Terapan & Mitigasi Bencana Longsor", "Analisis Dampak Lingkungan (AMDAL) & Dokumen KLHS", "Klimatologi Spasial & Adaptasi Perubahan Iklim"],
            "en": ["Integrated Watershed Resource Management", "Applied Geomorphology & Landslide Hazard Mapping", "Environmental Impact Assessment (EIA/AMDAL)", "Spatial Climatology & Climate Adaptation"]
        },
        "karir": {
            "id": ["Environmental Impact Analyst (Penyusun AMDAL)", "Water Resources & Watershed Specialist", "Disaster Risk Assessment Consultant di BNPB", "Sustainability & ESG Consultant di Korporasi"],
            "en": ["Certified Environmental Impact Analyst (EIA)", "Watershed Management & Hydrological Specialist", "Disaster Risk Consultant at National Disaster Agencies", "Corporate Sustainability & ESG Consultant"]
        }
    },
    {
        "id": "s1-kartografi-dan-penginderaan-jauh",
        "kode": "32602",
        "nama": "Kartografi dan Penginderaan Jauh",
        "nama_en": "Cartography and Remote Sensing",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Geografi", "fakultas_singkatan": "Geografi",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 27, "dt_umugm": 36,
        "website": "https://geo.ugm.ac.id/kpjonline",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Pusat rujukan nasional pengolahan citra satelit multispektral, penginderaan jauh radar satelit, pemodelan visualisasi kartografi 3D, dan analitika geospasial berbasis AI.",
            "en": "National center of excellence in satellite image processing, radar remote sensing, 3D cartographic visualization, and geospatial machine learning."
        },
        "fokus": {
            "id": ["Pengolahan Citra Satelit Optik & Radar (SAR)", "Kartografi Digital & Visualisasi Geovisual", "Machine Learning untuk Klasifikasi Tutupan Lahan", "Web GIS & Infrastruktur Data Spasial Nasional"],
            "en": ["Optical & Radar (SAR) Satellite Image Processing", "Digital Cartography & Geovisual Analytics", "Machine Learning for Automated Landcover Mapping", "Web GIS Architecture & Spatial Data Infrastructure"]
        },
        "karir": {
            "id": ["Remote Sensing Scientist di Badan Informasi Geospasial", "Geospatial Data Engineer di Industri Pemetaan Citra", "Spatial Machine Learning Specialist", "Kartografer Desain Navigasi Digital"],
            "en": ["Remote Sensing Scientist at Geospatial Agencies", "Geospatial Data Engineer in Satellite Analytics", "Spatial Machine Learning Specialist", "Digital Map Navigation Cartographer"]
        }
    },

    # =========================================================================
    # 17. FIB - Fakultas Ilmu Budaya
    # =========================================================================
    {
        "id": "s1-sastra-inggris",
        "kode": "32701",
        "nama": "Sastra Inggris",
        "nama_en": "English Literature",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Budaya", "fakultas_singkatan": "FIB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://fib.ugm.ac.id/sastra-inggris",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 9.000.000)",
        "deskripsi": {
            "id": "Kajian linguistik bahasa Inggris teoritis dan terapan, analisis kritis sastra dunia, penerjemahan profesional tersumpah, dan komunikasi antarbudaya global.",
            "en": "Theoretical and applied English linguistics, critical world literary studies, professional certified translation, and global intercultural communications."
        },
        "fokus": {
            "id": ["Linguistik Terapan & Analisis Wacana Kritis", "Sastra Dunia & Kajian Budaya Poskolonial", "Penerjemahan Teks Hukum & Lokalisasi Digital", "Komunikasi Antarbudaya Korporasi"],
            "en": ["Applied Linguistics & Critical Discourse Analysis", "World Literature & Postcolonial Cultural Studies", "Legal Translation & Digital Content Localization", "Intercultural Corporate Communications"]
        },
        "karir": {
            "id": ["Professional Translator & Conference Interpreter", "International Content Strategist di Media Global", "Corporate Communications Officer Kedutaan Asing", "Editor & Publisher Buku Sastra Internasional"],
            "en": ["Certified Translator & Simultaneous Interpreter", "Global Content Strategist in Media Houses", "Intercultural Diplomatic Officer in Embassies", "International Publishing Editor"]
        }
    },
    {
        "id": "s1-arkeologi",
        "kode": "32702",
        "nama": "Arkeologi",
        "nama_en": "Archaeology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Budaya", "fakultas_singkatan": "FIB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://fib.ugm.ac.id/arkeologi",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 9.000.000)",
        "deskripsi": {
            "id": "Eksplorasi warisan peradaban masa lampau nusantara melalui ekskavasi ilmiah, analisis artefak prasejarah dan klasik, konservasi cagar budaya (Borobudur/Prambanan), dan manajemen museum.",
            "en": "Scientific exploration of past archipelago civilizations through stratigraphic excavation, artifact conservation, World Heritage site management, and museum curation."
        },
        "fokus": {
            "id": ["Ekskavasi Arkeologi Lapangan & Stratigrafi", "Konservasi Artefak Warisan Dunia (UNESCO Sites)", "Arkeologi Bawah Air & Maritim Nusantara", "Manajemen Museum & Kurasi Benda Purbakala"],
            "en": ["Field Archaeological Excavation & Stratigraphy", "World Heritage Site Conservation (Borobudur/Prambanan)", "Underwater & Maritime Archipelago Archaeology", "Museum Management & Ancient Artifact Curation"]
        },
        "karir": {
            "id": ["Arkeolog Peneliti di Balai Pelestarian Cagar Budaya", "Kurator Museum Nasional & Koleksi Bersejarah", "Konsultan Manajemen Warisan Budaya UNESCO", "Cultural Heritage Specialist di Proyek Infrastruktur"],
            "en": ["Archaeological Researcher at Heritage Centers", "National Museum Curator & Conservator", "UNESCO Cultural Heritage Management Advisor", "Cultural Heritage Compliance Specialist"]
        }
    },

    # =========================================================================
    # 18. Fakultas Filsafat
    # =========================================================================
    {
        "id": "s1-filsafat",
        "kode": "32801",
        "nama": "Filsafat",
        "nama_en": "Philosophy",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Filsafat", "fakultas_singkatan": "Filsafat",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": [],
        "daya_tampung": 150, "dt_snbp": 45, "dt_snbt": 45, "dt_umugm": 60,
        "website": "https://filsafat.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 9.000.000)",
        "deskripsi": {
            "id": "Pusat filsafat Pancasila dan pemikiran kritis Indonesia, mendalami epistemologi sains, etika teknologi AI, filsafat hukum politik, dan logika dialektika analitis.",
            "en": "National center of Pancasila philosophy and critical thought exploring epistemology of science, ethics of artificial intelligence, political philosophy, and analytical logic."
        },
        "fokus": {
            "id": ["Filsafat Pancasila & Ideologi Kenegaraan", "Etika Teknologi & Kecerdasan Artifisial (AI Ethics)", "Epistemologi & Filsafat Ilmu Pengetahuan", "Logika Simbolik & Penalaran Kritis Analitis"],
            "en": ["Pancasila Philosophy & State Ideology", "Ethics of Technology & Artificial Intelligence", "Epistemology & Philosophy of Science", "Symbolic Logic & Critical Analytical Reasoning"]
        },
        "karir": {
            "id": ["AI Ethics & Policy Advisor di Perusahaan Teknologi", "Analis Strategis Kebijakan Negara di Lemhannas", "Penulis Opini, Jurnalis Analitis, & Pemikir Publik", "Konsultan Tata Kelola Etika Korporasi"],
            "en": ["AI Ethics & Responsible Tech Policy Advisor", "Strategic Policy Analyst at National Think Tanks", "Critical Essayist, Columnist & Public Intellectual", "Corporate Ethics & Governance Specialist"]
        }
    },

    # =========================================================================
    # 19. Sekolah Vokasi (SV UGM) - Sarjana Terapan (D4) Unggulan
    # =========================================================================
    {
        "id": "d4-teknologi-rekayasa-perangkat-lunak",
        "kode": "32901",
        "nama": "Teknologi Rekayasa Perangkat Lunak",
        "nama_en": "Software Engineering Technology",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Saintek",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://sv.ugm.ac.id/trpl",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Program Sarjana Terapan vokasi berorientasi industri terapan, mendalami rekayasa aplikasi web/mobile skala produksi, arsitektur microservices, DevOps CI/CD, dan cloud native.",
            "en": "Applied Bachelor degree focusing on production-grade web/mobile engineering, microservices architecture, DevOps CI/CD pipelines, and cloud-native software deployment."
        },
        "fokus": {
            "id": ["Rekayasa Aplikasi Web & Mobile Skala Produksi", "DevOps & Otomasi Infrastruktur CI/CD", "Arsitektur Microservices & API Gateway", "Pengujian Kualitas Perangkat Lunak (QA Automation)"],
            "en": ["Full-Stack Mobile & Web Production Engineering", "DevOps & Continuous Deployment Pipelines", "Microservices & Distributed API Architecture", "Automated QA & Software Quality Assurance"]
        },
        "karir": {
            "id": ["Full Stack Software Engineer di Korporasi Teknologi", "DevOps & Platform Automation Engineer", "Mobile Application Specialist (iOS/Android)", "Quality Assurance (QA) Automation Lead"],
            "en": ["Full Stack Software Engineer in Tech Companies", "DevOps & Cloud Automation Engineer", "Mobile Applications Developer (iOS/Android)", "QA Test Automation Lead"]
        }
    },
    {
        "id": "d4-teknologi-rekayasa-internet",
        "kode": "32902",
        "nama": "Teknologi Rekayasa Internet",
        "nama_en": "Internet Engineering Technology",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Saintek",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://sv.ugm.ac.id/tri",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Spesialisasi arsitektur jaringan komputer enterprise, keamanan sistem siber, routing internet tingkat lanjut, komputasi awan, dan implementasi jaringan IoT.",
            "en": "Applied specialisation in enterprise network architectures, cybersecurity defense, advanced BGP internet routing, cloud networking, and industrial IoT implementation."
        },
        "fokus": {
            "id": ["Desain Arsitektur Jaringan Komputer Enterprise", "Keamanan Siber & Mitigasi Serangan Jaringan", "Komputasi Awan (Cloud Systems) & Server Virtualisasi", "Teknologi Jaringan Nirkabel & Internet of Things"],
            "en": ["Enterprise Computer Network Design & Routing", "Cybersecurity Threat Detection & Defense", "Cloud Virtualization & Datacenter Systems", "Wireless Communications & Industrial IoT Networks"]
        },
        "karir": {
            "id": ["Network Engineer & Infrastructure Architect", "Cybersecurity Operations Analyst (SOC)", "Cloud Network Administrator", "IoT Systems Deployment Engineer"],
            "en": ["Enterprise Network Operations Engineer", "Security Operations Center (SOC) Analyst", "Cloud Network Systems Administrator", "IoT Field Deployment Specialist"]
        }
    },
    {
        "id": "d4-sistem-informasi-geografis",
        "kode": "32903",
        "nama": "Sistem Informasi Geografis",
        "nama_en": "Geographic Information Systems",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Saintek",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": [],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://sv.ugm.ac.id/sig",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Aplikasi praktis pemrograman spasial Web GIS, pemetaan drone fotogrametri, survei terestrial digital, dan manajemen basis data geospasial enterprise.",
            "en": "Practical application of spatial Web GIS programming, UAV mapping photogrammetry, digital terrestrial surveying, and enterprise geospatial database management."
        },
        "fokus": {
            "id": ["Pengembangan Aplikasi Web GIS Interaktif", "Survei Pemetaan Drone & Fotogrametri Terapan", "Basis Data Geospasial Enterprise (PostGIS)", "Analitika Spasial Pemodelan Tata Ruang Wilayah"],
            "en": ["Interactive Web GIS Application Development", "UAV Mapping & Applied Photogrammetry", "Enterprise Spatial Databases (PostGIS/GeoServer)", "Spatial Analytics for Regional Planning"]
        },
        "karir": {
            "id": ["Web GIS Developer di Perusahaan Teknologi", "GIS Specialist di Konsultan Tata Ruang Wilayah", "Drone Mapping Specialist di Industri Pertambangan", "Spesialis Data Spasial di Instansi Pemerintah"],
            "en": ["Web GIS Application Developer", "GIS Analyst in Urban Planning Consultancies", "UAV Drone Mapping Specialist in Mining", "Geospatial Data Specialist in Government"]
        }
    },
    {
        "id": "d4-akuntansi-sektor-publik",
        "kode": "32904",
        "nama": "Akuntansi Sektor Publik",
        "nama_en": "Public Sector Accounting",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Soshum",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": [],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 27, "dt_umugm": 36,
        "website": "https://sv.ugm.ac.id/asp",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Pendidikan akuntansi terapan untuk instansi pemerintah pusat, daerah, BUMN, dan organisasi nirlaba, berfokus pada audit kepatuhan, penganggaran APBN/APBD, dan sistem keuangan daerah.",
            "en": "Applied accounting for government agencies, state-owned enterprises (BUMN), and NGOs focusing on compliance audit, public budgeting, and digital regional finance systems."
        },
        "fokus": {
            "id": ["Standar Akuntansi Pemerintahan (SAP) & Pelaporan", "Audit Sektor Publik & Kepatuhan Keuangan Negara", "Manajemen Anggaran APBN / APBD & SIPD", "Perpajakan Bendahara & Akuntansi BUMN/BUMD"],
            "en": ["Government Accounting Standards (SAP) & Reporting", "Public Sector Compliance Audit & Verification", "State and Regional Budgeting (APBN/APBD)", "Treasury Taxation & State-Owned Enterprise Finance"]
        },
        "karir": {
            "id": ["Auditor di Badan Pemeriksa Keuangan (BPK / BPKP)", "Analis Keuangan di Kementerian & Pemerintah Daerah", "Staf Pengendalian Keuangan BUMN & Rumah Sakit Umum", "Konsultan Manajemen Keuangan Sektor Publik"],
            "en": ["Auditor at State Audit Boards (BPK / BPKP)", "Public Financial Analyst in Ministries/Local Government", "Financial Control Officer at State Enterprises", "Public Sector Financial Management Advisor"]
        }
    },
    {
        "id": "d4-teknik-pengelolaan-dan-pemeliharaan-infrastruktur-sipil",
        "kode": "32905",
        "nama": "Teknik Pengelolaan dan Pemeliharaan Infrastruktur Sipil",
        "nama_en": "Civil Infrastructure Management and Maintenance Technology",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Saintek",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://sv.ugm.ac.id/tppis",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Penerapan teknologi inspeksi, audit keandalan struktur, pemeliharaan jalan jembatan, manajemen aset konstruksi, dan Building Information Modeling (BIM).",
            "en": "Practical application of structural health monitoring, bridge and highway asset maintenance, construction project execution, and BIM coordination."
        },
        "fokus": {
            "id": ["Inspeksi & Pemeliharaan Jembatan serta Jalan Raya", "Building Information Modeling (BIM) Konstruksi", "Manajemen Proyek & Estimasi Biaya Pekerjaan Sipil", "Audit Keandalan Bangunan Gedung Bertingkat"],
            "en": ["Highway & Bridge Infrastructure Asset Maintenance", "Building Information Modeling (BIM) in Construction", "Project Management & Civil Cost Quantity Surveying", "Structural Health Auditing for Multi-Story Buildings"]
        },
        "karir": {
            "id": ["Site Engineer & Quantity Surveyor di Kontraktor BUMN", "BIM Coordinator di Konsultan Konstruksi", "Bridge & Highway Maintenance Inspector di BPJT / PUPR", "Facility Management Lead di Gedung Komersial"],
            "en": ["Civil Site Engineer & Quantity Surveyor", "BIM Coordinator in Construction Engineering", "Highway & Bridge Asset Maintenance Inspector", "Commercial Infrastructure Facility Manager"]
        }
    },

    # =========================================================================
    # 17. FIB Tambahan (Sastra & Humaniora)
    # =========================================================================
    {
        "id": "s1-sastra-indonesia",
        "kode": "32703",
        "nama": "Sastra Indonesia",
        "nama_en": "Indonesian Literature",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Budaya", "fakultas_singkatan": "FIB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://fib.ugm.ac.id/sasindo",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 9.000.000)",
        "deskripsi": {
            "id": "Pusat rujukan nasional kebahasaan dan kesusastraan Indonesia, stilistika bahasa, filologi naskah kuno nusantara, kritik sastra kontemporer, dan penyuntingan profesional.",
            "en": "National center for Indonesian linguistics and literature, stylistics, manuscript philology, contemporary literary criticism, and professional publishing editorial."
        },
        "fokus": {
            "id": ["Linguistik Bahasa Indonesia & Leksikografi", "Filologi & Digitalisasi Naskah Kuno", "Kritik Sastra & Kajian Budaya Indonesia", "Penyuntingan Naskah & Penerbitan Kreatif"],
            "en": ["Indonesian Linguistics & Lexicography", "Archipelago Manuscript Philology", "Literary Criticism & Indonesian Cultural Studies", "Professional Manuscript Editing & Publishing"]
        },
        "karir": {
            "id": ["Penyunting Buku Senior di Penerbit Nasional", "Peneliti Bahasa di Badan Bahasa Kemendikbud", "Content Strategist & Copywriter Kreatif", "Pengajar Bahasa Indonesia untuk Penutur Asing (BIPA)"],
            "en": ["Senior Book Editor at National Publishing Houses", "Linguistics Researcher at National Language Agency", "Content Strategist & Creative Copywriter", "Indonesian for Foreign Speakers (BIPA) Instructor"]
        }
    },
    {
        "id": "s1-sastra-jepang",
        "kode": "32704",
        "nama": "Sastra Jepang",
        "nama_en": "Japanese Literature",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Budaya", "fakultas_singkatan": "FIB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://fib.ugm.ac.id/sasjep",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 9.000.000)",
        "deskripsi": {
            "id": "Penguasaan kemahiran bahasa Jepang tingkat lanjut (JLPT N1/N2), sastra klasik dan modern Jepang, dinamika sosiokultural masyarakat Jepang, dan etika bisnis korporasi Jepang.",
            "en": "Advanced Japanese language proficiency (JLPT N1/N2), classical and modern Japanese literature, socio-cultural dynamics, and Japanese corporate business ethics."
        },
        "fokus": {
            "id": ["Kemahiran Bahasa Jepang Lanjutan & JLPT N1", "Sastra & Kebudayaan Kontemporer Jepang", "Etika Bisnis & Komunikasi Perusahaan Jepang", "Penerjemahan Teks Industri Jepang-Indonesia"],
            "en": ["Advanced Japanese Language Proficiency (JLPT N1)", "Contemporary Japanese Culture & Media", "Japanese Business Communications & Work Ethics", "Japanese-Indonesian Industrial Translation"]
        },
        "karir": {
            "id": ["Translator & Interpreter Korporasi Multinasional Jepang", "Bilingual Coordinator di Perusahaan Otomotif Jepang", "Liaison Officer Hubungan Bilateral Indonesia-Jepang", "Spesialis Budaya & Media Populer Jepang"],
            "en": ["Japanese Corporate Translator & Simultaneous Interpreter", "Bilingual Business Coordinator in Auto Firms", "Indonesia-Japan Bilateral Liaison Officer", "Japanese Culture & Media Analyst"]
        }
    },
    {
        "id": "s1-bahasa-dan-kebudayaan-korea",
        "kode": "32705",
        "nama": "Bahasa dan Kebudayaan Korea",
        "nama_en": "Korean Language and Culture",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Budaya", "fakultas_singkatan": "FIB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://fib.ugm.ac.id/korea",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 9.000.000)",
        "deskripsi": {
            "id": "Kemahiran bahasa Korea tingkat tinggi (TOPIK Level 5/6), sejarah dan sastra Korea, analisis industri kreatif Hallyu (K-Wave), dan diplomasi budaya Indonesia-Korea.",
            "en": "Advanced Korean language mastery (TOPIK Level 5/6), Korean literature and history, Korean wave (Hallyu) creative industries, and bilateral cultural diplomacy."
        },
        "fokus": {
            "id": ["Bahasa Korea Akademik & Standar TOPIK Tingkat 6", "Analisis Industri Kreatif Hallyu & K-Culture", "Sejarah, Politik, & Masyarakat Semenanjung Korea", "Penerjemahan Resmi Kontrak Dagang Korea-Indonesia"],
            "en": ["Academic Korean Language & TOPIK Level 6", "Hallyu Creative Industry & Media Analysis", "Korean Peninsula History, Politics & Society", "Official Korean-Indonesian Commercial Translation"]
        },
        "karir": {
            "id": ["Bilingual Specialist di Korporasi Konglomerasi Korea (Chaebol)", "Penerjemah Tersumpah Bahasa Korea", "Program Officer di Korea Foundation / Kedutaan Korea", "Media Strategist Hiburan & Konten Kreatif Korea"],
            "en": ["Korean Conglomerate (Chaebol) Bilingual Officer", "Certified Korean-Indonesian Sworn Translator", "Program Officer at Korea Foundation / Embassy", "Korean Creative Media & Entertainment Strategist"]
        }
    },
    {
        "id": "s1-sejarah",
        "kode": "32706",
        "nama": "Sejarah",
        "nama_en": "History",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Budaya", "fakultas_singkatan": "FIB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["AUN-QA"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://sejarah.fib.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 9.000.000)",
        "deskripsi": {
            "id": "Metodologi penelitian sejarah kritis, historiografi dekolonisasi Indonesia, sejarah sosial maritim, sejarah ekonomi agraria, dan preservasi arsip memori kolektif bangsa.",
            "en": "Critical historical research methodology, Indonesian decolonial historiography, maritime social history, agrarian economic history, and archival memory preservation."
        },
        "fokus": {
            "id": ["Historiografi Kritis & Dekolonisasi Narasi Sejarah", "Sejarah Maritim & Jalur Rempah Nusantara", "Sejarah Ekonomi Agraria & Transformasi Pedesaan", "Digital Humanities & Manajemen Arsip Sejarah"],
            "en": ["Critical Historiography & Decolonial Narratives", "Maritime History & Archipelago Spice Routes", "Agrarian Economic History & Rural Transformation", "Digital Humanities & Archival Data Preservation"]
        },
        "karir": {
            "id": ["Sejarawan & Peneliti di Badan Riset Nasional", "Kurator & Arsiparis Senior di Arsip Nasional RI (ANRI)", "Analis Kebijakan Sejarah & Nilai Kebangsaan", "Penulis Biografi & Peneliti Dokumenter Sejarah"],
            "en": ["Professional Historian at National Research Institutes", "Senior Archivist & Curator at National Archives (ANRI)", "National History Policy Analyst", "Historical Documentary Researcher & Biographer"]
        }
    },
    {
        "id": "s1-pariwisata",
        "kode": "32707",
        "nama": "Pariwisata",
        "nama_en": "Tourism Studies",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Budaya", "fakultas_singkatan": "FIB",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": [],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://pariwisata.fib.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 9.000.000)",
        "deskripsi": {
            "id": "Perencanaan destinasi pariwisata berkelanjutan berbasis masyarakat (CBT), konservasi warisan budaya, ekonomi sirkular pariwisata, dan manajemen perhotelan berstandar global.",
            "en": "Community-based sustainable tourism destination planning, cultural heritage preservation, tourism circular economics, and hospitality asset governance."
        },
        "fokus": {
            "id": ["Perencanaan Destinasi Wisata Berkelanjutan", "Pariwisata Berbasis Masyarakat (CBT) & Ekowisata", "Manajemen Warisan Budaya & Event Internasional", "Pemasaran Digital Destinasi & Pariwisata Cerdas"],
            "en": ["Sustainable Destination Masterplanning", "Community-Based Tourism (CBT) & Ecotourism", "Cultural Heritage Tourism & Global Event Management", "Smart Tourism & Destination Digital Marketing"]
        },
        "karir": {
            "id": ["Tourism Destination Planner di Kemenparekraf / Dinas", "Ecotourism Consultant di Lembaga Pembangunan Global", "Event & MICE Operations Director", "General Manager Hotel & Kawasan Wisata Terpadu"],
            "en": ["Tourism Destination Planner at Tourism Ministries", "Ecotourism Consultant at Global Development Agencies", "MICE & International Event Operations Director", "Resort & Destination General Manager"]
        }
    },

    # =========================================================================
    # 8. FISIPOL Tambahan
    # =========================================================================
    {
        "id": "s1-pembangunan-sosial-dan-kesejahteraan",
        "kode": "31805",
        "nama": "Pembangunan Sosial dan Kesejahteraan",
        "nama_en": "Social Development and Welfare (PSdK)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Sosial dan Ilmu Politik", "fakultas_singkatan": "FISIPOL",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": [],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://psdk.fisipol.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Strategi perlindungan sosial inklusif, Corporate Social Responsibility (CSR), pemberdayaan masyarakat adat dan marginal, serta program pengentasan kemiskinan berbasis bukti.",
            "en": "Inclusive social protection systems, corporate social responsibility (CSR), indigenous and marginalized empowerment, and evidence-based poverty eradication."
        },
        "fokus": {
            "id": ["Corporate Social Responsibility (CSR) & ESG Strategis", "Pemberdayaan Masyarakat & Transformasi Komunitas", "Kebijakan Perlindungan Sosial & Jaminan Kesejahteraan", "Kewirausahaan Sosial (Social Enterprise)"],
            "en": ["Corporate Social Responsibility (CSR) & ESG Strategy", "Community Empowerment & Participatory Rural Appraisal", "Social Welfare Policy & Safety Net Design", "Social Entrepreneurship & Inclusive Business"]
        },
        "karir": {
            "id": ["Head of CSR & Community Development di Korporasi", "Social Impact Specialist di Lembaga PBB (UNDP/UNICEF)", "Program Lead di Yayasan Filantropi & NGO Internasional", "Analis Kesejahteraan Sosial di Kementerian Sosial"],
            "en": ["Corporate CSR & Community Development Director", "Social Impact Specialist at UN Agencies", "Philanthropic Foundation Program Lead", "Social Welfare Policy Analyst"]
        }
    },
    {
        "id": "s1-sosiologi",
        "kode": "31806",
        "nama": "Sosiologi",
        "nama_en": "Sociology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Sosial dan Ilmu Politik", "fakultas_singkatan": "FISIPOL",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": [],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://sosiologi.fisipol.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Analisis struktur dan perubahan sosial masyarakat modern, sosiologi digital, resolusi konflik komunal, sosiologi lingkungan perkotaan, dan dinamika gerakan sosial.",
            "en": "Analysis of modern social structures, digital sociology, conflict resolution, urban environmental sociology, and dynamics of contemporary social movements."
        },
        "fokus": {
            "id": ["Sosiologi Digital & Interaksi Komunitas Maya", "Resolusi Konflik Sosial & Mediasi Perdamaian", "Sosiologi Lingkungan & Gerakan Ekologis", "Riset Kualitatif & Etnografi Terapan"],
            "en": ["Digital Sociology & Online Community Dynamics", "Social Conflict Resolution & Peace Mediation", "Environmental Sociology & Ecological Movements", "Advanced Qualitative Research & Applied Ethnography"]
        },
        "karir": {
            "id": ["Social Research Lead di Lembaga Konsultasi Global", "Conflict Resolution Specialist & Mediator Sosial", "Policy Analyst di Lembaga Advokasi Publik", "Peneliti Kebijakan Sosial Budaya"],
            "en": ["Social Research Lead in International Consultancies", "Conflict Resolution & Social Mediation Specialist", "Public Advocacy Policy Analyst", "Social-Cultural Research Scientist"]
        }
    },

    # =========================================================================
    # 11. Fakultas Pertanian Tambahan
    # =========================================================================
    {
        "id": "s1-ilmu-tanah",
        "kode": "32104",
        "nama": "Ilmu Tanah",
        "nama_en": "Soil Science",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Pertanian", "fakultas_singkatan": "Pertanian",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://soil.faperta.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Evaluasi kesuburan tanah, remidiasi lahan terdegradasi, biologi tanah, pemetaan survei tanah digital, dan konservasi tanah dan air untuk ketahanan pangan.",
            "en": "Soil fertility assessment, degraded land bioremediation, digital soil mapping, and soil and water conservation for national food resilience."
        },
        "fokus": {
            "id": ["Kesuburan Tanah & Nutrisi Pemupukan Berimbang", "Survei Tanah Digital & Evaluasi Kesesuaian Lahan", "Biologi Tanah & Mikrobioma Perakaran Tanaman", "Remediasi Lahan Kritis & Konservasi DAS"],
            "en": ["Soil Fertility & Balanced Nutrient Management", "Digital Soil Mapping & Land Evaluation", "Soil Microbiology & Rhizosphere Ecology", "Land Remediation & Watershed Soil Conservation"]
        },
        "karir": {
            "id": ["Soil Scientist di Korporasi Perkebunan Besar", "Agronomy Land Suitability Specialist", "Konsultan Reklamasi Lahan Tambang & AMDAL", "Peneliti Tanah & Lahan Pertanian Balitbangtan"],
            "en": ["Soil Scientist in Commercial Plantations", "Land Suitability & Precision Soil Specialist", "Mine Land Reclamation & Remediation Advisor", "Agricultural Soil Research Scientist"]
        }
    },
    {
        "id": "s1-mikrobiologi-pertanian",
        "kode": "32105",
        "nama": "Mikrobiologi Pertanian",
        "nama_en": "Agricultural Microbiology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Pertanian", "fakultas_singkatan": "Pertanian",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://mikro.faperta.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Pemanfaatan mikroorganisme menguntungkan untuk biofertilizer, biopestisida alami, bioremediasi limbah agroindustri, dan bioteknologi fermentasi tanaman pangan.",
            "en": "Harnessing beneficial microorganisms for biofertilizers, biological pest control, agro-industrial bioremediation, and agricultural fermentation biotechnology."
        },
        "fokus": {
            "id": ["Biofertilizer & Mikroba Penambat Nitrogen", "Biopestisida Alami & Agen Antagonis Patogen", "Bioremediasi Polutan Lahan Pertanian", "Genomik Mikroba Tanah Tropis"],
            "en": ["Biofertilizers & Nitrogen-Fixing Microbes", "Biological Pest Control & Bio-fungicides", "Agricultural Soil Bioremediation Systems", "Tropical Soil Microbial Metagenomics"]
        },
        "karir": {
            "id": ["Agricultural Microbiologist di Industri Pupuk Hayati", "Fermentation Lead di Perusahaan Bioteknologi", "Quality Control Specialist Produk Biologi Pertanian", "Peneliti Mikrobioma Tanah di BRIN"],
            "en": ["Agricultural Microbiologist in Bio-fertilizer Firms", "Fermentation Engineer in Biotech Companies", "Biocontrol Products QA/QC Specialist", "Soil Metagenomics Research Scientist"]
        }
    },
    {
        "id": "s1-proteksi-tanaman",
        "kode": "32106",
        "nama": "Proteksi Tanaman",
        "nama_en": "Plant Protection",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Pertanian", "fakultas_singkatan": "Pertanian",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://proteksi.faperta.ugm.ac.id",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Diagnosis dan pengendalian hama penyakit tanaman secara terpadu (PHT), entomologi pertanian, virologi dan mikologi tumbuhan, serta biosafety karantina hayati.",
            "en": "Integrated pest management (IPM), agricultural entomology, plant pathology, epidemiology, and phytosanitary biosafety quarantine."
        },
        "fokus": {
            "id": ["Pengendalian Hama Terpadu (PHT) Berkelanjutan", "Entomologi Pertanian & Ekologi Serangga", "Patologi Tumbuhan & Diagnosis Molekuler Penyakit", "Karantina Tumbuhan & Biosafety Perbatasan"],
            "en": ["Integrated Pest Management (IPM)", "Agricultural Entomology & Insect Ecology", "Molecular Plant Pathology & Epidemiology", "Phytosanitary Inspection & Plant Quarantine"]
        },
        "karir": {
            "id": ["Plant Protection Specialist di Perkebunan Komersial", "Analis Karantina Tumbuhan di Badan Karantina Indonesia", "Formulator Biopestisida di Industri Agrokimia", "Peneliti Hama & Penyakit Tanaman Kementan"],
            "en": ["Crop Protection Manager in Commercial Agriculture", "Plant Quarantine Officer at Border Inspection", "Agrochemical Product Development Specialist", "Agricultural Pathology Researcher"]
        }
    },

    # =========================================================================
    # 14. FTP Tambahan
    # =========================================================================
    {
        "id": "s1-teknologi-industri-pertanian",
        "kode": "32403",
        "nama": "Teknologi Industri Pertanian",
        "nama_en": "Agro-industrial Technology (TIP)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Agro",
        "fakultas": "Fakultas Teknologi Pertanian", "fakultas_singkatan": "FTP",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 110, "dt_snbp": 33, "dt_snbt": 33, "dt_umugm": 44,
        "website": "https://tip.tp.ugm.ac.id/tip",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Desain sistem agroindustri hilir, optimasi rantai pasok komoditas pertanian, rekayasa proses bioproduk ramah lingkungan, dan manajemen mutu ISO industri perkebunan.",
            "en": "Downstream agro-industrial systems engineering, agricultural supply chain optimization, bioproduct process engineering, and ISO quality systems."
        },
        "fokus": {
            "id": ["Desain Sistem Manufaktur Agroindustri Hilir", "Optimasi Rantai Pasok Pangan & Kelapa Sawit", "Rekayasa Bioproduk & Bioekonomi Sirkular", "Manajemen Mutu ISO & Audit Industri Pertanian"],
            "en": ["Downstream Agro-Processing Facility Design", "Agri-Supply Chain Logistics & Palm Oil Analytics", "Bioproduct Engineering & Circular Bioeconomy", "Quality Management Systems (ISO 9001/22000)"]
        },
        "karir": {
            "id": ["Plant Operations Lead di Industri Agrokimia/Pangan", "Supply Chain Lead di Korporasi Kelapa Sawit & Kopi", "Quality Assurance & ESG Auditor Industri Pertanian", "Konsultan Kelayakan Investasi Agroindustri"],
            "en": ["Agro-industrial Plant Operations Manager", "Supply Chain Lead in Coffee & Palm Oil Firms", "ESG & Quality Assurance Auditor in Agriculture", "Agro-industrial Investment Feasibility Consultant"]
        }
    },

    # =========================================================================
    # 16. Geografi Tambahan
    # =========================================================================
    {
        "id": "s1-pembangunan-wilayah",
        "kode": "32603",
        "nama": "Pembangunan Wilayah",
        "nama_en": "Regional Development",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "fakultas": "Fakultas Geografi", "fakultas_singkatan": "Geografi",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 27, "dt_umugm": 36,
        "website": "https://geo.ugm.ac.id/pw",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Analisis spasial dinamika kependudukan, kesenjangan ekonomi antar-wilayah, perencanaan kawasan tertinggal dan perbatasan, serta manajemen sumber daya pedesaan-perkotaan.",
            "en": "Spatial analysis of demographic dynamics, inter-regional economic disparities, borderlands development, and rural-urban linkage planning."
        },
        "fokus": {
            "id": ["Ekonomi Regional & Analisis Kesenjangan Wilayah", "Perencanaan Wilayah Perbatasan & Daerah Tertinggal", "Dinamika Demografi Spasial & Migrasi Penduduk", "Kebijakan Pembangunan Berkelanjutan (SDGs)"],
            "en": ["Regional Economic Disparities & Growth Nodes", "Borderlands & Underdeveloped Area Planning", "Spatial Demography & Population Migration Analytics", "Sustainable Development Goals (SDGs) Localization"]
        },
        "karir": {
            "id": ["Perencana Pembangunan di Bappenas / Bappeda", "Regional Economic Analyst di Lembaga Multilateral", "Konsultan Masterplan Pembangunan Wilayah", "Tenaga Ahli Pemberdayaan Daerah 3T"],
            "en": ["Regional Development Planner at National Agencies", "Economic Geographer in Multilateral Development", "Regional Development Masterplan Advisor", "Regional Equity Policy Consultant"]
        }
    },

    # =========================================================================
    # 19. Sekolah Vokasi (SV) Tambahan
    # =========================================================================
    {
        "id": "d4-teknologi-rekayasa-elektro",
        "kode": "32906",
        "nama": "Teknologi Rekayasa Elektro",
        "nama_en": "Electrical Engineering Technology",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Saintek",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://sv.ugm.ac.id/tre",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Penerapan sistem kelistrikan gedung bertingkat, transmisi daya, instalasi pembangkit energi terbarukan surya (PLTS), dan pemeliharaan mesin-mesin listrik industri.",
            "en": "Applied electrical systems for high-rise buildings, power transmission, solar photovoltaic integration, and industrial motor maintenance."
        },
        "fokus": {
            "id": ["Instalasi Listrik Industri & Proteksi Tenaga", "Sistem Pembangkit Listrik Tenaga Surya (PLTS)", "Programmable Logic Controller (PLC) & SCADA", "Audit Konsumsi Energi Listrik Gedung"],
            "en": ["Industrial Electrical Installations & Protection", "Solar PV Systems & Grid-Tie Inverters", "PLC & SCADA Industrial Automation", "Electrical Building Energy Auditing"]
        },
        "karir": {
            "id": ["Electrical Site Engineer di Proyek Gedung & Pabrik", "Solar PV Installation & Commissioning Specialist", "PLC Programmer & Automation Maintenance Lead", "Auditor Energi Listrik Industri Terakreditasi"],
            "en": ["Electrical Site Construction Engineer", "Solar Photovoltaic Commissioning Specialist", "PLC Programming & SCADA Maintenance Lead", "Certified Electrical Energy Auditor"]
        }
    },
    {
        "id": "d4-teknologi-rekayasa-mesin",
        "kode": "32907",
        "nama": "Teknologi Rekayasa Mesin",
        "nama_en": "Mechanical Engineering Technology",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Saintek",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://sv.ugm.ac.id/trm",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 12.000.000)",
        "deskripsi": {
            "id": "Teknologi permesinan Computer Numerical Control (CNC), pengelasan presisi (welding inspector), pemeliharaan peralatan pabrik (plant maintenance), dan CAD/CAM manufaktur.",
            "en": "CNC machining technology, precision welding inspection, industrial plant maintenance, and CAD/CAM mechanical manufacturing."
        },
        "fokus": {
            "id": ["Permesinan Presisi CNC 5-Axis & CAM", "Inspeksi Pengelasan (Welding Inspector Bersertifikat)", "Preventive Maintenance Peralatan Mekanikal Pabrik", "Desain Manufaktur Komponen Otomotif 3D"],
            "en": ["Multi-Axis Precision CNC Machining & CAM", "Certified Welding Inspection & NDT Testing", "Preventive Mechanical Plant Maintenance", "3D CAD Automotive Component Manufacturing"]
        },
        "karir": {
            "id": ["Production Engineer di Industri Manufaktur Presisi", "Certified Welding Inspector di Sektor Migas & Galangan", "Mechanical Maintenance Supervisor di Pabrik", "CNC Programmer & Tooling Engineer"],
            "en": ["Precision Manufacturing Production Engineer", "Certified Welding Inspector (CSWIP/AWS)", "Industrial Mechanical Maintenance Supervisor", "CNC Programmer & Tooling Specialist"]
        }
    },
    {
        "id": "d4-manajemen-informasi-kesehatan",
        "kode": "32908",
        "nama": "Manajemen Informasi Kesehatan",
        "nama_en": "Health Information Management",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Medika",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 18, "dt_umugm": 24,
        "website": "https://sv.ugm.ac.id/mik",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 11.000.000)",
        "deskripsi": {
            "id": "Pengelolaan rekam medis elektronik (RME), kodifikasi klinis penyakit (ICD-10 dan ICD-9-CM), klaim asuransi BPJS Kesehatan (INA-CBGs), dan analitika data rumah sakit.",
            "en": "Electronic medical records (EMR) administration, clinical disease coding (ICD-10/ICD-9-CM), healthcare reimbursement (INA-CBGs), and hospital healthcare analytics."
        },
        "fokus": {
            "id": ["Rekam Medis Elektronik (RME) & Standar FHIR", "Klasifikasi & Kodifikasi Klinis ICD-10/ICD-9-CM", "Manajemen Klaim Jaminan Kesehatan (BPJS INA-CBGs)", "Tata Kelola Keamanan Data Medis Pasien"],
            "en": ["Electronic Medical Records (EMR) & Interoperability", "Clinical Coding (ICD-10 & ICD-9-CM Standards)", "Healthcare Reimbursement & Casemix Systems", "Healthcare Data Privacy & Security Governance"]
        },
        "karir": {
            "id": ["Kepala Instalasi Rekam Medis Rumah Sakit", "Certified Clinical Coder di Asuransi & Rumah Sakit", "Health Data Analyst di Dinas Kesehatan", "Hospital Information System Implementation Specialist"],
            "en": ["Director of Hospital Medical Records", "Certified Clinical Coding Specialist", "Public Health Data Analyst", "Hospital Information System (HIS) Consultant"]
        }
    },
    {
        "id": "d4-perbankan",
        "kode": "32909",
        "nama": "Perbankan",
        "nama_en": "Banking and Financial Services",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Soshum",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "374",
        "akreditasi_internasional": [],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 24, "dt_umugm": 32,
        "website": "https://sv.ugm.ac.id/perbankan",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Operasional perbankan komersial dan syariah, analisis kelayakan kredit UMKM dan korporasi, kepatuhan perbankan (AML/CFT), dan inovasi layanan digital banking.",
            "en": "Commercial and Islamic banking operations, credit underwriting analysis for SMEs and corporates, anti-money laundering compliance, and digital banking innovation."
        },
        "fokus": {
            "id": ["Analisis Kredit Komersial & Penilaian Risiko", "Operasional Perbankan Digital & FinTech", "Perbankan Syariah & Kepatuhan Produk Fikih", "Audit Kepatuhan Perbankan & Regulasi OJK/BI"],
            "en": ["Commercial Credit Underwriting & Risk Analysis", "Digital Banking Operations & Payment FinTech", "Islamic Banking & Sharia Compliance", "Banking Compliance & Financial Regulations"]
        },
        "karir": {
            "id": ["Relationship Manager (RM) Lending & Funding Bank BUMN", "Credit Analyst di Bank Komersial & Lembaga Finansial", "Branch Operations Supervisor Perbankan", "Fintech Payment Operations Specialist"],
            "en": ["Commercial Banking Relationship Manager", "Credit Risk Analyst in Commercial Banks", "Bank Branch Operations Supervisor", "FinTech Payment Operations Specialist"]
        }
    },
    {
        "id": "d4-pengelolaan-hutan",
        "kode": "32910",
        "nama": "Pengelolaan Hutan",
        "nama_en": "Forest Management",
        "jenjang": "D4", "kategori": "Sarjana Terapan", "rumpun": "Agro",
        "fakultas": "Sekolah Vokasi", "fakultas_singkatan": "SV",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "374",
        "akreditasi_internasional": [],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 21, "dt_umugm": 28,
        "website": "https://sv.ugm.ac.id/pengelolaan-hutan",
        "ukt_rentang": "UKT Pendidikan Unggul Bersubsidi 100% (Rp 0) s/d UKT Unggul (Rp 10.000.000)",
        "deskripsi": {
            "id": "Praktek lapang inventarisasi tegakan hutan, pemanenan kayu ramah lingkungan (RIL), patroli perlindungan kawasan hutan dari kebakaran, dan perhutanan sosial kemasyarakatan.",
            "en": "Field inventory of timber stands, reduced-impact logging (RIL), forest fire prevention patrols, and community social forestry implementation."
        },
        "fokus": {
            "id": ["Inventarisasi Hutan & Pengukuran Kayu Terapan", "Pemanenan Hutan Berdampak Rendah (RIL)", "Mitigasi & Pengendalian Kebakaran Hutan Lahan", "Perhutanan Sosial & Pemberdayaan Masyarakat Desa Hutan"],
            "en": ["Applied Timber Inventory & Forest Mensuration", "Reduced-Impact Logging (RIL) Forestry", "Wildfire Prevention & Patrol Tactics", "Social Forestry & Forest Community Development"]
        },
        "karir": {
            "id": ["Supervisor Lapangan di Perusahaan HTI / Konsesi Hutan", "Forest Fire Protection Specialist di Kemen LHK", "Surveyor Inventarisasi Sumber Daya Hutan", "Fasilitator Perhutanan Sosial di Lembaga Lingkungan"],
            "en": ["Forestry Concession Field Operations Supervisor", "Forest Fire Management Specialist", "Timber Stand Inventory Surveyor", "Community Social Forestry Facilitator"]
        }
    },
    # =========================================================================
    # 20. Pascasarjana Unggulan (S2 Magister Terakreditasi Global)
    # =========================================================================
    {
        "id": "s2-magister-manajemen",
        "kode": "33001",
        "nama": "Magister Manajemen",
        "nama_en": "Master of Business Administration (MM UGM)",
        "jenjang": "S2", "kategori": "Magister", "rumpun": "Bisnis & Manajemen",
        "fakultas": "Fakultas Ekonomika dan Bisnis", "fakultas_singkatan": "FEB",
        "lokasi": "Kampus UGM Yogyakarta & Jakarta",
        "akreditasi": "Unggul", "akreditasi_skor": "390",
        "akreditasi_internasional": ["AACSB"],
        "daya_tampung": 200, "dt_snbp": 0, "dt_snbt": 0, "dt_umugm": 200,
        "website": "https://mm.feb.ugm.ac.id",
        "ukt_rentang": "Rp 26.000.000 - Rp 38.000.000 per semester",
        "deskripsi": {
            "id": "Program MBA tertua dan berperingkat dunia di Indonesia dengan akreditasi AACSB, mencetak CEO, direktur korporasi, dan pengusaha berdaya saing global melalui kurikulum kepemimpinan strategis dan inovasi digital.",
            "en": "Indonesia's premier world-ranked AACSB-accredited MBA program cultivating CEOs, corporate directors, and innovative entrepreneurs in strategic digital leadership."
        },
        "fokus": {
            "id": ["Executive Leadership & Transformasi Digital", "Corporate Finance & Mergers Acquisitions", "Strategic Marketing & Global Brand Building", "Sustainability Leadership & ESG Reporting"],
            "en": ["Executive Leadership & Digital Enterprise Transformation", "Corporate Finance & Mergers and Acquisitions", "Strategic Marketing & Global Brand Architecture", "Corporate Sustainability & ESG Governance"]
        },
        "karir": {
            "id": ["Chief Executive Officer (CEO) / C-Suite Corporate Leader", "Managing Director di Private Equity & Venture Capital", "Senior Strategy Consultant di Firma Internasional", "VP of Business Strategy & Corporate Development"],
            "en": ["Chief Executive Officer (CEO) / C-Suite Executive", "Private Equity & Venture Capital Managing Director", "Senior Strategic Management Consulting Partner", "Vice President of Corporate Strategy"]
        }
    },
    {
        "id": "s2-magister-administrasi-publik",
        "kode": "33002",
        "nama": "Magister Administrasi Publik",
        "nama_en": "Master of Public Administration (MAP UGM)",
        "jenjang": "S2", "kategori": "Magister", "rumpun": "Soshum",
        "fakultas": "Fakultas Ilmu Sosial dan Ilmu Politik", "fakultas_singkatan": "FISIPOL",
        "lokasi": "Kampus UGM Bulaksumur (Yogyakarta)",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": [],
        "daya_tampung": 120, "dt_snbp": 0, "dt_snbt": 0, "dt_umugm": 120,
        "website": "https://map.fisipol.ugm.ac.id",
        "ukt_rentang": "Rp 15.000.000 per semester",
        "deskripsi": {
            "id": "Pendidikan pascasarjana kepemimpinan sektor publik terkemuka, melatih birokrat reformis, analis kebijakan strategis, dan pemimpin lembaga publik dalam tata kelola pemerintahan adaptif.",
            "en": "Leading public leadership master program training transformative civil servants, strategic policy analysts, and public institution heads in adaptive governance."
        },
        "fokus": {
            "id": ["Kepemimpinan Sektor Publik & Reformasi Birokrasi", "Analisis & Evaluasi Kebijakan Publik Strategis", "Transformasi Digital Pemerintahan (GovTech)", "Manajemen Anggaran & Keuangan Publik Terpadu"],
            "en": ["Public Sector Leadership & Bureaucratic Reform", "Strategic Public Policy Formulation & Evaluation", "Government Digital Transformation (GovTech)", "Integrated Public Finance Management"]
        },
        "karir": {
            "id": ["Pimpinan Tinggi Pratama / Madya di Kementerian", "Kepala Badan Perencanaan Pembangunan Daerah (Bappeda)", "Senior Policy Advisor di Lembaga PBB / Internasional", "Direktur Eksekutif Lembaga Kebijakan Publik"],
            "en": ["Senior Executive Service Officer in Ministries", "Regional Development Planning Board Director", "Senior Policy Advisor in International Agencies", "Executive Director of Public Policy Think Tanks"]
        }
    }
]

def generate_datasets():
    print(f"Generating UGM study program dataset... Total programs: {len(RAW_PRODI)}")

    # 1. Write JSON
    json_path = os.path.join(DATA_DIR, "ugm_prodi.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(RAW_PRODI, f, indent=2, ensure_ascii=False)
    print(f"Written: {json_path}")

    # 2. Extract faculties metadata
    faculties_map = {}
    for p in RAW_PRODI:
        f_code = p["fakultas_singkatan"]
        if f_code not in faculties_map:
            faculties_map[f_code] = {
                "singkatan": f_code,
                "nama": p["fakultas"],
                "lokasi": p["lokasi"]
            }

    # 3. Write JS (for static web consumption)
    js_path = os.path.join(DATA_DIR, "ugm_prodi.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("// Dataset Resmi Direktori Program Studi Universitas Gadjah Mada (UGM)\n")
        f.write(f"// Diperbarui: {datetime.date.today().strftime('%d %B %Y')}\n\n")
        f.write("window.UGM_METADATA = " + json.dumps(UGM_METADATA, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("window.UGM_FACULTIES = " + json.dumps(faculties_map, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("window.UGM_PRODI_DATA = " + json.dumps(RAW_PRODI, indent=2, ensure_ascii=False) + ";\n")
    print(f"Written: {js_path}")

    # 4. Write CSV
    csv_path = os.path.join(DATA_DIR, "ugm_prodi.csv")
    csv_fields = [
        "id", "kode", "nama", "nama_en", "jenjang", "kategori", "rumpun",
        "fakultas", "fakultas_singkatan", "lokasi", "akreditasi",
        "akreditasi_skor", "akreditasi_internasional", "daya_tampung", "dt_snbp",
        "dt_snbt", "dt_umugm", "website", "ukt_rentang"
    ]
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for p in RAW_PRODI:
            row = {
                "id": p["id"],
                "kode": p["kode"],
                "nama": p["nama"],
                "nama_en": p["nama_en"],
                "jenjang": p["jenjang"],
                "kategori": p["kategori"],
                "rumpun": p["rumpun"],
                "fakultas": p["fakultas"],
                "fakultas_singkatan": p["fakultas_singkatan"],
                "lokasi": p["lokasi"],
                "akreditasi": p["akreditasi"],
                "akreditasi_skor": p["akreditasi_skor"],
                "akreditasi_internasional": "; ".join(p["akreditasi_internasional"]),
                "daya_tampung": p["daya_tampung"],
                "dt_snbp": p["dt_snbp"],
                "dt_snbt": p["dt_snbt"],
                "dt_umugm": p["dt_umugm"],
                "website": p["website"],
                "ukt_rentang": p["ukt_rentang"]
            }
            writer.writerow(row)
    print(f"Written: {csv_path}")

    # 5. Write metadata.json
    now = datetime.datetime.now()
    metadata_path = os.path.join(DATA_DIR, "metadata.json")
    meta_content = {
        "title": "Universitas Gadjah Mada Study Programs & Accreditation Directory",
        "university": "Universitas Gadjah Mada",
        "acronym": "UGM",
        "last_updated_iso": now.isoformat(),
        "last_updated_date": now.strftime("%d %B %Y"),
        "total_prodi": len(RAW_PRODI),
        "total_fakultas": len(faculties_map),
        "total_s1": sum(1 for p in RAW_PRODI if p["jenjang"] == "S1"),
        "total_vokasi_d4": sum(1 for p in RAW_PRODI if p["jenjang"] == "D4"),
        "total_pascasarjana": sum(1 for p in RAW_PRODI if p["jenjang"] in ("S2", "S3")),
        "total_unggul": sum(1 for p in RAW_PRODI if p["akreditasi"] == "Unggul"),
        "total_akreditasi_internasional": sum(1 for p in RAW_PRODI if len(p["akreditasi_internasional"]) > 0),
        "total_daya_tampung": sum(p["daya_tampung"] for p in RAW_PRODI),
        "source": "https://um.ugm.ac.id",
        "license": "MIT"
    }
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(meta_content, f, indent=2, ensure_ascii=False)
    print(f"Written: {metadata_path}")
    print("Dataset generation completed successfully.")

if __name__ == "__main__":
    generate_datasets()
