let tree;

function setup() {
  noCanvas();
  tree = new Tree();
  tree.add(8);
  tree.add(3);
  tree.add(10);
  tree.add(1);

  console.log(tree);
}

function Node(val) {
  this.left = null;
  this.right = null;
  this.value = val;
}

Node.prototype.addNode = function(node) {
  if(node.value <= this.value) {
    if(this.left == null) {
      this.left = node;
    }
    else {
      this.left.addNode(node);
    }    
  }
  else {
    if(this.right == null) {
      this.right = node;
    }
    else{
      this.right.addNode(node);
    }    
  }
}

function Tree() {
  this.root = null;
}

Tree.prototype.add = function(value) {
  let node = new Node(value);
  if(this.root == null) {
    this.root = node;
  }
  else {
    this.root.addNode(node);
  }
}
