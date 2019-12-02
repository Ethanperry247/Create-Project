import peasy.*;

PeasyCam cam;

BufferedReader reader;
String line;

void setup() {
 // size(800, 600, P3D);
 fullScreen(P3D);
 background(30);
 
 cam = new PeasyCam(this, width/2, height/2, 0, 200);
 
 reader = createReader("log.txt");
 line = null;
  
}


boolean checkStatus = false;
int nodeID = -1;

void draw() {
  background(30);
  try {
      while ((line = reader.readLine()) != null) {
        println (line);
        if (line.substring(line.length()-5).equals("False")) {
          checkStatus = false;
        } else if (line.substring(line.length()-5).equals("Error")) {
          checkStatus = false;
        } else { 
          nodeID = int(line.substring(line.length()-21,line.length()-20));
          checkStatus = true; 
        }
      }
  }
  catch (IOException e) {
    e.printStackTrace();
  }
  
  translate(width/2, height/2);
  noFill();
  stroke(255);
  strokeWeight(2);
  
  float roomX = 100;
  float roomY = 50;
  float roomZ = 80;
  float nodeSize = 5;
  
  if (checkStatus) {
    
      color col;
    
      if (second()%2==0) col = color(255,0,0);
      else col = color(255);
    
      if (nodeID == 0) {
      
        box(roomX, roomY, roomZ);
        translate(-roomX/2+nodeSize/2, -roomY/2+nodeSize/2, -roomZ/2+nodeSize/2);
        fill(col);
        noStroke();
        box(nodeSize);
        
        translate(roomX-nodeSize, 0, 0);
        fill(255);
        noStroke();
        box(nodeSize);
      
        translate(0, 0, roomZ-nodeSize);
        fill(255);
        noStroke();
        box(nodeSize);
      
      } else if (nodeID == 1) {
        
        box(roomX, roomY, roomZ);
        translate(-roomX/2+nodeSize/2, -roomY/2+nodeSize/2, -roomZ/2+nodeSize/2);
        fill(255);
        noStroke();
        box(nodeSize);
        
        translate(roomX-nodeSize, 0, 0);
        fill(col);
        noStroke();
        box(nodeSize);
      
        translate(0, 0, roomZ-nodeSize);
        fill(255);
        noStroke();
        box(nodeSize);
        
      } else {
        
        box(roomX, roomY, roomZ);
        translate(-roomX/2+nodeSize/2, -roomY/2+nodeSize/2, -roomZ/2+nodeSize/2);
        fill(255);
        noStroke();
        box(nodeSize);
        
        translate(roomX-nodeSize, 0, 0);
        fill(255);
        noStroke();
        box(nodeSize);
      
        translate(0, 0, roomZ-nodeSize);
        fill(col);
        noStroke();
        box(nodeSize);
        
      }
      
      
  
  } else {
      color col = color(255);
    
      box(roomX, roomY, roomZ);
      translate(-roomX/2+nodeSize/2, -roomY/2+nodeSize/2, -roomZ/2+nodeSize/2);
      fill(col);
      noStroke();
      box(nodeSize);
      
      translate(roomX-nodeSize, 0, 0);
      fill(col);
      noStroke();
      box(nodeSize);
      
      translate(0, 0, roomZ-nodeSize);
      fill(col);
      noStroke();
      box(nodeSize);
  }
  
  
  
}
