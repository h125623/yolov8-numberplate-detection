yolov8 numberplate detection

환경 설정
1. anaconda 설치
2. 가상환경 설정 python3.9(3.10, 3.7 사용시 에러)
3. jupyter 설치
4. pip install opencv-python
5. pip install ultralytics
6. nvidia 그래픽드라이버 최신버전 설치
7. cuda 12.1 버전 설치
8. cudnn 8.9.7 버전 cuda 12.1용 설치
9. pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 (pytorch getstart 참고, windows cuda 12.1용)
10. https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e (데이터 다운로드, 압축 해제 후 [train, valid, test]폴더를 yolov8-numberplate-detection 폴더로 이동)
11. data.yaml 파일에서 경로 수정
12. Untitled-1.ipynb 파일 통해서 학습 및 탐지 수행
