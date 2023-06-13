(function() {
  let child1 = document.createElement("li");
  let child2 = document.createElement("li");
  let child3 = document.createElement("li");
  child1.textContent = "1";
  child1.textContent = "2";
  child1.textContent = "3";
  let parent = document.getElementById("test");
  parent.appendChild(child1);
  parent.appendChild(child2);
  parent.appendChild(child3);
})();