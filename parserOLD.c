#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  FILE *infile, *outfile;
  if(argc != 3)
  {
    printf("To use this program:\n./parser inputfile outputfile\n");
    return -1;
  }
  infile = fopen(argv[1], "r");
  outfile = fopen(argv[2], "w");
  int level = 1;  //Stores the level of nesting, 1 because 0 is dblp

  char line[256];
  char type[64];
  char *t;
  size_t size;
  char element[10][256];  //Stores the strings needed to be copied
  int num, sub_num;

//remove any header labels
  fgets(line, 256, infile);
  while((line[1] == '?') | (line[1] == '!'))
    fgets(line, 256, infile);

  fprintf(outfile, "digraph { \nrankdir=LR\n\nnode [shape =\"box\"]\n");
  
  //Remove brackets
  t = line;
  t++;
  num = strlen(t);
  t[num - 2] = '\0';
  strcpy(element[0], t);
  fprintf(outfile, "%s [label=", element[0]);
  fprintf(outfile, "\"%s\"]\n", element[0]);
  num = 0;

  while(fgets(line, 256, infile) != NULL)
  {
    if ((level == 1) && (line[0] == '<') && (line[1] != '/'))
    {
      sprintf(element[1], "article%d", num);
      num++;
      
      //Gets the date
      t = strtok(line, "\"");
      t = strtok(NULL, "\"");
      fprintf(outfile, "node [shape = \"box\"]\n"); //change node shape
      fprintf(outfile, "%s [label=\"ARTICLE\\n", element[1]);
      fprintf(outfile, "%s\\nkey: ", t);
      
      //Gets the article key
      t = strtok(NULL, "\"");
      t = strtok(NULL, "\"");
      fprintf(outfile, "%s\"]\n", t);
      fprintf(outfile, "%s -> {", element[0]);
      fprintf(outfile, "%s}\n", element[1]);
      level++;
      sub_num = 0;
    } else {//not article
      if(line[0] == '<')
      {
        if(line[1] == '/')//Closing
        {
          level--;
        } else {//New element
          t = strtok(line, "<>");
          strcpy(type, t);
          sprintf(element[level], "%s%d", type, num - 1);
          fprintf(outfile, "node [shape = \"oval\"]\n");
          fprintf(outfile, "%s [label =\"", element[level]);
          fprintf(outfile, "%s\\n", type);
          //Obtain attribute value
          t = strtok(NULL, "<>");
          fprintf(outfile, "%s\"]\n", t);
          t = strtok(NULL, "<>");
          fprintf(outfile, "%s -> {", element[level - 1]);
          fprintf(outfile, "%s}\n", element[level]);
        }
      }
    }
  }
  fprintf(outfile, "}");
  return 0;
}
