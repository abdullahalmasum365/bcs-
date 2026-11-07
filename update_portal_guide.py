# -*- coding: utf-8 -*-
import re

with open(r'd:\study\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add navigation button in sidebar under data-track="teacher"
sidebar_target = '''          <button onclick="loadLesson('teacher-classroom-daily')" class="lesson-link w-full text-left px-3 py-2 rounded-lg flex items-center gap-2 font-medium border border-transparent hover:border-current/20" data-id="teacher-classroom-daily">
            <span class="shrink-0">●</span>
            <span class="truncate">১.২: ক্লাসরুমের দৈনন্দিন ৪০টি অপরিহার্য বাক্য</span>
          </button>
        </div>'''

sidebar_replacement = '''          <button onclick="loadLesson('teacher-classroom-daily')" class="lesson-link w-full text-left px-3 py-2 rounded-lg flex items-center gap-2 font-medium border border-transparent hover:border-current/20" data-id="teacher-classroom-daily">
            <span class="shrink-0">●</span>
            <span class="truncate">১.২: ক্লাসরুমের দৈনন্দিন ৪০টি অপরিহার্য বাক্য</span>
          </button>
          <button onclick="loadLesson('teacher-mastery-guide')" class="lesson-link w-full text-left px-3 py-2 rounded-lg flex items-center gap-2 font-medium border border-transparent hover:border-current/20 text-blue-600 dark:text-blue-400 font-bold" data-id="teacher-mastery-guide">
            <span class="shrink-0">⭐</span>
            <span class="truncate">১.৩: Spoken English & Grammar Mastery Guide (ভিজ্যুয়াল PDF)</span>
          </button>
        </div>'''

if sidebar_target in content:
    content = content.replace(sidebar_target, sidebar_replacement)
    print("Sidebar button added successfully!")
else:
    print("WARNING: sidebar_target not found!")

# 2. Add LESSON_DATABASE entry for teacher-mastery-guide
lesson_target = '''                <div class="p-2 rounded eink-card border eink-border">16. <em>"Have a great day, see you in the next class."</em></div>
              </div>
            </div>
          </div>
        `
      },
    };'''

lesson_code = '''                <div class="p-2 rounded eink-card border eink-border">16. <em>"Have a great day, see you in the next class."</em></div>
              </div>
            </div>
          </div>
        `
      },

      // ----------------------------------------------------
      // TEACHER'S MASTER SPOKEN & GRAMMAR GUIDE (PDF EDITION)
      // ----------------------------------------------------
      'teacher-mastery-guide': {
        category: 'শিক্ষকের স্পোকেন ও ক্লাসরুম ইংরেজি',
        dateCreated: '০৭ নভেম্বর ২০২৬',
        lastUpdated: '০৭ নভেম্বর ২০২৬',
        badge: 'টেন্স, V3, প্রিপজিশন, SAR ফ্রেমওয়ার্ক ও বোর্ড বানান স্পেশাল',
        title: '১.৩: The CS Teacher Spoken English & Grammar Mastery Guide (ভিজ্যুয়াল হ্যান্ডবুক)',
        readTime: '২০ মিনিট পূর্ণাঙ্গ গাইড',
        html: `
          <div class="space-y-6 text-xs sm:text-sm leading-relaxed">
            
            <!-- Download Banner -->
            <div class="p-5 rounded-xl border border-blue-500/30 bg-blue-50/60 dark:bg-blue-950/30 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div>
                <span class="px-2 py-0.5 rounded bg-blue-600 text-white font-bold text-[10px] uppercase tracking-wider">অফিসিয়াল প্রিন্ট এডিশন</span>
                <h3 class="font-bold text-base text-blue-900 dark:text-blue-200 mt-1">📄 পূর্ণাঙ্গ ৬ পৃষ্ঠার অল-ইন-ওয়ান কালার PDF গাইড</h3>
                <p class="text-xs text-blue-800/80 dark:text-blue-300/80 mt-0.5">সবগুলো ভিজ্যুয়াল ডায়াগ্রাম, ছক ও ফর্মুলা সমন্বিত হাই-কোয়ালিটি প্রিন্ট রেডি ডকুমেন্ট।</p>
              </div>
              <div class="flex gap-2 shrink-0">
                <a href="English_Mastery_Guide_For_CS_Educator.pdf" download target="_blank" class="px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs flex items-center gap-1.5 shadow transition">
                  📥 ডাউনলোড করুন PDF (766 KB)
                </a>
                <a href="English_Mastery_Guide_For_CS_Educator.html" target="_blank" class="px-3 py-2 rounded-lg border border-blue-400 text-blue-700 dark:text-blue-300 font-semibold text-xs hover:bg-blue-100/50 transition">
                  🌐 ওয়েব ভিউ
                </a>
              </div>
            </div>

            <!-- MODULE 1: 3-STATE TENSE ENGINE -->
            <div class="eink-surface p-5 rounded-xl border eink-border space-y-4">
              <div class="flex items-center justify-between border-b eink-border pb-2">
                <h3 class="font-bold text-base flex items-center gap-2">⚡ মডিউল ১: The 3-State Spoken Tense Engine</h3>
                <span class="text-[10px] px-2 py-0.5 rounded eink-card border eink-border font-bold">১২ টেন্সের জটলা মুক্ত</span>
              </div>
              <p class="opacity-90">
                কথা বলার সময় ১২টি টেন্সের কথা ভুলে যান। একজন প্রোগ্রামার হিসেবে ৩টি স্টেটে ভাবুন:
              </p>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                <div class="p-3 rounded-lg eink-card border eink-border space-y-1">
                  <div class="font-bold text-blue-600 dark:text-blue-400">STATE 1: Present (V1)</div>
                  <div class="text-[11px] opacity-75">রুটিন, অভ্যাস, পেশা, সফটওয়্যার লজিক</div>
                  <div class="font-mono font-bold text-[11px]">Subject + V1 (s/es)</div>
                  <div class="italic text-[11px] opacity-90">"I teach coding everyday."</div>
                </div>
                <div class="p-3 rounded-lg eink-card border eink-border space-y-1">
                  <div class="font-bold text-rose-600 dark:text-rose-400">STATE 2: Past (V2)</div>
                  <div class="text-[11px] opacity-75">অতীতের গল্প, আগের দিনের ক্লাস, শেষ ঘটনা</div>
                  <div class="font-mono font-bold text-[11px]">Subject + V2</div>
                  <div class="italic text-[11px] opacity-90">"Yesterday, I taught Scratch."</div>
                </div>
                <div class="p-3 rounded-lg eink-card border eink-border space-y-1">
                  <div class="font-bold text-emerald-600 dark:text-emerald-400">STATE 3: Future</div>
                  <div class="text-[11px] opacity-75">সামনের ক্লাসের প্ল্যান, পরবর্তী অ্যাকশন</div>
                  <div class="font-mono font-bold text-[11px]">Subject + will + V1</div>
                  <div class="italic text-[11px] opacity-90">"Tomorrow, we will start loops."</div>
                </div>
              </div>
              <div class="p-3 rounded-lg bg-rose-500/10 border border-rose-500/30 text-rose-800 dark:text-rose-200 text-xs">
                <strong>⚠️ The Golden DID Rule:</strong> অতীতে প্রশ্ন করতে বা 'না' বলতে সেন্টেন্সে যখনই <strong>DID</strong> আসে, মূল ভার্ব সবসময় তার আদি রূপ <strong>V1</strong>-এ ফিরে যায়!<br>
                • ❌ "The cat did not moved." ➔ ✅ "The cat <strong>did not move</strong>."<br>
                • ❌ "Did you saw the bug?" ➔ ✅ "Did you <strong>see</strong> the bug?"
              </div>
            </div>

            <!-- MODULE 2: V3 DEMYSTIFIED -->
            <div class="eink-surface p-5 rounded-xl border eink-border space-y-4">
              <div class="flex items-center justify-between border-b eink-border pb-2">
                <h3 class="font-bold text-base flex items-center gap-2">🛡️ মডিউল ২: V3 (Past Participle) Demystified</h3>
                <span class="text-[10px] px-2 py-0.5 rounded eink-card border eink-border font-bold">Finished Status Flag</span>
              </div>
              <p class="opacity-90">
                <strong>V3 পাস্ট টেন্স নয়—এটি একটি Finished Status Flag!</strong> এটি বোঝায় কাজটি সম্পন্ন এবং রেজাল্ট চোখের সামনে আছে।
              </p>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div class="p-3 rounded-lg eink-card border eink-border">
                  <div class="font-bold text-rose-600 dark:text-rose-400 mb-1">V2 (Past Simple) = ইতিহাস</div>
                  <p class="opacity-80">অতীতে শেষ হয়েছে, বর্তমানের সাথে সম্পর্ক নেই।</p>
                  <div class="font-mono mt-1 font-semibold">"I sent the CV yesterday."</div>
                  <div class="text-[10px] opacity-60">(গতকাল পাঠিয়েছিলাম, তারিখ অতীত)</div>
                </div>
                <div class="p-3 rounded-lg eink-card border eink-border">
                  <div class="font-bold text-emerald-600 dark:text-emerald-400 mb-1">have + V3 = কমপ্লিট স্ট্যাটাস</div>
                  <p class="opacity-80">কাজটি এইমাত্র শেষ এবং প্রমাণ এখন রেডি!</p>
                  <div class="font-mono mt-1 font-semibold">"I have sent the CV."</div>
                  <div class="text-[10px] opacity-60">(এইমাত্র পাঠিয়েছি, মেইল চলে গেছে দেখুন)</div>
                </div>
              </div>
              <div class="p-3 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-900 dark:text-amber-200 text-xs">
                <strong>🛡️ The Bodyguard Rule:</strong> V3 কখনো একা বসতে পারে না! এর আগে সবসময় বডিগার্ড থাকে (<code>have / has / had / is / was</code>)। বডিগার্ড না থাকলে ভুলেও V3 মুখে আনবেন না।
              </div>
            </div>

            <!-- MODULE 3: PREPOSITIONS VIA MENTAL PHYSICS -->
            <div class="eink-surface p-5 rounded-xl border eink-border space-y-4">
              <div class="flex items-center justify-between border-b eink-border pb-2">
                <h3 class="font-bold text-base flex items-center gap-2">🎯 মডিউল ৩: Prepositions via Mental Physics (ভিজ্যুয়াল ছবি)</h3>
                <span class="text-[10px] px-2 py-0.5 rounded eink-card border eink-border font-bold">৩টি মনের চোখ দিয়ে দেখা ছবি</span>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                <div class="p-3 rounded-lg eink-card border eink-border space-y-1">
                  <div class="font-bold text-blue-600 dark:text-blue-400">🎯 ১. Dartboard (AT)</div>
                  <p class="opacity-80">নির্দিষ্ট টার্গেট নিশানা বা স্কিল পয়েন্ট।</p>
                  <ul class="list-disc list-inside space-y-0.5 font-mono text-[11px]">
                    <li>good <strong>at</strong> coding</li>
                    <li>look <strong>at</strong> the board</li>
                    <li>starts <strong>at</strong> 9:00 AM</li>
                  </ul>
                </div>
                <div class="p-3 rounded-lg eink-card border eink-border space-y-1">
                  <div class="font-bold text-indigo-600 dark:text-indigo-400">📦 ২. Box vs Table (Into/Onto)</div>
                  <p class="opacity-80">ত্রিমাত্রিক বাক্সের ভেতরে vs সমতল তলের ওপর।</p>
                  <ul class="list-disc list-inside space-y-0.5 font-mono text-[11px]">
                    <li>save <strong>into</strong> folder</li>
                    <li>drag <strong>onto</strong> screen</li>
                    <li>insert <strong>into</strong> laptop</li>
                  </ul>
                </div>
                <div class="p-3 rounded-lg eink-card border eink-border space-y-1">
                  <div class="font-bold text-emerald-600 dark:text-emerald-400">➡️ ৩. Voice Arrow vs Gift (To/For)</div>
                  <p class="opacity-80">কথা বা গতির দিক vs উদ্দেশ্য বা উপহার।</p>
                  <ul class="list-disc list-inside space-y-0.5 font-mono text-[11px]">
                    <li>listen <strong>to</strong> me</li>
                    <li>explain <strong>to</strong> students</li>
                    <li>games <strong>for</strong> kids</li>
                  </ul>
                </div>
              </div>

              <!-- BY vs WITH Table -->
              <div class="p-3 rounded-lg bg-current/5 border eink-border text-xs space-y-2">
                <div class="font-bold">⚡ BY বনাম WITH — কে করল vs কী দিয়ে করল:</div>
                <p>• <strong>BY (The Agent):</strong> মানুষ বা যার দ্বারা করা হয়েছে ➔ <em>"The game was made <strong>by</strong> Rahul."</em></p>
                <p>• <strong>WITH (The Tool):</strong> যে যন্ত্র বা সফটওয়্যার দিয়ে করা হয়েছে ➔ <em>"...<strong>with</strong> Scratch and a mouse."</em></p>
                <p class="font-semibold text-emerald-700 dark:text-emerald-300">➔ "The animation was designed BY Sarah WITH a tablet."</p>
              </div>
            </div>

            <!-- MODULE 4: SAR SITUATION FRAMEWORK -->
            <div class="eink-surface p-5 rounded-xl border eink-border space-y-4">
              <div class="flex items-center justify-between border-b eink-border pb-2">
                <h3 class="font-bold text-base flex items-center gap-2">🎬 মডিউল ৪: SAR Framework (পরিস্থিতি ব্যাখ্যার ৩-শট ইঞ্জিন)</h3>
                <span class="text-[10px] px-2 py-0.5 rounded eink-card border eink-border font-bold">Situation ➔ Action ➔ Resolution</span>
              </div>
              <p class="opacity-90">বাংলায় বড় বাক্য চিন্তা না করে ৩টি ছোট ক্যামেরা শটে ঘটনা বলুন:</p>
              <div class="space-y-2 text-xs">
                <div class="p-2.5 rounded eink-card border eink-border flex gap-2">
                  <span class="font-bold text-blue-600 dark:text-blue-400 shrink-0">[S - Situation]:</span>
                  <span>"Yesterday, a Grade 2 student wrote a code in Scratch."</span>
                </div>
                <div class="p-2.5 rounded eink-card border eink-border flex gap-2">
                  <span class="font-bold text-rose-600 dark:text-rose-400 shrink-0">[A - Action/Problem]:</span>
                  <span>"His sprite did not move, and he felt upset."</span>
                </div>
                <div class="p-2.5 rounded eink-card border eink-border flex gap-2">
                  <span class="font-bold text-emerald-600 dark:text-emerald-400 shrink-0">[R - Resolution]:</span>
                  <span>"I helped him find the bug, and he fixed the coordinates."</span>
                </div>
              </div>
            </div>

            <!-- MODULE 5: WHITEBOARD SPELLING HACKS -->
            <div class="eink-surface p-5 rounded-xl border eink-border space-y-4">
              <div class="flex items-center justify-between border-b eink-border pb-2">
                <h3 class="font-bold text-base flex items-center gap-2">✍️ মডিউল ৫: হোয়াইটবোর্ড বানান নির্ভুল করার গোল্ডেন রুলস</h3>
                <span class="text-[10px] px-2 py-0.5 rounded eink-card border eink-border font-bold">Spelling Phobia Cure</span>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div class="p-3 rounded-lg eink-card border eink-border">
                  <div class="font-bold text-blue-600 dark:text-blue-400 mb-1">১. 1-1-1 CVC ডাবলিং রুল</div>
                  <p class="opacity-80">১টি Syllable + ১ Vowel + ১ Consonant থাকলে শেষের অক্ষর ডাবল হবে:</p>
                  <p class="font-mono mt-1">• Stop ➔ Stop<strong>ped</strong> / Stop<strong>ping</strong></p>
                  <p class="font-mono">• Run ➔ Run<strong>ning</strong> | Plan ➔ Plan<strong>ned</strong></p>
                </div>
                <div class="p-3 rounded-lg eink-card border eink-border">
                  <div class="font-bold text-blue-600 dark:text-blue-400 mb-1">২. সাইলেন্ট 'E' ড্রপ রুল</div>
                  <p class="opacity-80">শেষে অনুচ্চারিত 'e' থাকলে 'ing' যোগ করার সময় 'e' মুছে যাবে:</p>
                  <p class="font-mono mt-1">• Code ➔ Cod<strong>ing</strong> (Codeing ❌)</p>
                  <p class="font-mono">• Write ➔ Writ<strong>ing</strong> | Create ➔ Creat<strong>ing</strong></p>
                </div>
              </div>
              <div class="p-3 rounded-lg eink-card border eink-border text-xs">
                <div class="font-bold mb-1">৩. CS শব্দের চাঙ্কিং মেথড (Chunking Method):</div>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono text-[11px]">
                  <div class="p-1.5 rounded border eink-border text-center"><strong>Al - go - rithm</strong><br><span class="text-[9px] opacity-75">Algorithm</span></div>
                  <div class="p-1.5 rounded border eink-border text-center"><strong>Se - quen - ce</strong><br><span class="text-[9px] opacity-75">Sequence</span></div>
                  <div class="p-1.5 rounded border eink-border text-center"><strong>Sep - a - rate</strong><br><span class="text-[9px] opacity-75">মাঝে a rat 🐀</span></div>
                  <div class="p-1.5 rounded border eink-border text-center"><strong>To - mor - row</strong><br><span class="text-[9px] opacity-75">১টি m, ২টি r</span></div>
                </div>
              </div>
            </div>

            <!-- MODULE 6: MASTER INTERVIEW PITCH -->
            <div class="eink-surface p-5 rounded-xl border eink-border space-y-4">
              <div class="flex items-center justify-between border-b eink-border pb-2">
                <h3 class="font-bold text-base flex items-center gap-2">🎤 মডিউল ৬: The 60-Second Master Interview Pitch</h3>
                <span class="text-[10px] px-2 py-0.5 rounded eink-card border eink-border font-bold">Executive Delivery</span>
              </div>
              <div class="p-4 rounded-lg bg-stone-900 text-stone-100 font-serif italic text-xs leading-relaxed space-y-2">
                <p>"My name is <strong>Abdullah Al Masum</strong>. Currently, I serve as a Computer Science Teacher at <strong>Singapore School Kinderland</strong> and a Global Coding Educator at <strong>BrightChamps</strong>."</p>
                <p>"My core passion is nurturing young minds through <strong>computational thinking</strong> and creative problem-solving."</p>
                <p>"As Artificial Intelligence rapidly reshapes our world, my mission is to build foundational <strong>AI literacy</strong> and <strong>technology ethics</strong> from an early age—empowering our students to become confident <strong>creators of technology, rather than just passive consumers</strong>."</p>
              </div>
            </div>

          </div>
        `
      },
    };'''

if lesson_target in content:
    content = content.replace(lesson_target, lesson_code)
    print("Lesson database entry added successfully!")
else:
    print("WARNING: lesson_target not found!")

with open(r'd:\study\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")
