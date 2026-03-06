---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:51.467146+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: automacao_catalogo_servicos
    weight: 8
    confidence: 0.9
  - name: armazenamento_objetos
    weight: 7
    confidence: 0.85
  - name: fila_mensageria
    weight: 7
    confidence: 0.85
  - name: database_as_a_service
    weight: 7
    confidence: 0.85
  - name: backup_as_a_service
    weight: 6
    confidence: 0.75
  - name: compliance_services
    weight: 6
    confidence: 0.75
  - name: broker_as_a_service
    weight: 6
    confidence: 0.75
  - name: infraestrutura_nuvem_serpro
    weight: 9
    confidence: 0.95
  - name: roadmap_projetos_ti
    weight: 8
    confidence: 0.9
  - name: cursos_online_tecnologia
    weight: 5
    confidence: 0.6
  cdu_primary: '004.7'
  cdu_secondary:
  - '004.4'
  - '004.6'
  - '004.77'
  - '004.78'
  - '004.73'
  cdu_description: Redes de computadores. Sistemas de computadores. Gestão de sistemas. Serviços de rede. Serviços de computação em nuvem.
---
# Cursos
- https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/block-v1:LinuxFoundationX+LFS158x+1T2022+type@sequential+block@f0d11db04aff45479f54a3075d2286c1/block-v1:LinuxFoundationX+LFS158x+1T2022+type@vertical+block@42047bd89f89466cbd2d4b8f5144c564
- https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS151.x+3T2021/home
- https://digitallearning.vmware.com/learn/courses/101/vmware-vsphere-and-vmware-vsan-fundamentals/lessons/2113:621/vsphere-and-vsan-technical-overview

# Tentando entender o projeto
- Aqui há uma apresentação que lista as entregas: [[EntregasCloudOneApresentacao.png]] Fonte: https://serprogovbr.sharepoint.com/:p:/s/CDINO/ETtsVIvNhydBuVJFCdihy2QBMqLOYPU30SRmgJ7BF6Esng
- Mas aqui há um roadmap que lista entregas com itemização diferente: https://git.[[serpro]]/CDINO/Iniciativas/roadmap-cloud-one
	- E1 Armazenamento de objetos (baseado no Cloudian)
	- E2 Automação e catálogo de serviços(baseado no vRealize Automation) 
	- E3 Fila de mensageria (baseada no VMware RabbitMQ + vCD Plugin)
	- E4 Database as a Service (baseado no DMS vCloud Director Plugins) - na apresentação do 1o item acima está informando "baseado no VMWare TDSE + vCD plugin"
	- E5 Backup as a Service (tecnologia em definição)
	- E6 Infovia BSA
	- E7 Saida Internet AZ2 SPO
	- E8 Compliance Services (baseado no vRealize Network Log Insight) 
	- E9 GPU no laaS
	- E10 Broker as a Service (baseado no vRealize Cloud Health) 
	- E11 DirectConnect
	- E12 Licenciamento facilitado Windows
- [Modelo Operacional do Serpro Cloud One](https://automatus.gitpages.serpro/serprocloud-docs/)
- 