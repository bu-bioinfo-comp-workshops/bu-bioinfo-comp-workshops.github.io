## Workshop 1: DNA Sequence Quality Assessment

**Problem Statement**: You have received FASTQ files from a bacterial genome sequencing project. Your collaborator wants to know: "Are these sequences good quality? Should we proceed with assembly or re-sequence?" You need to provide a definitive answer with supporting data.

**Target Result**: A quality report stating "PROCEED" or "RE-SEQUENCE" with:

- Average read length and quality scores
- Percentage of reads below Q20
- GC content distribution plot
- Recommendation with justification

**Technical Skills Introduced**:

- Conda environment setup and package management
- Basic CLI commands for file inspection
- Python/R file reading and basic statistics
- Simple data visualization

**Workshop Structure**:

1. **Environment Setup** (30 min):
    
    - Problem: "Create a conda environment with tools needed for sequence analysis"
    - Students prompt LLM to generate conda environment creation commands
    - Debug installation issues with LLM assistance
2. **File Exploration** (30 min):
    
    - Problem: "Examine FASTQ file structure without loading entire files into memory"
    - Prompt LLM for CLI commands to inspect files
    - Learn head, tail, wc, grep through LLM guidance
3. **Quality Analysis Coding** (150 min):
    
    - Main problem: Generate code to read FASTQ, calculate statistics, make plots
    - Students iteratively work with LLM to:
        - Read FASTQ files properly
        - Calculate quality metrics
        - Handle any parsing errors
        - Create visualization code
        - Debug plotting issues
4. **Report Generation** (30 min):
    
    - Problem: "Create a final recommendation based on quality thresholds"
    - Use LLM to help format results and create decision logic

**Sample Initial Prompt**: "I have bacterial genome FASTQ files and need Python code to calculate average read quality, read length distribution, and GC content. The code should determine if average quality is above Q20 and recommend proceeding or re-sequencing."